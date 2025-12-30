# GitHub 项目完善操作指南

由于网络问题，部分操作需要手动完成。以下是详细步骤：

## ✅ 已完成的任务

1. ✅ 代码已推送到 GitHub
2. ✅ README 已添加更多徽章
3. ✅ Git tag v1.0.0 已创建（本地）

## 🔧 需要手动完成的任务

### 任务 1：推送 Git Tag

由于网络问题，tag还没有推送到GitHub。请执行：

```bash
cd ~/.claude/skills/md2word
git push origin v1.0.0
```

或者推送所有tag：
```bash
git push --tags
```

### 任务 2：在 GitHub 添加 Topics 和 About

1. 访问：https://github.com/liyajun2alan/md2word
2. 点击右上角的 ⚙️ (Settings图标，在About旁边)
3. 添加以下信息：

**Description (描述)**:
```
Convert Markdown to Word documents with template formatting
```

**Website (可选)**:
```
https://github.com/liyajun2alan/md2word
```

**Topics (标签)**:
添加以下标签（每输入一个按回车）：
- `markdown`
- `word`
- `docx`
- `converter`
- `python`
- `document`
- `template`
- `python-docx`
- `mistune`

### 任务 3：创建 Release

#### 方式一：通过 GitHub 网页（推荐）

1. 访问：https://github.com/liyajun2alan/md2word/releases
2. 点击 "Create a new release" 或 "Draft a new release"
3. 填写以下信息：

**Choose a tag**:
- 如果 v1.0.0 已经推送成功，从下拉列表选择 `v1.0.0`
- 如果没有，输入 `v1.0.0` 并选择 "Create new tag: v1.0.0 on publish"

**Release title**:
```
v1.0.0 - Initial Release
```

**Describe this release**:
复制并粘贴 `RELEASE_NOTES_v1.0.0.md` 的内容（文件路径：~/.claude/skills/md2word/RELEASE_NOTES_v1.0.0.md）

或者使用以下简化版本：

```markdown
🎉 **md2word 首次发布！**

## ✨ 主要功能
- 📝 Markdown 转 Word 文档
- 🎨 模板样式继承
- 🔢 多级标题自动编号
- 📊 表格格式转换
- 📑 列表支持（有序/无序）
- 🖼️ 支持图片、代码块、引用

## 🐛 Bug修复
- 修复列表项重复生成bug
- 修复表格样式不匹配问题
- 修复单元格首行缩进问题
- 修复空项目符号段落问题

## 📦 安装
\`\`\`bash
git clone https://github.com/liyajun2alan/md2word.git
cd md2word
pip install -r requirements.txt
\`\`\`

## 🚀 快速开始
\`\`\`bash
./md2word input.md output.docx template.docx
\`\`\`

完整文档：https://github.com/liyajun2alan/md2word
```

**Set as the latest release**: ✅ 勾选

**Create a discussion for this release**: 可选

4. 点击 "Publish release"

#### 方式二：通过 GitHub CLI（需要先安装）

```bash
# 安装 GitHub CLI
brew install gh

# 登录
gh auth login

# 创建 release
cd ~/.claude/skills/md2word
gh release create v1.0.0 \
  --title "v1.0.0 - Initial Release" \
  --notes-file RELEASE_NOTES_v1.0.0.md \
  --latest
```

### 任务 4：设置仓库可见性（如果需要）

如果您想将仓库设为公开或私有：

1. 访问：https://github.com/liyajun2alan/md2word/settings
2. 滚动到最底部的 "Danger Zone"
3. 根据需要选择：
   - **Change repository visibility** → Public (公开，推荐)
   - 或 Private (私有)

### 任务 5：添加仓库描述和链接

在仓库首页右侧的 About 部分：
1. 点击 ⚙️ 图标
2. 填写：
   - **Description**: `Convert Markdown to Word documents with template formatting`
   - **Website**: 留空或填写文档链接
   - **Topics**: `markdown`, `word`, `docx`, `converter`, `python`
3. 保存

### 任务 6：验证徽章是否正常显示

访问 https://github.com/liyajun2alan/md2word

检查 README 顶部的徽章是否正常显示：
- ✅ Python Version
- ✅ License
- ✅ GitHub release (创建 release 后会显示)
- ✅ GitHub stars
- ✅ GitHub issues
- ✅ GitHub last commit

## 📋 完成检查清单

- [ ] Tag v1.0.0 已推送到 GitHub
- [ ] Topics 已添加 (markdown, word, docx, converter, python)
- [ ] About 描述已设置
- [ ] Release v1.0.0 已创建
- [ ] README 徽章正常显示
- [ ] 仓库可见性已设置

## 🎉 完成后

您的项目将拥有：
- ✨ 专业的 README 文档（带徽章）
- 📦 正式的 Release 版本
- 🏷️ 清晰的 Topics 标签
- 📖 完整的文档和更新日志
- ⭐ 可以被其他开发者 star 和 fork

## ❓ 遇到问题？

### 推送 tag 失败
```bash
# 删除本地 tag
git tag -d v1.0.0

# 重新创建并推送
git tag -a v1.0.0 -m "Version 1.0.0"
git push origin v1.0.0
```

### 需要重新生成 token
如果之前的 token 过期或删除：
1. 访问：https://github.com/settings/tokens
2. Generate new token (classic)
3. 勾选 `repo` 权限
4. 更新远程URL：
```bash
cd ~/.claude/skills/md2word
git remote set-url origin https://YOUR_NEW_TOKEN@github.com/liyajun2alan/md2word.git
```

---

**项目地址**: https://github.com/liyajun2alan/md2word

祝您的开源项目越来越好！🚀
