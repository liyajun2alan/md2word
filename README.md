# md2word

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![GitHub release](https://img.shields.io/github/v/release/liyajun2alan/md2word)](https://github.com/liyajun2alan/md2word/releases)
[![GitHub stars](https://img.shields.io/github/stars/liyajun2alan/md2word?style=social)](https://github.com/liyajun2alan/md2word)
[![GitHub issues](https://img.shields.io/github/issues/liyajun2alan/md2word)](https://github.com/liyajun2alan/md2word/issues)
[![GitHub last commit](https://img.shields.io/github/last-commit/liyajun2alan/md2word)](https://github.com/liyajun2alan/md2word/commits/main)

将 Markdown 文件按照 Word 模板格式转换为 Word 文档的工具。支持保留模板样式、自动编号、表格格式等功能。

## 功能特点

✨ **核心功能**
- 📝 将 Markdown 转换为 Word 文档（.docx）
- 🎨 保留 Word 模板的样式和格式
- 🔢 自动编号（支持多级标题编号）
- 📊 表格格式继承（边框、对齐、单元格边距等）
- 🖼️ 支持图片、代码块、引用等元素
- 📑 支持列表（有序/无序）

✅ **最新修复**
- 修复列表项重复生成的bug
- 修复表格样式不匹配问题
- 优化单元格对齐和缩进
- 过滤空项目符号段落

## 安装

### 依赖要求

- Python 3.8+
- python-docx
- mistune 3.x

### 安装步骤

```bash
# 克隆仓库
git clone https://github.com/你的用户名/md2word.git
cd md2word

# 安装依赖
pip install -r requirements.txt

# 添加执行权限
chmod +x md2word
```

## 使用方法

### 基本用法

```bash
# 使用默认模板转换
./md2word input.md output.docx

# 使用自定义模板转换
./md2word input.md output.docx template.docx
```

### 示例

```bash
# 转换技术文档
./md2word 技术方案.md 技术方案.docx 模板.docx

# 转换到当前目录
./md2word README.md README.docx
```

## 配置说明

### 模板格式

工具会从模板文档中提取以下格式：
- 标题样式（Heading 1-6）
- 正文样式
- 列表样式
- 表格样式（边框、对齐、单元格边距）
- 代码块样式
- 引用块样式

### 支持的 Markdown 语法

- 标题（# ~ ######）
- 段落
- 列表（有序/无序）
- 表格
- 代码块（```）
- 引用块（>）
- 图片（![alt](url)）
- 粗体、斜体、行内代码

## 项目结构

```
md2word/
├── md2word              # 主执行脚本
├── scripts/             # Python 脚本
│   ├── main.py         # 主程序入口
│   ├── markdown_parser.py    # Markdown 解析器
│   ├── template_parser.py    # 模板解析器
│   ├── word_generator.py     # Word 生成器
│   └── utils.py        # 工具函数
├── references/          # 参考文件
│   └── default_template.docx # 默认模板
├── requirements.txt     # Python 依赖
├── README.md           # 项目说明
└── LICENSE             # 开源许可证
```

## 技术细节

### 架构设计

1. **Markdown 解析层**：使用 mistune 3.x 解析 Markdown 文档
2. **模板解析层**：提取 Word 模板的样式和格式
3. **文档生成层**：使用 python-docx 生成 Word 文档并应用样式

### 核心特性

- **自动编号**：从模板中提取多级编号配置并自动应用
- **表格处理**：
  - 自动调整列宽（autofit）
  - 继承模板的单元格边距（默认左右5.4pt）
  - 标题行居中对齐并加粗
  - 数据行左对齐
- **列表处理**：
  - 优先使用 Word 内置列表样式
  - 降级方案：手动添加项目符号
  - 自动过滤空项目符号
- **样式继承**：完整继承模板的字体、颜色、间距等格式

## 常见问题

### Q: 为什么生成的文档有重复内容？
A: 这是旧版本的bug，已在最新版本中修复。请更新到最新版本。

### Q: 表格样式不匹配怎么办？
A: 确保模板文档中至少有一个表格作为样式参考。工具会自动提取第一个表格的格式。

### Q: 支持哪些 Markdown 扩展语法？
A: 目前支持标准 Markdown 语法和表格（GFM）。不支持脚注、高亮等扩展语法。

### Q: 如何自定义样式？
A: 创建一个 Word 模板文档，设置好标题、正文、表格等样式，然后使用该模板进行转换。

## 开发计划

- [ ] 支持更多 Markdown 扩展语法
- [ ] 支持图片尺寸自动调整
- [ ] 支持更复杂的表格（合并单元格）
- [ ] 提供 Web 界面
- [ ] 支持批量转换

## 贡献指南

欢迎贡献代码、报告问题或提出建议！

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 创建 Pull Request

## 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件

## 致谢

- [python-docx](https://python-docx.readthedocs.io/) - Word 文档处理
- [mistune](https://mistune.lepture.com/) - Markdown 解析

## 作者

李亚军 - [@liyajun2alan](https://github.com/liyajun2alan)

## 更新日志

### v1.0.0 (2024-12-30)
- 🎉 初始发布
- ✅ 支持基本 Markdown 转 Word 功能
- ✅ 支持模板样式继承
- ✅ 修复列表重复bug
- ✅ 优化表格格式处理
