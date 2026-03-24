# figma-to-mobile 设计方案 v0.2

## 核心理念

Figma 设计稿 → 可直接使用的移动端 UI 代码。
用户复制到项目里就能看效果，不需要额外配置资源文件。

## 设计原则

1. **输出即可用** — 颜色写死 hex，文本写死字符串，不引用资源 ID
2. **交互式确认** — 不确定的结构主动提问，给选项+优劣说明，简洁不啰嗦
3. **不猜业务逻辑** — 列表/Adapter/自定义组件等，问用户而不是假设
4. **先 Skill 后 MCP** — 在 OpenClaw Skill 里验证流程，跑通后再适配 MCP Server
5. **分层输出** — 主布局一个文件，列表 item 单独一个文件，不生成 Adapter

## 工作流程（三步走）

### Step 1: 扫描 + 分析

输入：用户提供 Figma 链接
动作：调用 figma_fetch.py 拉取数据，AI 分析结构
输出：简要结构摘要 + 需要确认的问题

示例交互：
```
AI: 这个页面我分析出以下结构：
📱 通知设置页 (375x812)
├── 导航栏：返回按钮 + 标题
├── 专家通知：标题 + 3个相似卡片（头像+文字+开关）
└── 系统通知：标题 + 1个卡片（图标+文字+开关）

有几个问题：
1. 专家通知的3个卡片结构相似，是动态列表还是固定项？
   → 动态列表：输出 RecyclerView + item 布局
   → 固定项：直接写死在主布局
2. 输出格式？Android XML / Compose / SwiftUI / UIKit
```

### Step 2: 用户确认

用户回答问题，补充信息。
可能补充的内容：
- 动态/静态
- 输出格式
- 特殊组件名（如自定义 Switch）
- 其他需求

### Step 3: 生成代码

根据确认结果生成：
- 主布局文件（完整可用的 XML/Compose/SwiftUI/UIKit）
- item 布局文件（如果有列表）
- 不生成 Adapter、颜色资源、字符串资源

## 输出规范

### Android XML
- 颜色直接写 hex：android:textColor="#0F0F0F"
- 文本直接写中文：android:text="通知设置"
- 尺寸直接写 dp/sp：android:textSize="17sp"
- 优先使用 ConstraintLayout（复杂布局）或 LinearLayout（简单线性）
- 图片统一用 placeholder：android:src="@drawable/placeholder"

### Jetpack Compose
- 颜色用 Color(0xFF0F0F0F)
- 文本直接写字符串
- 尺寸用 .dp / .sp

### SwiftUI
- 颜色用 Color(hex:) 扩展
- 文本直接写字符串
- 尺寸用 CGFloat

### UIKit
- 颜色用 UIColor(hex:) 扩展
- 文本直接写字符串

## 交互设计原则

1. 问题不超过 3-5 个，每个问题给明确选项
2. 每个选项说一句话解释优劣
3. 不输出 JSON/技术细节，用自然语言
4. 如果所有结构都很明确（高 confidence），可以跳过交互直接生成

## 后续演进

### Phase 2: project_scan
- 扫描项目已有的颜色定义、自定义组件、布局习惯
- 生成时自动匹配已有资源
- 存储项目配置到 .figma-to-mobile.json

### Phase 3: MCP Server
- 将 Skill 逻辑封装为 MCP Server
- 支持 VS Code / Cursor / Claude Code
- npm 发布，npx 一键启动

### Phase 4: Adapter 生成（可选）
- 扫描项目已有 Adapter 封装模式
- 按用户的封装习惯生成 Adapter
- 需要用户确认后才生成
