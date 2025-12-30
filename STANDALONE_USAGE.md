# md2word 独立使用指南

md2word 是一个完全独立的 Python 工具，可以在**任何环境**中使用，无需依赖 Claude Code。

## 安装方式

### 方式一：使用 pip（最简单，推荐）

```bash
# 从 GitHub 安装最新版本
pip install git+https://github.com/liyajun2alan/md2word.git

# 安装到用户目录（不需要 sudo）
pip install --user git+https://github.com/liyajun2alan/md2word.git

# 安装指定版本
pip install git+https://github.com/liyajun2alan/md2word.git@v1.0.0

# 开发模式安装（可编辑源码）
git clone https://github.com/liyajun2alan/md2word.git
cd md2word
pip install -e .
```

安装后可在系统任意位置使用 `md2word` 命令：

```bash
cd ~/Documents
md2word report.md report.docx

cd ~/Projects
md2word README.md README.docx template.docx
```

### 方式二：从 GitHub 克隆

```bash
# 克隆到任意目录
git clone https://github.com/liyajun2alan/md2word.git
cd md2word

# 安装 Python 依赖
pip install -r requirements.txt

# 添加执行权限（macOS/Linux）
chmod +x md2word
```

### 方式三：下载压缩包

```bash
# 下载最新版本
wget https://github.com/liyajun2alan/md2word/archive/refs/tags/v1.0.0.tar.gz

# 解压
tar -xzf v1.0.0.tar.gz
cd md2word-1.0.0

# 安装依赖
pip install -r requirements.txt
```

## 使用方式

### 1️⃣ 命令行直接使用

#### 基本语法

```bash
./md2word <输入md文件> <输出docx文件> [可选:模板docx文件]
```

#### 示例

```bash
# 使用默认模板转换
./md2word README.md README.docx

# 使用自定义模板
./md2word 技术方案.md 输出.docx 公司模板.docx

# 使用绝对路径
./md2word /path/to/input.md /path/to/output.docx

# 使用相对路径
./md2word ../docs/report.md ./output/report.docx
```

#### Windows 系统使用

```cmd
python scripts\main.py input.md output.docx
python scripts\main.py input.md output.docx template.docx
```

### 2️⃣ 作为 Python 模块使用

#### 在您的 Python 脚本中导入

```python
import sys
sys.path.append('/path/to/md2word')

from scripts.main import convert_markdown_to_word

# 基本转换
convert_markdown_to_word(
    md_file='input.md',
    word_file='output.docx'
)

# 使用模板
convert_markdown_to_word(
    md_file='input.md',
    word_file='output.docx',
    template_file='template.docx'
)
```

#### 批量转换示例

```python
import os
import sys
sys.path.append('/path/to/md2word')

from scripts.main import convert_markdown_to_word

# 批量转换目录下所有 Markdown 文件
input_dir = './markdown_files'
output_dir = './word_files'
template = './template.docx'

for filename in os.listdir(input_dir):
    if filename.endswith('.md'):
        md_path = os.path.join(input_dir, filename)
        docx_path = os.path.join(output_dir, filename.replace('.md', '.docx'))

        print(f'Converting {filename}...')
        convert_markdown_to_word(md_path, docx_path, template)
        print(f'✓ Generated {docx_path}')
```

### 3️⃣ 安装到系统路径（全局使用）

#### macOS / Linux

```bash
# 方法一：创建软链接
sudo ln -s /path/to/md2word/md2word /usr/local/bin/md2word

# 方法二：复制到系统路径
sudo cp /path/to/md2word/md2word /usr/local/bin/
sudo cp -r /path/to/md2word/scripts /usr/local/bin/

# 之后可以在任何位置使用
cd ~/Documents
md2word report.md report.docx
```

#### Windows

```cmd
# 添加到系统环境变量 PATH
# 1. 右键"此电脑" > "属性" > "高级系统设置"
# 2. "环境变量" > 编辑 "Path"
# 3. 添加 md2word 目录路径

# 或创建批处理文件 md2word.bat
@echo off
python "C:\path\to\md2word\scripts\main.py" %*

# 将 md2word.bat 放到 C:\Windows\System32
```

### 4️⃣ 在其他项目中集成

#### 作为子模块使用

