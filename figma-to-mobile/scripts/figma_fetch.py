#!/usr/bin/env python3
"""Fetch and simplify Figma node data for Android code generation."""

import json
import os
import re
import sys

try:
    import requests
except ImportError:
    print("ERROR: requests not installed. Run: pip install requests")
    sys.exit(1)


def parse_figma_url(url: str):
    """Extract file_key and node_id from a Figma URL."""
    file_match = re.search(r"figma\.com/(?:file|design)/([a-zA-Z0-9]+)", url)
    node_match = re.search(r"node-id=([0-9]+[-:][0-9]+)", url)
    if not file_match:
        return None, None
    file_key = file_match.group(1)
    node_id = node_match.group(1).replace("-", ":") if node_match else None
    return file_key, node_id


def rgba_to_hex(color: dict) -> str:
    """Convert Figma RGBA (0-1) to Android hex #AARRGGBB."""
    r = int(color.get("r", 0) * 255)
    g = int(color.get("g", 0) * 255)
    b = int(color.get("b", 0) * 255)
    a = int(color.get("a", 1) * 255)
    if a == 255:
        return f"#{r:02X}{g:02X}{b:02X}"
    return f"#{a:02X}{r:02X}{g:02X}{b:02X}"


def simplify_node(node: dict, parent_pos: dict = None) -> dict:
    """Simplify a Figma node to only the info needed for code generation."""
    bbox = node.get("absoluteBoundingBox", {})
    result = {
        "type": node.get("type"),
        "name": node.get("name"),
        "width": bbox.get("width"),
        "height": bbox.get("height"),
    }

    # Relative position
    if parent_pos and bbox:
        result["x"] = round(bbox.get("x", 0) - parent_pos.get("x", 0), 1)
        result["y"] = round(bbox.get("y", 0) - parent_pos.get("y", 0), 1)

    # Background color
    fills = node.get("fills", [])
    for fill in fills:
        if fill.get("type") == "SOLID" and fill.get("visible", True):
            result["backgroundColor"] = rgba_to_hex(fill.get("color", {}))
            break
        elif fill.get("type") == "IMAGE":
            result["hasImage"] = True
            break

    # Border
    strokes = node.get("strokes", [])
    for stroke in strokes:
        if stroke.get("type") == "SOLID" and stroke.get("visible", True):
            result["borderColor"] = rgba_to_hex(stroke.get("color", {}))
            result["borderWidth"] = node.get("strokeWeight", 1)
            break

    # Corner radius
    cr = node.get("cornerRadius")
    if cr and cr > 0:
        result["cornerRadius"] = cr

    # Text properties
    if node.get("type") == "TEXT":
        result["text"] = node.get("characters", "")
        style = node.get("style", {})
        if style:
            result["fontSize"] = style.get("fontSize")
            result["fontWeight"] = style.get("fontWeight")
            result["textAlignHorizontal"] = style.get("textAlignHorizontal")
        # Text color from fills
        for fill in fills:
            if fill.get("type") == "SOLID":
                result["textColor"] = rgba_to_hex(fill.get("color", {}))
                break

    # Auto-layout
    layout_mode = node.get("layoutMode")
    if layout_mode:
        result["layoutMode"] = layout_mode  # VERTICAL or HORIZONTAL
        result["itemSpacing"] = node.get("itemSpacing", 0)
        result["paddingLeft"] = node.get("paddingLeft", 0)
        result["paddingRight"] = node.get("paddingRight", 0)
        result["paddingTop"] = node.get("paddingTop", 0)
        result["paddingBottom"] = node.get("paddingBottom", 0)
        result["primaryAxisAlignItems"] = node.get("primaryAxisAlignItems")
        result["counterAxisAlignItems"] = node.get("counterAxisAlignItems")

    # Opacity
    opacity = node.get("opacity")
    if opacity is not None and opacity < 1:
        result["opacity"] = opacity

    # Visibility
    if not node.get("visible", True):
        result["visible"] = False

    # Children
    children = node.get("children", [])
    if children:
        current_pos = {"x": bbox.get("x", 0), "y": bbox.get("y", 0)}
        result["children"] = [
            simplify_node(child, current_pos)
            for child in children
            if child.get("visible", True)
        ]

    return result


def fetch_node(file_key: str, node_id: str, token: str, depth: int = 5) -> dict:
    """Fetch a node from Figma API."""
    api_node_id = node_id.replace(":", "-")
    url = f"https://api.figma.com/v1/files/{file_key}/nodes?ids={api_node_id}&depth={depth}"
    headers = {"X-Figma-Token": token}
    resp = requests.get(url, headers=headers, timeout=30)
    resp.raise_for_status()
    data = resp.json()

    if "err" in data:
        raise Exception(f"Figma API error: {data['err']}")

    node_data = data.get("nodes", {}).get(node_id)
    if not node_data:
        raise Exception(f"Node {node_id} not found in response")

    return node_data["document"]


def main():
    if len(sys.argv) < 2:
        print("Usage: python figma_fetch.py <figma_url> [--depth N]")
        print("Example: python figma_fetch.py 'https://www.figma.com/design/ABC/Project?node-id=100-200'")
        sys.exit(1)

    url = sys.argv[1]
    depth = 5
    if "--depth" in sys.argv:
        idx = sys.argv.index("--depth")
        depth = int(sys.argv[idx + 1])

    token = os.environ.get("FIGMA_TOKEN")
    if not token:
        print("ERROR: FIGMA_TOKEN environment variable not set.")
        print("Get your token: Figma -> Settings -> Personal Access Tokens")
        sys.exit(1)

    file_key, node_id = parse_figma_url(url)
    if not file_key:
        print(f"ERROR: Could not parse Figma URL: {url}")
        sys.exit(1)
    if not node_id:
        print("ERROR: URL must contain a node-id parameter.")
        print("Open a specific frame in Figma and copy the URL.")
        sys.exit(1)

    print(f"Fetching node {node_id} from file {file_key}...", file=sys.stderr)
    raw_node = fetch_node(file_key, node_id, token, depth)
    simplified = simplify_node(raw_node)

    print(json.dumps(simplified, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
