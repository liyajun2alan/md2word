#!/usr/bin/env python3
"""
md2word Skill - 主入口脚本
将 Markdown 文件按照 Word 模板格式追加到目标 Word 文件
"""

import sys
import argparse
from pathlib import Path

from template_parser import TemplateParser
from markdown_parser import MarkdownParser
from word_generator import WordGenerator
from utils import validate_file_exists, get_default_template


def main():
    """主函数"""
    parser = argparse.ArgumentParser(
        description='将 Markdown 文件按照 Word 模板格式追加到目标 Word 文件'
    )
    parser.add_argument('md_file', help='Markdown 文件路径')
    parser.add_argument('word_file', help='目标 Word 文件路径')
    parser.add_argument('template_file', nargs='?', default=None, help='模板 Word 文件路径（可选）')
    parser.add_argument('--debug', action='store_true', help='调试模式（打印详细信息）')

    args = parser.parse_args()

    print("🚀 md2word Skill")
    print("=" * 60)

    # 1. 验证输入文件
    print("\n📂 验证文件...")
    try:
        md_path = validate_file_exists(args.md_file, "Markdown 文件")

        # 模板文件：优先使用用户指定，否则使用默认模板
        if args.template_file:
            template_path = validate_file_exists(args.template_file, "模板文件")
        else:
            template_path = get_default_template()
            print(f"   使用默认模板: {template_path.name}")

        word_path = Path(args.word_file)
        print(f"✅ 输入文件验证完成")

    except FileNotFoundError as e:
        print(f"❌ 错误: {e}")
        sys.exit(1)

    # 2. 提取模板格式
    print("\n🎨 提取模板格式...")
    try:
        template_parser = TemplateParser(str(template_path))
        format_styles = template_parser.extract_all_formats()

        print(f"✅ 提取了 {len(format_styles)} 种格式样式")
        if args.debug:
            for style_name in format_styles.keys():
                print(f"   - {style_name}")

    except Exception as e:
        print(f"❌ 提取模板格式时出错: {e}")
        if args.debug:
            import traceback
            traceback.print_exc()
        sys.exit(1)

    # 3. 解析 Markdown
    print("\n📝 解析 Markdown...")
    try:
        md_parser = MarkdownParser(str(md_path))
        elements = md_parser.parse()

        print(f"✅ 解析了 {len(elements)} 个元素")
        if args.debug:
            element_types = {}
            for elem in elements:
                elem_type = elem['type']
                element_types[elem_type] = element_types.get(elem_type, 0) + 1

            for elem_type, count in element_types.items():
                print(f"   - {elem_type}: {count}")

    except Exception as e:
        print(f"❌ 解析 Markdown 时出错: {e}")
        if args.debug:
            import traceback
            traceback.print_exc()
        sys.exit(1)

    # 4. 生成 Word 文档
    print("\n📄 生成 Word 文档...")
    try:
        generator = WordGenerator(str(word_path), format_styles, str(template_path))
        generator.load_target_document()
        generator.append_elements(elements)
        generator.save()

        print(f"✅ 文档已保存: {word_path}")

    except Exception as e:
        print(f"❌ 生成 Word 文档时出错: {e}")
        if args.debug:
            import traceback
            traceback.print_exc()
        sys.exit(1)

    # 5. 完成
    print("\n" + "=" * 60)
    print("🎉 转换完成!")
    print(f"   输入: {md_path.name}")
    print(f"   输出: {word_path.name}")
    print(f"   元素: {len(elements)} 个")


if __name__ == '__main__':
    main()
