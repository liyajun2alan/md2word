# 在 Claude Code 中使用 md2word

这是一个专为 Claude Code 优化的 Markdown 转 Word 工具，支持通过自然语言进行操作。

## 快速安装

### 方式一：一键安装（推荐）

```bash
curl -fsSL https://raw.githubusercontent.com/liyajun2alan/md2word/main/install.sh | bash
```

### 方式二：手动安装

```bash
# 克隆到 Claude Skills 目录
git clone https://github.com/liyajun2alan/md2word.git ~/.claude/skills/md2word

# 进入目录
cd ~/.claude/skills/md2word

# 安装依赖
pip install -r requirements.txt

# 添加执行权限
chmod +x md2word
```

## 在 Claude Code 中使用

安装后，md2word 会自动注册为 Claude Code skill，您可以通过以下方式使用：

### 🗣️ 自然语言触发

md2word 支持多种自然语言表达，Claude Code 会自动识别并调用：

```
"帮我把这个 Markdown 转换为 Word"
"导出 README.md 为 Word 文档"
"将技术方案.md 转换成 docx"
"生成 Word 版本的文档"
"把 input.md 转成 Word，使用 template.docx 模板"
```

### 💻 命令触发

如果您更喜欢精确控制，可以使用命令格式：

```
/md2word input.md output.docx
/md2word input.md output.docx template.docx
```

### 📝 使用示例

#### 示例 1：基本转换
```
用户: "帮我把 README.md 转换为 Word 文档"

Claude: 我来帮您将 README.md 转换为 Word 文档。
[调用 md2word skill]
✅ 已生成 README.docx
```

#### 示例 2：使用模板
```
用户: "把技术方案.md 转成 Word，使用公司模板.docx 的格式"

Claude: 我将使用公司模板.docx 的格式来转换技术方案.md。
[调用 md2word skill，应用模板样式]
✅ 已生成 技术方案.docx（应用了模板样式）
```

#### 示例 3：批量处理
```
用户: "把 docs 文件夹下所有 md 文件都转成 Word"

Claude: 我来扫描 docs 文件夹并批量转换...
[循环调用 md2word skill]
✅ 已转换 5 个文件
```

## Skill 配置

md2word 的 skill.yml 配置如下：

```yaml
name: md2word
description: "将Markdown文件按照Word模板格式转换为Word文档"
command: /md2word
handler: md2word
enabled: true

triggers:
  - "转换为word"
  - "导出word"
  - "生成word"
  - "md转word"
  - "markdown转word"
  - "/md2word"

parameters:
  - name: md_file
    type: string
    description: "Markdown文件路径"
    required: true

  - name: word_file
    type: string
    description: "目标Word文件路径"
    required: true

  - name: template_file
    type: string
    description: "Word模板文件路径（可选）"
    required: false

permissions:
  - "Bash(python3:*)"
  - "Read(*.md)"
  - "Read(*.docx)"
  - "Write(*.docx)"
```

## 功能特性

### ✨ Claude Code 集成优势

1. **自然语言理解**
   - 无需记忆命令语法
   - Claude 自动识别转换意图
   - 支持上下文理解（"再转换另一个"、"用同样的模板"）

2. **智能路径处理**
   - 自动补全相对路径
   - 智能推测输出文件名
   - 处理中文路径和特殊字符

3. **批量操作支持**
   - 一次转换多个文件
   - 文件夹递归处理
   - 自动跳过非 Markdown 文件

4. **错误处理友好**
   - Claude 用自然语言解释错误
   - 提供解决方案建议
   - 自动重试机制

### 🎨 转换功能

- ✅ 标题层级（H1-H6）
- ✅ 段落和换行
- ✅ 列表（有序/无序/嵌套）
- ✅ 表格（边框/对齐/单元格样式）
- ✅ 代码块（语法高亮保留）
- ✅ 引用块
- ✅ 粗体/斜体/行内代码
- ✅ 图片（自动嵌入）
- ✅ 链接（转换为超链接）

### 🔧 模板功能

- 样式继承（字体/颜色/间距）
- 自动编号（多级标题编号）
- 表格格式（边框/单元格边距）
- 页眉页脚保留
- 自定义样式应用

## 常见场景

