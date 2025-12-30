#!/bin/bash
# md2word 一键安装脚本
# 适用于 Claude Code Skills

set -e

echo "🚀 开始安装 md2word..."

# 检测安装目标目录
if [ -d "$HOME/.claude/skills" ]; then
    TARGET_DIR="$HOME/.claude/skills/md2word"
    echo "✓ 检测到 Claude Code 环境"
elif [ -n "$CLAUDE_SKILLS_DIR" ]; then
    TARGET_DIR="$CLAUDE_SKILLS_DIR/md2word"
    echo "✓ 使用环境变量 CLAUDE_SKILLS_DIR: $CLAUDE_SKILLS_DIR"
else
    TARGET_DIR="$HOME/.claude/skills/md2word"
    echo "📁 将安装到默认目录: $TARGET_DIR"
    mkdir -p "$HOME/.claude/skills"
fi

# 克隆或更新仓库
if [ -d "$TARGET_DIR" ]; then
    echo "📦 检测到已存在的安装，正在更新..."
    cd "$TARGET_DIR"
    git pull origin main
else
    echo "📥 正在下载 md2word..."
    git clone https://github.com/liyajun2alan/md2word.git "$TARGET_DIR"
    cd "$TARGET_DIR"
fi

# 检查 Python 版本
echo "🔍 检查 Python 环境..."
if ! command -v python3 &> /dev/null; then
    echo "❌ 错误: 未找到 Python 3"
    echo "请先安装 Python 3.8 或更高版本"
    exit 1
fi

PYTHON_VERSION=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
echo "✓ Python 版本: $PYTHON_VERSION"

# 安装依赖
echo "📦 安装 Python 依赖..."
pip3 install -r requirements.txt --quiet

# 添加执行权限
echo "🔧 配置执行权限..."
chmod +x md2word

# 测试安装
echo "🧪 测试安装..."
if ./md2word --help &> /dev/null || python3 scripts/main.py --help &> /dev/null; then
    echo "✅ 安装成功！"
else
    echo "⚠️  安装完成，但命令测试失败"
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🎉 md2word 已安装到: $TARGET_DIR"
echo ""
echo "📖 使用方法："
echo ""
echo "  在 Claude Code 中："
echo "    '帮我把这个 Markdown 转换为 Word'"
echo "    '导出 README.md 为 Word 文档'"
echo "    '/md2word input.md output.docx'"
echo ""
echo "  命令行："
echo "    cd $TARGET_DIR"
echo "    ./md2word input.md output.docx [template.docx]"
echo ""
echo "📚 完整文档: https://github.com/liyajun2alan/md2word"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
