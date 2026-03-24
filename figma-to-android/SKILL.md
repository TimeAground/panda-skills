---
name: figma-to-android
description: >
  Convert Figma designs to Android UI code (Jetpack Compose or XML).
  Use when a user provides a Figma link (frame or component) and wants
  Android layout code generated. Supports both Compose and XML output.
  Extracts design tokens (colors, fonts, spacing, layout hierarchy)
  via Figma REST API and generates production-ready Android code.
---

# Figma to Android

Convert Figma designs to Android UI code. Supports Jetpack Compose and XML layouts.

## Prerequisites

- `FIGMA_TOKEN` environment variable set with a Figma Personal Access Token
- Python 3.8+ (for the fetch script)
- `requests` Python package (`pip install requests`)

## Workflow

### Step 1: Get User Input

Ask the user for:
1. **Figma link** — URL of a specific Frame or Component (not entire file)
2. **Output format** — "Compose" or "XML" (ask if not specified)
3. **Project context** (optional) — existing theme, color scheme, component library name

Example valid URLs:
- `https://www.figma.com/design/ABC123/Project?node-id=100-200`
- `https://www.figma.com/file/ABC123/Project?node-id=100:200`

### Step 2: Fetch Design Data

Run the fetch script to extract design structure:

```bash
python3 scripts/figma_fetch.py "<figma_url>"
```

The script will:
1. Parse the URL to extract file key and node ID
2. Call Figma REST API to get the node tree (depth=5)
3. Output a simplified JSON with only the info needed for code generation

The output JSON contains for each element:
- type, name, size (width x height)
- position (x, y relative to parent)
- fills (background colors)
- strokes (borders)
- text content, font size, font weight, text color
- layout mode (auto-layout direction, spacing, padding)
- corner radius
- children (nested)

### Step 3: Generate Code

Based on the simplified JSON and the user's chosen format:

**If Compose**: Read `references/compose-patterns.md` for patterns and generate Kotlin code.
**If XML**: Read `references/xml-patterns.md` for patterns and generate XML layout code.

#### Code Generation Rules

1. **Map Figma types to Android components:**
   - FRAME with auto-layout VERTICAL → Column (Compose) / LinearLayout vertical (XML)
   - FRAME with auto-layout HORIZONTAL → Row (Compose) / LinearLayout horizontal (XML)
   - FRAME without auto-layout → Box (Compose) / FrameLayout (XML)
   - TEXT → Text (Compose) / TextView (XML)
   - RECTANGLE → Box with background (Compose) / View with background (XML)
   - INSTANCE → Treat as its expanded children
   - GROUP → Treat as transparent container

2. **Extract design tokens:**
   - Colors: convert Figma RGBA (0-1) to Android hex (#AARRGGBB)
   - Font sizes: Figma px → Android sp
   - Spacing/padding: Figma px → Android dp
   - Corner radius: Figma px → Android dp

3. **Code quality:**
   - Use meaningful names from Figma layer names (clean up auto-generated names)
   - Add comments for major sections
   - Use modifier chains in Compose, attributes in XML
   - Generate dimensions as dp/sp constants, colors as hex constants
   - Make the code compilable as-is

4. **DO NOT:**
   - Generate pixel-perfect absolute positioning (use relative layouts)
   - Hard-code strings (use placeholder resources)
   - Modify the Figma file in any way

### Step 4: Present Results

Show the generated code and ask:
- Does it match the design?
- Any components to adjust?
- Want to generate another frame?

## Error Handling

- If FIGMA_TOKEN is not set → tell user how to get one (Figma Settings → Personal Access Tokens)
- If URL is invalid → show example of valid URL format
- If API returns error → show the error message
- If node has too many children (>200) → suggest selecting a smaller frame
