# Compose Patterns Reference

## Basic Mapping

### Column (Vertical Layout)
```kotlin
Column(
    modifier = Modifier
        .fillMaxWidth()
        .padding(horizontal = 16.dp, vertical = 12.dp),
    verticalArrangement = Arrangement.spacedBy(8.dp)
) {
    // children
}
```

### Row (Horizontal Layout)
```kotlin
Row(
    modifier = Modifier.fillMaxWidth(),
    horizontalArrangement = Arrangement.spacedBy(8.dp),
    verticalAlignment = Alignment.CenterVertically
) {
    // children
}
```

### Box (Overlay/Absolute)
```kotlin
Box(
    modifier = Modifier
        .size(width = 351.dp, height = 210.dp)
        .background(Color(0xFFFFFFFF), RoundedCornerShape(12.dp))
) {
    // children
}
```

### Text
```kotlin
Text(
    text = "Title",
    fontSize = 17.sp,
    fontWeight = FontWeight.Bold,
    color = Color(0xFF0F0F0F)
)
```

### Image Placeholder
```kotlin
Image(
    painter = painterResource(id = R.drawable.placeholder),
    contentDescription = "description",
    modifier = Modifier
        .fillMaxWidth()
        .height(200.dp),
    contentScale = ContentScale.Crop
)
```

### Button
```kotlin
Button(
    onClick = { /* TODO */ },
    modifier = Modifier
        .fillMaxWidth()
        .height(40.dp),
    colors = ButtonDefaults.buttonColors(containerColor = Color(0xFF0158FF)),
    shape = RoundedCornerShape(8.dp)
) {
    Text("Button Text", color = Color.White, fontSize = 16.sp)
}
```

### TextField / Input
```kotlin
OutlinedTextField(
    value = "",
    onValueChange = { /* TODO */ },
    placeholder = { Text("Placeholder") },
    modifier = Modifier.fillMaxWidth(),
    shape = RoundedCornerShape(8.dp)
)
```

### Card
```kotlin
Card(
    modifier = Modifier.fillMaxWidth(),
    shape = RoundedCornerShape(12.dp),
    colors = CardDefaults.cardColors(containerColor = Color.White),
    elevation = CardDefaults.cardElevation(defaultElevation = 2.dp)
) {
    // content
}
```

## Color Conversion

Figma color (r, g, b, a) where values are 0.0-1.0:
- Convert to Android: Color(0xAARRGGBB)
- Formula: each channel = (int)(value * 255)
- Example: r=0.0863, g=0.3412, b=1.0, a=1.0 → Color(0xFF1657FF)

## Size Conversion

- Figma px → Compose dp (1:1 for standard density)
- Figma font px → Compose sp (1:1)
- Use .dp for dimensions, .sp for text sizes

## Auto-layout Mapping

| Figma Property | Compose Equivalent |
|---|---|
| layoutMode: VERTICAL | Column |
| layoutMode: HORIZONTAL | Row |
| itemSpacing | Arrangement.spacedBy(X.dp) |
| paddingLeft/Right/Top/Bottom | Modifier.padding() |
| primaryAxisAlignItems: CENTER | verticalArrangement = Arrangement.Center |
| counterAxisAlignItems: CENTER | horizontalAlignment = Alignment.CenterHorizontally |
| layoutGrow: 1 | Modifier.weight(1f) |
