# XML Layout Patterns — Figma to Android Mapping

> Purpose: Map Figma properties to Android XML attributes.
> This is a **mapping reference**, not an Android tutorial — the agent already knows Android conventions.
> Also includes **real-project usage patterns** — what experienced Android devs actually use in production.

## Layout Selection Guide

| Figma Structure | Recommended Layout |
|---|---|
| Complex with overlaps / relative positioning | **ConstraintLayout** (default choice) |
| Simple vertical/horizontal stack, no overlap | LinearLayout |
| Children overlapping / z-stacking | FrameLayout |
| Repeating similar items (≥3) | RecyclerView + item layout |

## Page Architecture Patterns

These patterns reflect how Android apps are **actually structured** in production.
When generating code, think about the **page-level architecture**, not just individual views.

### Multi-Tab Pages
When a design shows **multiple tabs** (≥2 text labels acting as navigation):
- Use `TabLayout` + `ViewPager2` (or legacy `ViewPager`) — this is the standard pattern
- Do NOT use plain TextViews for tabs — they lack selection state, indicators, and swipe support
- The content area below tabs should be a `FrameLayout` or `ViewPager2` container, NOT the final content directly
- Each tab's content lives in its own **Fragment** with its own layout XML
- Output: main layout (with TabLayout + container) + separate fragment layout(s) for each tab's content

```xml
<!-- Standard Tab + ViewPager2 structure -->
<com.google.android.material.tabs.TabLayout
    android:id="@+id/tabLayout"
    android:layout_width="0dp"
    android:layout_height="48dp"
    app:tabIndicatorColor="#0F0F0F"
    app:tabSelectedTextColor="#0F0F0F"
    app:tabTextColor="#858A99"
    app:tabGravity="center"
    app:tabMode="fixed" />

<androidx.viewpager2.widget.ViewPager2
    android:id="@+id/viewPager"
    android:layout_width="0dp"
    android:layout_height="0dp" />
```

### Navigation Bar Buttons
- **Back/close buttons**: Use `ImageView` — simple, reliable, supports `src` + `background` combo
  - Circular background: set `android:background` to a circle shape drawable
  - Icon: set `android:src` to the arrow/close icon
  - The entire thing might also be a single combined asset — when in doubt, use one `ImageView`
- Do NOT use `FrameLayout` wrapping another view for simple icon buttons

```xml
<!-- Back button: ImageView with circle background + icon -->
<ImageView
    android:id="@+id/btnBack"
    android:layout_width="32dp"
    android:layout_height="32dp"
    android:background="@drawable/placeholder"
    android:src="@drawable/placeholder"
    android:scaleType="centerInside"
    android:contentDescription="返回" />
<!-- background = circle shape (#000000), src = white arrow icon -->
```

### Buttons with Icon + Text
`MaterialButton` with `app:icon` has known rendering issues in some configurations.
**Prefer `LinearLayout` + `ImageView` + `TextView`** for reliable icon+text buttons:

```xml
<!-- Outlined button with icon -->
<LinearLayout
    android:id="@+id/btnVideo"
    android:layout_width="0dp"
    android:layout_height="40dp"
    android:orientation="horizontal"
    android:gravity="center"
    android:background="@drawable/placeholder"
    android:clickable="true"
    android:focusable="true">
    <!-- background = rounded rect shape with stroke #DCDCDC, cornerRadius=12dp, solid #FFFFFF -->

    <ImageView
        android:layout_width="20dp"
        android:layout_height="20dp"
        android:src="@drawable/placeholder" />

    <TextView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_marginStart="6dp"
        android:text="查看视频"
        android:textSize="15sp"
        android:textColor="#0F0F0F"
        android:textStyle="bold" />
</LinearLayout>

<!-- Solid filled button (no icon, or icon optional) -->
<TextView
    android:id="@+id/btnReport"
    android:layout_width="0dp"
    android:layout_height="40dp"
    android:gravity="center"
    android:text="查看报告"
    android:textSize="15sp"
    android:textColor="#FFFFFF"
    android:textStyle="bold"
    android:background="@drawable/placeholder" />
<!-- background = rounded rect shape, solid #0158FF, cornerRadius=12dp -->
```

Use `MaterialButton` only for simple text-only buttons where its default styling is sufficient.

### List Item Height Alignment
When a list item has a **left sidebar element** (like a time capsule/tag) and **right content area**:
- Both sides should have **matching height** — use ConstraintLayout constraints to align top-to-top and bottom-to-bottom
- Or set both to the same fixed height
- Do NOT let one side be `wrap_content` while the other is fixed — they will look misaligned

## ConstraintLayout Mapping

```xml
<androidx.constraintlayout.widget.ConstraintLayout
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:padding="16dp">

    <TextView
        android:id="@+id/tvTitle"
        android:layout_width="0dp"
        android:layout_height="wrap_content"
        android:text="标题"
        android:textSize="17sp"
        android:textColor="#0F0F0F"
        android:textStyle="bold"
        app:layout_constraintTop_toTopOf="parent"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintEnd_toStartOf="@id/ivArrow" />

    <ImageView
        android:id="@+id/ivArrow"
        android:layout_width="24dp"
        android:layout_height="24dp"
        android:src="@drawable/placeholder"
        app:layout_constraintTop_toTopOf="@id/tvTitle"
        app:layout_constraintBottom_toBottomOf="@id/tvTitle"
        app:layout_constraintEnd_toEndOf="parent" />
</androidx.constraintlayout.widget.ConstraintLayout>
```

Key constraint patterns:
- **Centering**: `constraintTop_toTopOf + constraintBottom_toBottomOf` same target
- **Chains**: horizontal/vertical chains for distributing elements
- **0dp (match_constraints)**: fill available space between constraints
- **Guidelines**: use for percentage-based positioning
- **Barrier**: align to the largest of a group

## Auto-layout Mapping

| Figma Property | XML Equivalent |
|---|---|
| layoutMode: VERTICAL | LinearLayout vertical / ConstraintLayout vertical chain |
| layoutMode: HORIZONTAL | LinearLayout horizontal / ConstraintLayout horizontal chain |
| itemSpacing | marginTop/marginStart on children |
| padding* | android:padding on parent |
| primaryAxisAlignItems: CENTER | gravity=center / chain spread_inside |
| counterAxisAlignItems: CENTER | gravity=center_vertical/horizontal |
| layoutGrow: 1 | layout_weight=1 (Linear) / 0dp + constraints (Constraint) |
| primaryAxisSizingMode: FIXED | layout_height/width = exact dp |
| counterAxisSizingMode: AUTO | layout_width/height = wrap_content |

## Size Conversion

- Figma px → Android dp (1:1)
- Figma font px → Android sp (1:1)

## Shadow Mapping

```xml
<!-- Use MaterialCardView for elevation shadow -->
<com.google.android.material.card.MaterialCardView
    app:cardElevation="4dp"
    app:cardCornerRadius="12dp">
```

For custom shadows (specific color/offset): use `android:elevation` + `android:outlineSpotShadowColor` (API 28+) or a drawable background with shadow layer.

## Gradient Mapping

```xml
<!-- Define in drawable XML -->
<shape>
    <gradient
        android:startColor="#FF6B6B"
        android:endColor="#4ECDC4"
        android:angle="90" />
</shape>
```
