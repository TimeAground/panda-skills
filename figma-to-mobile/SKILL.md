---
name: figma-to-mobile
description: >
  Convert Figma designs to mobile UI code.
  Supports Android (Jetpack Compose, XML) and iOS (SwiftUI, UIKit).
  Use when a user provides a Figma link and wants mobile layout code.
  Extracts design tokens via Figma REST API and generates
  production-ready code for the chosen platform and framework.
---

# Figma to Mobile

Convert Figma designs to mobile UI code.

Supported output formats:
- **Android**: Jetpack Compose (Kotlin) / XML Layout
- **iOS**: SwiftUI / UIKit (Storyboard code or programmatic)

## Prerequisites

- `FIGMA_TOKEN` environment variable set with a Figma Personal Access Token
- Python 3.8+ (for the fetch script)
- `requests` Python package (`pip install requests`)

## Workflow

### Step 1: Get User Input

Ask the user for:
1. **Figma link** — URL of a specific Frame or Component (not entire file)
2. **Platform & format** — one of:
   - Android Compose
   - Android XML
   - iOS SwiftUI
   - iOS UIKit
3. **Project context** (optional) — existing theme, design system, component library

Example valid URLs:
- `https://www.figma.com/design/ABC123/Project?node-id=100-200`
- `https://www.figma.com/file/ABC123/Project?node-id=100:200`

### Step 2: Fetch Design Data

Run the fetch script:

```bash
python3 scripts/figma_fetch.py "<figma_url>"
```

The script outputs simplified JSON containing for each element:
- type, name, size (width x height)
- position (x, y relative to parent)
- fills (background colors), strokes (borders)
- text content, font size, font weight, text color
- layout mode (auto-layout direction, spacing, padding)
- corner radius
- children (nested)

### Step 3: Generate Code

Read the appropriate reference file:
- **Android Compose** → `references/compose-patterns.md`
- **Android XML** → `references/xml-patterns.md`
- **iOS SwiftUI** → `references/swiftui-patterns.md`
- **iOS UIKit** → `references/uikit-patterns.md`

#### Universal Rules (all platforms)

1. **Figma type mapping** (see platform-specific reference for exact components):
   - FRAME with auto-layout VERTICAL → vertical stack/list
   - FRAME with auto-layout HORIZONTAL → horizontal stack/row
   - FRAME without auto-layout → overlay/absolute container
   - TEXT → text label
   - RECTANGLE → view with background
   - INSTANCE → expand as children
   - GROUP → transparent container

2. **Design token conversion:**
   - Colors: Figma RGBA (0-1) → platform hex format
   - Font sizes: Figma px → sp (Android) / pt (iOS)
   - Spacing/dimensions: Figma px → dp (Android) / pt (iOS)
   - Corner radius: same conversion as spacing

3. **Code quality:**
   - Use meaningful names from Figma layer names
   - Add comments for major sections
   - Generate compilable/buildable code
   - Follow platform conventions and idioms

4. **DO NOT:**
   - Use absolute positioning (prefer relative/stack layouts)
   - Hard-code user-visible strings
   - Modify the Figma file in any way

### Step 4: Present Results

Show the generated code and ask:
- Does it match the design?
- Any components to adjust?
- Want a different platform output for the same design?

## Error Handling

- FIGMA_TOKEN not set → tell user: Figma → Settings → Personal Access Tokens
- Invalid URL → show example format
- API error → show error message
- Node too large (>200 children) → suggest selecting a smaller frame
