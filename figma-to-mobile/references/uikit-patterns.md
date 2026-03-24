# UIKit Patterns Reference

## Basic Mapping

### UIStackView Vertical
```swift
let stackView = UIStackView()
stackView.axis = .vertical
stackView.spacing = 8
stackView.alignment = .fill
stackView.distribution = .fill
stackView.layoutMargins = UIEdgeInsets(top: 12, left: 16, bottom: 12, right: 16)
stackView.isLayoutMarginsRelativeArrangement = true
```

### UIStackView Horizontal
```swift
let stackView = UIStackView()
stackView.axis = .horizontal
stackView.spacing = 8
stackView.alignment = .center
```

### UIView (Container)
```swift
let container = UIView()
container.backgroundColor = .white
container.layer.cornerRadius = 12
container.translatesAutoresizingMaskIntoConstraints = false
NSLayoutConstraint.activate([
    container.widthAnchor.constraint(equalToConstant: 351),
    container.heightAnchor.constraint(equalToConstant: 210)
])
```

### UILabel
```swift
let label = UILabel()
label.text = "Title"
label.font = .systemFont(ofSize: 17, weight: .bold)
label.textColor = UIColor(hex: "0F0F0F")
```

### UIImageView
```swift
let imageView = UIImageView()
imageView.contentMode = .scaleAspectFill
imageView.clipsToBounds = true
imageView.translatesAutoresizingMaskIntoConstraints = false
NSLayoutConstraint.activate([
    imageView.heightAnchor.constraint(equalToConstant: 200)
])
```

### UIButton
```swift
let button = UIButton(type: .system)
button.setTitle("Button Text", for: .normal)
button.setTitleColor(.white, for: .normal)
button.titleLabel?.font = .systemFont(ofSize: 16)
button.backgroundColor = UIColor(hex: "0158FF")
button.layer.cornerRadius = 8
button.translatesAutoresizingMaskIntoConstraints = false
NSLayoutConstraint.activate([
    button.heightAnchor.constraint(equalToConstant: 40)
])
```

### UITextField
```swift
let textField = UITextField()
textField.placeholder = "Placeholder"
textField.font = .systemFont(ofSize: 14)
textField.backgroundColor = UIColor(hex: "F7F7F7")
textField.layer.cornerRadius = 8
textField.leftView = UIView(frame: CGRect(x: 0, y: 0, width: 12, height: 0))
textField.leftViewMode = .always
```

### Card-like View
```swift
let card = UIView()
card.backgroundColor = .white
card.layer.cornerRadius = 12
card.layer.shadowColor = UIColor.black.cgColor
card.layer.shadowOpacity = 0.1
card.layer.shadowRadius = 4
card.layer.shadowOffset = CGSize(width: 0, height: 2)
```

## Color Conversion

UIColor hex extension (include in generated code):
```swift
extension UIColor {
    convenience init(hex: String) {
        let scanner = Scanner(string: hex)
        var rgb: UInt64 = 0
        scanner.scanHexInt64(&rgb)
        self.init(
            red: CGFloat((rgb >> 16) & 0xFF) / 255.0,
            green: CGFloat((rgb >> 8) & 0xFF) / 255.0,
            blue: CGFloat(rgb & 0xFF) / 255.0,
            alpha: 1.0
        )
    }
}
```

## Size Conversion
- Figma px → UIKit pt (1:1)
- Use CGFloat for all dimensions
- Font sizes: .systemFont(ofSize:) with pt values

## Auto-layout Mapping

| Figma Property | UIKit Equivalent |
|---|---|
| layoutMode: VERTICAL | UIStackView axis=.vertical |
| layoutMode: HORIZONTAL | UIStackView axis=.horizontal |
| itemSpacing | stackView.spacing |
| padding | layoutMargins + isLayoutMarginsRelativeArrangement |
| primaryAxisAlignItems: CENTER | distribution = .equalCentering |
| counterAxisAlignItems: CENTER | alignment = .center |
| layoutGrow: 1 | setContentHuggingPriority(.defaultLow) |

## Layout Approach

Prefer programmatic Auto Layout:
1. Set translatesAutoresizingMaskIntoConstraints = false
2. Use NSLayoutConstraint.activate([])
3. Use UIStackView for linear layouts (reduces constraint count)
4. Use direct constraints for complex/absolute positioning
