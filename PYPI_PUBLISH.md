# 发布 md2word 到 PyPI

将 md2word 发布到 PyPI 后，用户可以直接使用 `pip install md2word` 安装。

## 准备工作

### 1. 安装发布工具

```bash
pip install --upgrade pip setuptools wheel twine
```

### 2. 注册 PyPI 账号

- 访问：https://pypi.org/account/register/
- 完成邮箱验证
- 启用两步验证（推荐）

### 3. 创建 API Token

1. 访问：https://pypi.org/manage/account/token/
2. 点击 "Add API token"
3. Token name: `md2word-upload`
4. Scope: `Entire account (all projects)` 或指定 `md2word` 项目
5. 复制生成的 token（格式：`pypi-xxx...`）

## 发布步骤

### 1. 确保代码已提交

```bash
cd ~/.claude/skills/md2word
git status  # 确保没有未提交的更改
```

### 2. 构建分发包

```bash
# 清理旧的构建文件
rm -rf build/ dist/ *.egg-info

# 构建源码包和 wheel 包
python3 setup.py sdist bdist_wheel
```

这会生成：
- `dist/md2word-1.0.0.tar.gz` - 源码包
- `dist/md2word-1.0.0-py3-none-any.whl` - wheel 包

### 3. 检查构建结果

```bash
# 检查包的完整性
twine check dist/*
```

应该显示：
```
Checking dist/md2word-1.0.0.tar.gz: PASSED
Checking dist/md2word-1.0.0-py3-none-any.whl: PASSED
```

### 4. 上传到 PyPI

#### 方式一：使用 API Token

```bash
# 配置 token（只需一次）
# 创建 ~/.pypirc 文件
cat > ~/.pypirc << 'EOF'
[pypi]
  username = __token__
  password = pypi-YOUR_TOKEN_HERE
EOF

chmod 600 ~/.pypirc

# 上传
twine upload dist/*
```

#### 方式二：交互式上传

```bash
twine upload dist/*
# 输入 username: __token__
# 输入 password: pypi-YOUR_TOKEN_HERE
```

### 5. 验证发布

```bash
# 等待 1-2 分钟，然后测试安装
pip install md2word

# 测试命令
md2word --help
```

访问：https://pypi.org/project/md2word/

## 测试发布（推荐先测试）

使用 TestPyPI 进行测试：

### 1. 注册 TestPyPI

- 访问：https://test.pypi.org/account/register/
- 创建 API token

### 2. 上传到 TestPyPI

```bash
# 上传到测试服务器
twine upload --repository testpypi dist/*

# 或配置 ~/.pypirc
cat >> ~/.pypirc << 'EOF'

[testpypi]
  username = __token__
  password = pypi-YOUR_TESTPYPI_TOKEN_HERE
EOF

twine upload --repository testpypi dist/*
```

### 3. 从 TestPyPI 测试安装

```bash
pip install --index-url https://test.pypi.org/simple/ md2word
```

## 更新版本

每次发布新版本时：

### 1. 更新版本号

编辑 `setup.py`：
```python
setup(
    name="md2word",
    version="1.0.1",  # 修改这里
    ...
)
```

版本号规范（语义化版本）：
- **主版本号（Major）**: 不兼容的 API 修改
- **次版本号（Minor）**: 向下兼容的功能性新增
- **修订号（Patch）**: 向下兼容的问题修正

例如：
- Bug 修复：1.0.0 → 1.0.1
- 新功能（兼容）：1.0.1 → 1.1.0
- 重大更改（不兼容）：1.1.0 → 2.0.0

### 2. 更新 CHANGELOG.md

在 CHANGELOG.md 中添加新版本的更新说明。

### 3. 提交并打标签

```bash
git add setup.py CHANGELOG.md
git commit -m "Bump version to 1.0.1"
git tag -a v1.0.1 -m "Version 1.0.1"
git push origin main --tags
```

