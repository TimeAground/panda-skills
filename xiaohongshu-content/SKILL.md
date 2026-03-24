---
name: xiaohongshu-content
description: >
  Generate Xiaohongshu (Little Red Book) style content from a product or tool.
  Use when creating social media posts for Xiaohongshu/RED platform.
  Generates: multiple title candidates, full post body, hashtags, and
  cover image prompts. Optimized for engagement and discoverability.
  Supports both tool recommendations and story-driven content.
---

# Xiaohongshu Content Generator

Generate ready-to-publish Xiaohongshu content from a product, tool, or topic.

## When to Use

- User wants to create a Xiaohongshu post
- User has a product/tool/topic and needs content for RED/Xiaohongshu
- User asks for "small red book" or "xhs" content

## Workflow

### Step 1: Gather Info

Ask the user for:
1. **What** - Product name, URL, or topic
2. **Angle** (optional) - Story / tutorial / recommendation / comparison
3. **Series** (optional) - Series name and episode number

If user provides a GitHub URL, auto-research: star count, author, core features, use cases.
If user provides a website URL, visit and extract key selling points.

### Step 2: Generate Content

Output the following sections:

#### Titles (3-5 candidates)

Follow the XHS title formula: **Pain point/Curiosity + Number + Emotion word**

Rules:
- Under 20 characters is ideal
- No technical jargon (no "GitHub", "API", "CLI" in titles)
- User benefit first, product name second
- Include at least one emoji per title

Bad examples:
- "KittenTTS: 25MB open-source TTS model, 13K GitHub stars"
- "SiteSpy: webpage change monitoring tool"

Good examples:
- "Phone can run AI voice-over now, only 25MB, free"
- "After missing a visa appointment, he built a page-watching tool"

#### Body Text (600-900 chars)

Structure:
1. **Hook** (2-3 lines) - Story, pain point, or surprising fact
2. **Core content** - What it does, who needs it, how to use it
3. **Resource hook** (if applicable) - "Comment 'want' to get the package"
4. **Engagement question** - End with a question to drive comments

Style rules:
- Use line breaks liberally (XHS is mobile-first)
- Use emojis as bullet points
- No markdown tables (XHS does not render them)
- No technical terms without explanation
- Write like talking to a friend, not writing documentation

#### Hashtags (6-10)

Mix of:
- High-traffic tags: #AI tool, #free tool, #efficiency
- Medium tags: category-specific
- Long-tail tags: product name

#### Cover Design Brief

- Main text (big characters on cover): benefit/pain point, NOT product name
- Sub text: supporting detail
- Style: dark background + white/colored large text
- Include series tag if applicable

#### Image Prompts (for AI image generation)

For each recommended image (4-6 total), provide:
- Description of what the image should show
- Text overlay content
- Layout guidance

### Step 3: Resource Pack Plan (Optional)

If the product is open-source, generate a resource distribution plan:
- What to include in the pack
- License compatibility check
- Distribution method (comment + DM)
- Wording for the CTA

## Content Angle Templates

Read references/angles.md for detailed angle templates.

## Style Reference

Read references/style-guide.md for XHS writing style rules and examples.