### 场景 1：技术文档转换
```
用户: "帮我把这份技术方案转成 Word，要用标准模板"

Claude: 好的，我会用标准模板转换技术方案。
[自动使用 references/default_template.docx]
✅ 已生成格式规范的 Word 文档
```

### 场景 2：会议记录整理
```
用户: "把今天的会议记录.md 整理成 Word，发给领导"

Claude: 我来转换会议记录为 Word 格式。
[转换并优化格式]
✅ 已生成 会议记录.docx，格式整洁专业
```

### 场景 3：文档标准化
```
用户: "我有 10 个不同格式的 md 文件，统一转成公司标准格式的 Word"

Claude: 好的，我将使用公司模板批量转换这些文件。
[批量处理，应用统一模板]
✅ 已转换 10 个文件，格式统一
```

## 高级用法

### 自定义触发词

编辑 `~/.claude/skills/md2word/skill.yml`，添加您习惯的触发词：

```yaml
triggers:
  - "转换为word"
  - "导出word"
  - "生成word"
  - "md转word"
  - "markdown转word"
  - "/md2word"
  - "转docx"          # 自定义
  - "生成文档"         # 自定义
  - "导出文档"         # 自定义
```

### 设置默认模板

将您的常用模板命名为 `default_template.docx` 并放在：
```
~/.claude/skills/md2word/references/default_template.docx
```

这样即使不指定模板，也会自动使用您的默认模板。

### 与其他 Skills 配合

md2word 可以与其他 Claude Skills 配合使用：

```
用户: "先帮我用 mermaid 生成流程图，然后把文档转成 Word"

Claude:
1. [调用 mermaid skill] 生成流程图
2. [将图片插入到 Markdown]
3. [调用 md2word skill] 转换为 Word
✅ 已生成包含流程图的 Word 文档
```

## 故障排查

### 问题 1：Claude 没有识别转换命令

**原因**: skill.yml 可能未生效

**解决方案**:
```bash
# 重启 Claude Code
# 或检查 skill.yml 是否在正确位置
ls ~/.claude/skills/md2word/skill.yml
```

### 问题 2：转换失败提示缺少依赖

**原因**: Python 依赖未安装

**解决方案**:
```bash
cd ~/.claude/skills/md2word
pip install -r requirements.txt
```

### 问题 3：生成的 Word 样式不对

**原因**: 模板格式未正确提取

**解决方案**:
- 确保模板文档中至少有一个表格作为样式参考
- 检查模板中是否包含 Heading 1-6 样式
- 使用 `references/default_template.docx` 作为参考

### 问题 4：中文路径无法识别

**原因**: 路径包含空格或特殊字符

**解决方案**:
```
使用引号包裹路径：
'/md2word "技术 方案.md" "输出 文档.docx"'
```

## 权限说明

md2word skill 需要以下权限：

- `Bash(python3:*)`: 执行 Python 脚本
- `Read(*.md)`: 读取 Markdown 文件
- `Read(*.docx)`: 读取 Word 模板
- `Write(*.docx)`: 写入生成的 Word 文件

这些权限已在 skill.yml 中预配置，Claude Code 会在首次使用时请求授权。

## 更新 Skill

```bash
cd ~/.claude/skills/md2word
git pull origin main
pip install -r requirements.txt --upgrade
```

或使用一键安装脚本重新安装：
```bash
curl -fsSL https://raw.githubusercontent.com/liyajun2alan/md2word/main/install.sh | bash
```

## 卸载 Skill

```bash
rm -rf ~/.claude/skills/md2word
```

## 获取帮助

- 📚 完整文档: https://github.com/liyajun2alan/md2word
- 🐛 报告问题: https://github.com/liyajun2alan/md2word/issues
- 💬 讨论区: https://github.com/liyajun2alan/md2word/discussions

## 贡献

欢迎为 md2word 贡献代码或提出改进建议！

```bash
# Fork 仓库
# 创建特性分支
git checkout -b feature/my-feature

# 提交更改
git commit -am 'Add some feature'

# 推送到分支
git push origin feature/my-feature

# 创建 Pull Request
```

---

**作者**: 李亚军 ([@liyajun2alan](https://github.com/liyajun2alan))
**许可证**: MIT
**版本**: 1.0.0
