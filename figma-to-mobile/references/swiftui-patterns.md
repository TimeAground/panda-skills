# SwiftUI Patterns Reference

## Basic Mapping

### VStack (Vertical Layout)
```swift
VStack(alignment: .leading, spacing: 8) {
    // children
}
.padding(.horizontal, 16)
.padding(.vertical, 12)
```

### HStack (Horizontal Layout)
```swift
HStack(spacing: 8) {
    // children
}
```

### ZStack (Overlay)
```swift
ZStack {
    // children (back to front)
}
.frame(width: 351, height: 210)
.background(Color.white)
.cornerRadius(12)
```

### Text
```swift
Text("Title")
    .font(.system(size: 17, weight: .bold))
    .foregroundColor(Color(hex: "0F0F0F"))
```

### Image Placeholder
```swift
Image("placeholder")
    .resizable()
    .aspectRatio(contentMode: .fill)
    .frame(maxWidth: .infinity)
    .frame(height: 200)
    .clipped()
```

### Button
```swift
Button(action: { /* TODO */ }) {
    Text("Button Text")
        .font(.system(size: 16))
        .foregroundColor(.white)
        .frame(maxWidth: .infinity)
        .frame(height: 40)
        .background(Color(hex: "0158FF"))
        .cornerRadius(8)
}
```

### TextField / Input
```swift
TextField("Placeholder", text: $inputText)
    .padding(12)
    .background(Color(hex: "F7F7F7"))
    .cornerRadius(8)
```

### Card-like Container
```swift
VStack {
    // content
}
.padding(16)
.background(Color.white)
.cornerRadius(12)
.shadow(color: .black.opacity(0.1), radius: 4, y: 2)
```

### ScrollView
```swift
ScrollView {
    VStack(spacing: 12) {
        // scrollable content
    }
}
```

## Color Conversion

Figma RGBA (0-1) to SwiftUI:
- Use Color(red:green:blue:opacity:) or a hex extension
- Example: r=0.0863 g=0.3412 b=1.0 → Color(hex: "1657FF")

Hex extension (include in generated code):
```swift
extension Color {
    init(hex: String) {
        let scanner = Scanner(string: hex)
        var rgb: UInt64 = 0
        scanner.scanHexInt64(&rgb)
        self.init(
            red: Double((rgb >> 16) & 0xFF) / 255.0,
            green: Double((rgb >> 8) & 0xFF) / 255.0,
            blue: Double(rgb & 0xFF) / 255.0
        )
    }
}
```

## Size Conversion

- Figma px → SwiftUI pt (1:1 on standard density)
- Use CGFloat values
- Font sizes: use .system(size:) with pt values

## Auto-layout Mapping

| Figma Property | SwiftUI Equivalent |
|---|---|
| layoutMode: VERTICAL | VStack |
| layoutMode: HORIZONTAL | HStack |
| itemSpacing | spacing: parameter |
| paddingLeft/Right/Top/Bottom | .padding() modifiers |
| primaryAxisAlignItems: CENTER | alignment parameter + Spacer() |
| counterAxisAlignItems: CENTER | alignment: .center |
| layoutGrow: 1 | .frame(maxWidth: .infinity) or Spacer() |