### 4. 重新构建并上传

```bash
rm -rf build/ dist/ *.egg-info
python3 setup.py sdist bdist_wheel
twine check dist/*
twine upload dist/*
```

## 自动化发布（GitHub Actions）

创建 `.github/workflows/publish.yml`：

```yaml
name: Publish to PyPI

on:
  release:
    types: [created]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.11'

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install setuptools wheel twine

    - name: Build package
      run: python setup.py sdist bdist_wheel

    - name: Publish to PyPI
      env:
        TWINE_USERNAME: __token__
        TWINE_PASSWORD: ${{ secrets.PYPI_API_TOKEN }}
      run: twine upload dist/*
```

设置 GitHub Secret：
1. 访问：https://github.com/liyajun2alan/md2word/settings/secrets/actions
2. 添加 secret：`PYPI_API_TOKEN`，值为 PyPI token

之后每次创建 GitHub Release 时自动发布到 PyPI。

## 发布后的 README 更新

发布到 PyPI 后，更新 README.md 的安装部分：

```markdown
## 安装

### 使用 pip 安装（推荐）

\`\`\`bash
pip install md2word
\`\`\`

### 从源码安装

\`\`\`bash
git clone https://github.com/liyajun2alan/md2word.git
cd md2word
pip install -e .
\`\`\`
```

添加 PyPI 徽章到 README：
```markdown
[![PyPI version](https://img.shields.io/pypi/v/md2word.svg)](https://pypi.org/project/md2word/)
[![PyPI downloads](https://img.shields.io/pypi/dm/md2word.svg)](https://pypi.org/project/md2word/)
[![Python versions](https://img.shields.io/pypi/pyversions/md2word.svg)](https://pypi.org/project/md2word/)
```

## 管理发布

### 查看发布信息

```bash
# 查看包信息
pip show md2word

# 查看所有版本
pip index versions md2word
```

### 删除版本（谨慎操作）

PyPI 不允许删除已发布的版本，但可以 "yank"（标记为不推荐）：

1. 访问：https://pypi.org/manage/project/md2word/releases/
2. 选择版本
3. 点击 "Options" > "Yank"

### 转移所有权

如果需要添加其他维护者：
1. 访问：https://pypi.org/manage/project/md2word/collaboration/
2. 添加用户为 Maintainer 或 Owner

## 常见问题

### Q: 包名已被占用怎么办？

A: 可以使用其他名称，如：
- `markdown-to-word`
- `md2docx`
- `mdword`

修改 setup.py 中的 `name` 字段。

### Q: 上传失败：403 Forbidden

A: 检查：
1. API token 是否正确
2. 包名是否已存在且您无权限
3. 版本号是否已存在

### Q: 如何测试包的安装？

A: 使用虚拟环境测试：
```bash
python3 -m venv test_env
source test_env/bin/activate
pip install md2word
md2word --help
deactivate
rm -rf test_env
```

### Q: 如何包含数据文件？

A: 已在 setup.py 中配置：
```python
package_data={
    "": ["references/*.docx"],
},
include_package_data=True,
```

确保 MANIFEST.in 包含：
```
include references/*.docx
```

## 检查清单

发布前检查：

- [ ] 版本号已更新（setup.py）
- [ ] CHANGELOG.md 已更新
- [ ] README.md 准确无误
- [ ] 所有测试通过
- [ ] 代码已提交并推送到 GitHub
- [ ] Git tag 已创建
- [ ] 清理了 build/dist 目录
- [ ] twine check 通过
- [ ] 在 TestPyPI 测试成功（首次发布）

## 资源链接

- **PyPI 官网**: https://pypi.org/
- **PyPI 文档**: https://packaging.python.org/
- **Twine 文档**: https://twine.readthedocs.io/
- **语义化版本**: https://semver.org/

---

**提示**: 首次发布建议先在 TestPyPI 测试，确认无误后再正式发布到 PyPI。
