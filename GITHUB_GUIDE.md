# GitHub 发布指南

## 准备工作已完成 ✅

已为您完成以下准备工作：

1. ✅ 创建了 README.md（项目说明文档）
2. ✅ 创建了 LICENSE（MIT许可证）
3. ✅ 创建了 .gitignore（Git忽略文件）
4. ✅ 创建了 setup.py（Python包配置）
5. ✅ 创建了 CHANGELOG.md（更新日志）
6. ✅ 初始化了 Git 仓库
7. ✅ 完成了首次提交

## 接下来的步骤

### 1. 配置 Git 用户信息（如果还没配置）

```bash
# 设置全局用户名和邮箱
git config --global user.name "您的名字"
git config --global user.email "your.email@example.com"

# 或者只为这个项目设置
cd ~/.claude/skills/md2word
git config user.name "您的名字"
git config user.email "your.email@example.com"
```

### 2. 在 GitHub 上创建新仓库

1. 访问 https://github.com/new
2. 填写仓库信息：
   - **Repository name**: `md2word`
   - **Description**: `Convert Markdown to Word documents with template formatting`
   - **Public** 或 **Private**（根据需要选择）
   - ⚠️ **不要**勾选 "Add a README file"（我们已经有了）
   - ⚠️ **不要**勾选 "Add .gitignore"（我们已经有了）
   - ⚠️ **不要**勾选 "Choose a license"（我们已经有了）
3. 点击 "Create repository"

### 3. 推送到 GitHub

创建仓库后，GitHub会显示推送命令，使用以下命令：

```bash
cd ~/.claude/skills/md2word

# 添加远程仓库（替换 YOUR_USERNAME 为您的GitHub用户名）
git remote add origin https://github.com/YOUR_USERNAME/md2word.git

# 推送到 GitHub
git branch -M main
git push -u origin main
```

### 4. 更新项目文件中的链接（可选）

创建仓库后，更新以下文件中的链接：

#### README.md
```bash
# 将所有 "你的用户名" 替换为实际的GitHub用户名
# 例如：将 https://github.com/你的用户名/md2word
#      替换为 https://github.com/yourusername/md2word
```

#### setup.py
```python
# 更新以下字段：
author="Your Name",  # 您的名字
author_email="your.email@example.com",  # 您的邮箱
url="https://github.com/yourusername/md2word",  # 仓库URL
```

更新后重新提交：
```bash
cd ~/.claude/skills/md2word
git add README.md setup.py
git commit -m "Update project URLs and author info"
git push
```

### 5. 创建 Release（推荐）

在 GitHub 仓库页面：
1. 点击右侧的 "Releases"
2. 点击 "Create a new release"
3. 填写信息：
   - **Tag version**: `v1.0.0`
   - **Release title**: `v1.0.0 - Initial Release`
   - **Description**: 复制 CHANGELOG.md 中的 v1.0.0 内容
4. 点击 "Publish release"

### 6. 添加徽章到 README（可选）

在仓库设置中启用以下功能后，可以添加更多徽章：
- GitHub Stars
- GitHub Issues
- GitHub Last Commit
- Download Count

## 常用 Git 命令

```bash
# 查看状态
git status

# 添加文件
git add .

# 提交更改
git commit -m "描述信息"

# 推送到远程
git push

# 拉取更新
git pull

# 查看提交历史
git log --oneline

# 创建标签
git tag -a v1.0.0 -m "Version 1.0.0"
git push --tags
```

## 维护建议

### 定期更新

1. 修复bug或添加新功能后：
   ```bash
   git add .
   git commit -m "描述更改"
   git push
   ```

2. 更新版本号：
   - 修改 `setup.py` 中的 `version`
   - 更新 `CHANGELOG.md`
   - 创建新的 Git tag

### 处理 Issues

- 在 GitHub Issues 中及时回复用户问题
- 使用 Labels 分类问题
- 关闭已解决的 Issues

### 接受贡献

- 审查 Pull Requests
- 提供建设性的反馈
- 合并优质的贡献

## 故障排查

### 推送失败

如果推送时遇到认证问题：

1. **使用 Personal Access Token**：
   ```bash
   # 在 GitHub Settings > Developer settings > Personal access tokens 创建 token
   # 推送时使用 token 作为密码
   git push https://YOUR_TOKEN@github.com/YOUR_USERNAME/md2word.git
   ```

2. **配置 SSH**：
   ```bash
   # 生成 SSH key
   ssh-keygen -t ed25519 -C "your.email@example.com"

   # 添加到 ssh-agent
   eval "$(ssh-agent -s)"
   ssh-add ~/.ssh/id_ed25519

   # 将公钥添加到 GitHub Settings > SSH and GPG keys
   cat ~/.ssh/id_ed25519.pub

   # 使用 SSH URL
   git remote set-url origin git@github.com:YOUR_USERNAME/md2word.git
   ```

### 文件过大

如果某些文件过大无法推送：
```bash
# 从历史记录中删除大文件
git filter-branch --tree-filter 'rm -f path/to/large/file' HEAD
git push -f origin main
```

## 完成！

恭喜！🎉 您的项目现在已经发布到 GitHub 上了。

访问 https://github.com/YOUR_USERNAME/md2word 查看您的项目。
