# v1.0.0 - Initial Release

🎉 **md2word 首次发布！**

这是一个将 Markdown 文件转换为 Word 文档的工具，支持保留模板样式、自动编号、表格格式等功能。

## ✨ 主要功能

### 核心特性
- 📝 **Markdown 转 Word**：完整支持标准 Markdown 语法
- 🎨 **模板样式继承**：从 Word 模板中提取并应用样式
- 🔢 **自动编号**：支持多级标题自动编号
- 📊 **表格支持**：完整的表格格式转换和样式继承
- 📑 **列表处理**：支持有序/无序列表
- 🖼️ **富文本元素**：支持图片、代码块、引用等

### 新增功能
- ✨ 支持 Markdown 转 Word 文档功能
- 📝 支持模板样式继承
- 🔢 支持多级标题自动编号
- 📊 支持表格格式转换
- 📑 支持有序/无序列表
- 🖼️ 支持图片、代码块、引用等元素
- 🎨 支持自定义 Word 模板

## 🐛 Bug修复

- 修复列表项重复生成的bug（当Word模板缺少List Number/List Bullet样式时）
- 修复表格样式不匹配问题
- 修复表格单元格首行缩进问题
- 修复空项目符号段落问题

## ⚡ 性能优化

- 优化表格列宽自动调整（autofit）
- 优化表格单元格边距应用（默认左右5.4pt）
- 优化表格对齐方式（标题居中，数据左对齐）
- 改进模板格式提取逻辑

## 📦 安装

```bash
# 克隆仓库
git clone https://github.com/liyajun2alan/md2word.git
cd md2word

# 安装依赖
pip install -r requirements.txt

# 添加执行权限
chmod +x md2word
```

## 🚀 快速开始

```bash
# 基本用法
./md2word input.md output.docx

# 使用自定义模板
./md2word input.md output.docx template.docx
```

## 🛠️ 技术栈

- **Python**: 3.8+
- **python-docx**: Word 文档处理
- **mistune 3.x**: Markdown 解析

## 📊 项目统计

- 15 个文件
- 1800+ 行代码
- MIT 许可证
- 支持 Python 3.8+

## 🙏 致谢

- [python-docx](https://python-docx.readthedocs.io/) - Word 文档处理库
- [mistune](https://mistune.lepture.com/) - Markdown 解析库

## 📝 更新日志

完整的更新日志请查看 [CHANGELOG.md](https://github.com/liyajun2alan/md2word/blob/main/CHANGELOG.md)

---

**完整文档**: https://github.com/liyajun2alan/md2word
**问题反馈**: https://github.com/liyajun2alan/md2word/issues

感谢使用 md2word！如果觉得有用，请给个 ⭐️
