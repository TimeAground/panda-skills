# XML Layout Patterns — Figma to Android Mapping

> Purpose: Map Figma properties to Android XML attributes.
> This is a **mapping reference**, not an Android tutorial — the agent already knows Android conventions.

## Layout Selection Guide

| Figma Structure | Recommended Layout |
|---|---|
| Complex with overlaps / relative positioning | **ConstraintLayout** (default choice) |
| Simple vertical/horizontal stack, no overlap | LinearLayout |
| Children overlapping / z-stacking | FrameLayout |
| Repeating similar items (≥3) | RecyclerView + item layout |

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