```bash
# 在您的项目中添加为 git submodule
git submodule add https://github.com/liyajun2alan/md2word.git vendor/md2word

# 在代码中使用
import sys
sys.path.append('./vendor/md2word')
from scripts.main import convert_markdown_to_word
```

#### 作为依赖项

创建您的项目的 `requirements.txt`：
```
# requirements.txt
git+https://github.com/liyajun2alan/md2word.git@v1.0.0
```

或在 `setup.py` 中：
```python
setup(
    name='your-project',
    install_requires=[
        'md2word @ git+https://github.com/liyajun2alan/md2word.git@v1.0.0',
    ],
)
```

### 5️⃣ Web API 封装（高级用法）

#### 使用 Flask 创建 REST API

```python
from flask import Flask, request, send_file
import sys
import os
import tempfile

sys.path.append('/path/to/md2word')
from scripts.main import convert_markdown_to_word

app = Flask(__name__)

@app.route('/convert', methods=['POST'])
def convert():
    # 获取上传的 Markdown 文件
    md_file = request.files['markdown']
    template_file = request.files.get('template')

    # 创建临时文件
    with tempfile.NamedTemporaryFile(suffix='.md', delete=False) as md_tmp:
        md_file.save(md_tmp.name)
        md_path = md_tmp.name

    docx_path = md_path.replace('.md', '.docx')

    # 转换
    if template_file:
        with tempfile.NamedTemporaryFile(suffix='.docx', delete=False) as tpl_tmp:
            template_file.save(tpl_tmp.name)
            convert_markdown_to_word(md_path, docx_path, tpl_tmp.name)
            os.unlink(tpl_tmp.name)
    else:
        convert_markdown_to_word(md_path, docx_path)

    # 返回生成的文件
    return send_file(docx_path, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

使用 API：
```bash
curl -X POST -F "markdown=@input.md" -F "template=@template.docx" \
     http://localhost:5000/convert -o output.docx
```

### 6️⃣ Docker 容器化部署

#### Dockerfile

```dockerfile
FROM python:3.11-slim

WORKDIR /app

# 复制项目文件
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY scripts/ ./scripts/
COPY references/ ./references/
COPY md2word .

RUN chmod +x md2word

# 创建工作目录
RUN mkdir /workspace
WORKDIR /workspace

ENTRYPOINT ["/app/md2word"]
```

#### 构建和使用

```bash
# 构建镜像
docker build -t md2word:latest .

# 使用容器转换文件
docker run --rm -v $(pwd):/workspace md2word:latest input.md output.docx

# 使用自定义模板
docker run --rm -v $(pwd):/workspace md2word:latest \
    input.md output.docx template.docx
```

## 配置说明

### 环境变量

```bash
# 设置默认模板路径
export MD2WORD_DEFAULT_TEMPLATE="/path/to/default_template.docx"

