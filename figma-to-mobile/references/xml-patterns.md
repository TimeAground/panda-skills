# XML Layout Patterns Reference

## Basic Mapping

### LinearLayout Vertical
```xml
<LinearLayout
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:orientation="vertical"
    android:padding="16dp">
    <!-- children -->
</LinearLayout>
```

### LinearLayout Horizontal
```xml
<LinearLayout
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:orientation="horizontal"
    android:gravity="center_vertical">
    <!-- children -->
</LinearLayout>
```

### FrameLayout (Overlay)
```xml
<FrameLayout
    android:layout_width="351dp"
    android:layout_height="210dp"
    android:background="@drawable/bg_rounded_white">
    <!-- children -->
</FrameLayout>
```

### ConstraintLayout
```xml
<androidx.constraintlayout.widget.ConstraintLayout
    android:layout_width="match_parent"
    android:layout_height="wrap_content">
    <!-- Use for complex layouts with relative positioning -->
</androidx.constraintlayout.widget.ConstraintLayout>
```

### TextView
```xml
<TextView
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    android:text="Title"
    android:textSize="17sp"
    android:textColor="#0F0F0F"
    android:textStyle="bold" />
```

### ImageView
```xml
<ImageView
    android:layout_width="match_parent"
    android:layout_height="200dp"
    android:scaleType="centerCrop"
    android:src="@drawable/placeholder"
    android:contentDescription="description" />
```

### Button
```xml
<Button
    android:layout_width="match_parent"
    android:layout_height="40dp"
    android:text="Button Text"
    android:textColor="#FFFFFF"
    android:textSize="16sp"
    android:backgroundTint="#0158FF" />
```

### EditText / Input
```xml
<EditText
    android:layout_width="match_parent"
    android:layout_height="44dp"
    android:hint="Placeholder"
    android:background="@drawable/bg_input"
    android:padding="12dp"
    android:textSize="14sp" />
```

### CardView
```xml
<com.google.android.material.card.MaterialCardView
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    app:cardCornerRadius="12dp"
    app:cardBackgroundColor="#FFFFFF"
    app:cardElevation="2dp">
    <!-- content -->
</com.google.android.material.card.MaterialCardView>
```

## Color Conversion
Same as Compose: Figma (0-1) → Android hex #AARRGGBB

## Size Conversion
- Figma px → Android dp (1:1)
- Figma font px → Android sp (1:1)

## Auto-layout Mapping

| Figma Property | XML Equivalent |
|---|---|
| layoutMode: VERTICAL | LinearLayout orientation=vertical |
| layoutMode: HORIZONTAL | LinearLayout orientation=horizontal |
| itemSpacing | Use marginTop/marginStart on children |
| padding | android:padding on parent |
| primaryAxisAlignItems: CENTER | android:gravity=center |
| layoutGrow: 1 | android:layout_weight=1 |
