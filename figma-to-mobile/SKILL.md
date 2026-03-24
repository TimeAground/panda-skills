---
name: figma-to-mobile
description: >
  Convert Figma designs to mobile UI code.
  Supports Android (Jetpack Compose, XML) and iOS (SwiftUI, UIKit).
  Use when a user provides a Figma link and wants mobile layout code.
  Extracts design tokens via Figma REST API, asks clarifying questions,
  then generates production-ready code files.
---

# Figma to Mobile

Convert Figma designs to mobile UI code with interactive clarification.

Supported: Android Compose, Android XML, iOS SwiftUI, iOS UIKit.

## Prerequisites

- `FIGMA_TOKEN` environment variable set (Figma > Settings > Personal Access Tokens)
- Python 3.8+ with `requests` package

## Workflow

### Step 1: Fetch & Analyze

When user provides a Figma link:

1. Run `scripts/figma_fetch.py "<url>"` to get design data
2. Analyze the structure: identify sections, repeated patterns, component types
3. Assess confidence for each structural decision

### Step 2: Present Summary & Ask Questions

Show a brief structure summary (tree format, 3-8 lines max).
Then ask ONLY about things you are not confident about.

Rules for questions:
- Max 3-5 questions per interaction
- Each question gives concrete options with one-line pros/cons
- Use natural language, no JSON or technical dumps
- If structure is fully clear, skip questions and go to Step 3

Common questions to ask:
- "These N items look similar — dynamic list (RecyclerView/LazyColumn) or fixed layout?"
- "Output format? XML / Compose / SwiftUI / UIKit"
- "This icon area: single image asset or icon-on-colored-background combo?"
- "Any custom components to use instead of system defaults? (e.g. custom Switch)"

Do NOT ask about:
- Color resource names (write hex directly)
- String resource names (write strings directly)
- Dimension resource names (write dp/sp directly)
- Adapter implementation (do not generate Adapters)

### Step 3: Generate Code

After user confirms, generate code files.

Output rules:
- **Colors**: write hex directly (android:textColor="#0F0F0F" / Color(0xFF0F0F0F))
- **Strings**: write text directly (android:text="通知设置")
- **Dimensions**: write values directly (android:textSize="17sp")
- **Images**: use @drawable/placeholder or Image("placeholder")
- **Layout**: prefer ConstraintLayout for complex, LinearLayout for simple linear flows
- **Lists**: output main layout + separate item layout file. Do NOT generate Adapter.

Platform guidelines (follow strictly, do NOT need to read references for these):
- **Android XML**: follow Material Design 3 specs. Prefer ConstraintLayout as default. Use 8dp grid. Minimum touch target 48dp. Use MaterialSwitch/MaterialCardView over legacy widgets.
- **Android Compose**: follow Material3 composables. Use Modifier chains. LazyColumn for lists. Scaffold for page structure.
- **iOS SwiftUI**: follow Apple HIG. Use NavigationStack, List, VStack/HStack/ZStack. Respect safe areas. Use system fonts/spacing.
- **iOS UIKit**: follow Apple HIG. Use AutoLayout (NSLayoutConstraint or StackView). UITableView/UICollectionView for lists. Respect safe areas.

If multiple files are needed, output each with a clear filename header:
```
📄 activity_notification_settings.xml
[code]

📄 item_expert_notification.xml
[code]
```

Read platform-specific patterns from:
- Android Compose → references/compose-patterns.md
- Android XML → references/xml-patterns.md
- iOS SwiftUI → references/swiftui-patterns.md
- iOS UIKit → references/uikit-patterns.md

### Step 4: Review

After showing code, ask briefly:
- Matches the design?
- Any adjustments needed?
- Want the same design in a different format?

## Error Handling

- **FIGMA_TOKEN not set or invalid** → tell user:
  1. Open Figma → click avatar (top-left) → Settings → Security → Personal Access Tokens
  2. Click "Generate new token", set name and expiration
  3. Copy the token (starts with `figd_`)
  4. Provide it in chat, and the agent will configure it
  If API returns 403/401, the token may have expired or been revoked. Ask user to regenerate.
- **Invalid URL** → show valid URL example: `https://www.figma.com/design/<fileKey>/<name>?node-id=<id>`
- **API error** → show error message, suggest checking network/proxy
- **Node too large (>200 children)** → suggest selecting a smaller frame