# 设置脚本目录（如果非标准安装）
export MD2WORD_SCRIPTS_DIR="/path/to/scripts"
```

### 自定义模板

将您的常用模板放在 `references/default_template.docx`，这样不指定模板时会自动使用它。

```bash
cp 公司标准模板.docx /path/to/md2word/references/default_template.docx
```

## 系统要求

### 最低要求
- **Python**: 3.8 或更高版本
- **内存**: 256MB（小文件）到 2GB（大文件含图片）
- **磁盘**: 50MB（安装） + 临时空间

### 依赖包
- `python-docx >= 0.8.11`: Word 文档处理
- `mistune >= 3.0.0`: Markdown 解析
- `Pillow`: 图片处理（可选，用于图片嵌入）

## 性能说明

| 文件大小 | 转换时间 | 内存占用 |
|---------|---------|---------|
| < 100KB | < 1秒   | ~50MB   |
| 100KB-1MB | 1-3秒 | ~100MB  |
| 1MB-10MB | 3-15秒 | ~200MB  |
| > 10MB  | > 15秒  | ~500MB+ |

## 常见场景

### 场景 1：技术文档标准化

```bash
# 将所有技术文档转换为统一格式
for file in docs/*.md; do
    ./md2word "$file" "${file%.md}.docx" company_template.docx
done
```

### 场景 2：自动化文档生成

```bash
# 在 CI/CD 中自动生成文档
#!/bin/bash
# build_docs.sh

git clone https://github.com/liyajun2alan/md2word.git
cd md2word
pip install -r requirements.txt

./md2word ../README.md ../release_notes.docx ../templates/release.docx
```

### 场景 3：与其他工具结合

```bash
# 先用 pandoc 处理，再用 md2word 转换
pandoc input.org -o temp.md
./md2word temp.md output.docx template.docx
rm temp.md
```

### 场景 4：定时任务

```bash
# crontab -e
# 每天凌晨 2 点转换日报
0 2 * * * /path/to/md2word/md2word /data/daily_report.md /output/report_$(date +\%Y\%m\%d).docx
```

## 编程语言集成

### Python 项目

```python
# your_project.py
from md2word.scripts.main import convert_markdown_to_word

convert_markdown_to_word('input.md', 'output.docx')
```

### Node.js 项目

```javascript
// app.js
const { execSync } = require('child_process');

function convertMd2Word(mdFile, docxFile, template = null) {
    const cmd = template
        ? `./md2word/md2word ${mdFile} ${docxFile} ${template}`
        : `./md2word/md2word ${mdFile} ${docxFile}`;

    execSync(cmd);
    console.log(`✓ Generated ${docxFile}`);
}

convertMd2Word('input.md', 'output.docx', 'template.docx');
```

### Java 项目

```java
// DocumentConverter.java
import java.io.*;

public class DocumentConverter {
    public static void convertMd2Word(String mdFile, String docxFile, String template)
        throws IOException, InterruptedException {

        ProcessBuilder pb;
        if (template != null) {
            pb = new ProcessBuilder("./md2word/md2word", mdFile, docxFile, template);
        } else {
            pb = new ProcessBuilder("./md2word/md2word", mdFile, docxFile);
        }

        Process process = pb.start();
        int exitCode = process.waitFor();

        if (exitCode == 0) {
            System.out.println("✓ Generated " + docxFile);
        } else {
            throw new RuntimeException("Conversion failed");
        }
    }
}
```

### Shell 脚本

```bash
#!/bin/bash
# convert_docs.sh

MD2WORD_PATH="/path/to/md2word/md2word"
TEMPLATE="/path/to/template.docx"

convert_document() {
    local input=$1
    local output=$2

    echo "Converting $input..."
    "$MD2WORD_PATH" "$input" "$output" "$TEMPLATE"

    if [ $? -eq 0 ]; then
        echo "✓ Success: $output"
    else
        echo "✗ Failed: $input"
        return 1
    fi
}

# 批量转换
for md in *.md; do
    convert_document "$md" "${md%.md}.docx"
done
```

## 故障排查

### 问题 1：找不到 Python 模块

```bash
# 确保安装了依赖
pip install -r requirements.txt

# 检查 Python 路径
python3 -c "import sys; print(sys.path)"
```

### 问题 2：权限错误

```bash
# 添加执行权限
chmod +x md2word

# 或直接用 Python 运行
python3 scripts/main.py input.md output.docx
```

### 问题 3：找不到模板

```bash
# 使用绝对路径
./md2word input.md output.docx /absolute/path/to/template.docx

# 或设置默认模板
export MD2WORD_DEFAULT_TEMPLATE="/path/to/template.docx"
```

### 问题 4：中文路径问题

```python
# 确保使用 UTF-8 编码
# 在 Python 脚本开头添加
import sys
import os
os.environ['PYTHONIOENCODING'] = 'utf-8'
```

## 与 Claude Code 的区别

| 特性 | Claude Code 中使用 | 独立使用 |
|-----|------------------|---------|
| 安装方式 | 自动识别 Skills 目录 | 需手动克隆/安装 |
| 调用方式 | 自然语言 + 命令 | 仅命令行 |
| 路径处理 | Claude 自动推断 | 需明确指定 |
| 批量操作 | Claude 智能处理 | 需编写脚本 |
| 错误提示 | 自然语言解释 | 原始错误信息 |
| 适用场景 | 交互式使用 | 自动化/集成 |

## 开源协议

MIT License - 可自由用于商业和个人项目

## 获取帮助

- 📚 完整文档: https://github.com/liyajun2alan/md2word
- 🐛 报告问题: https://github.com/liyajun2alan/md2word/issues
- 💬 讨论区: https://github.com/liyajun2alan/md2word/discussions

---

**总结**: md2word 是一个标准的 Python 工具，可以像任何其他命令行工具一样独立使用，无需依赖 Claude Code。
