"""
Markdown 解析模块

解析 Markdown 文件，生成结构化元素列表
"""

import mistune
from typing import List, Dict, Any
import re


class MarkdownParser:
    """Markdown 解析器，生成结构化元素"""

    def __init__(self, md_path: str):
        """初始化

        Args:
            md_path: Markdown 文件路径
        """
        self.md_path = md_path
        self.elements = []

    def parse(self) -> List[Dict[str, Any]]:
        """解析 Markdown 文件，返回元素列表

        Returns:
            结构化元素列表
        """
        with open(self.md_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 使用自定义渲染器，启用表格插件
        renderer = StructuredRenderer()
        markdown = mistune.create_markdown(renderer=renderer, plugins=['table'])
        markdown(content)

        return renderer.elements


class StructuredRenderer(mistune.BaseRenderer):
    """自定义渲染器，生成结构化元素而非 HTML"""

    def __init__(self):
        """初始化"""
        super().__init__()
        self.elements = []

    def heading(self, token, state):
        """处理标题"""
        level = token['attrs']['level']
        text = self.render_children(token, state)
        self.elements.append({
            'type': f'heading{level}',
            'text': str(text).strip(),
            'level': level
        })
        return ''

    def paragraph(self, token, state):
        """处理段落"""
        text = self.render_children(token, state)
        clean_text = str(text).strip()
        if clean_text:
            self.elements.append({
                'type': 'body',
                'text': clean_text
            })
        return ''

    def block_code(self, token, state):
        """处理代码块"""
        code = token['raw']
        info = token.get('attrs', {}).get('info', None)
        self.elements.append({
            'type': 'code',
            'text': code.rstrip('\n'),
            'language': info
        })
        return ''

    def block_quote(self, token, state):
        """处理引用块"""
        text = self.render_children(token, state)
        self.elements.append({
            'type': 'quote',
            'text': str(text).strip()
        })
        return ''

    def list(self, token, state):
        """处理列表"""
        ordered = token['attrs'].get('ordered', False)
        items = []

        for child in token['children']:
            if child['type'] == 'list_item':
                item_text = self.render_children(child, state)
                items.append(str(item_text).strip())

        if items:
            self.elements.append({
                'type': 'list',
                'items': items,
                'ordered': ordered
            })
        return ''

    def list_item(self, token, state):
        """处理列表项"""
        return self.render_children(token, state)

    def table(self, token, state):
        """处理表格"""
        header = []
        body = []

        for child in token['children']:
            if child['type'] == 'table_head':
                # table_head 直接包含 table_cell（不经过 table_row）
                for cell in child['children']:
                    if cell['type'] == 'table_cell':
                        cell_text = self.render_children(cell, state)
                        header.append(str(cell_text).strip())

            elif child['type'] == 'table_body':
                # table_body 包含 table_row，table_row 包含 table_cell
                for row in child['children']:
                    if row['type'] == 'table_row':
                        row_data = []
                        for cell in row['children']:
                            if cell['type'] == 'table_cell':
                                cell_text = self.render_children(cell, state)
                                row_data.append(str(cell_text).strip())
                        body.append(row_data)

        if header or body:
            self.elements.append({
                'type': 'table',
                'header': header,
                'body': body
            })
        return ''

    def table_head(self, token, state):
        """表格头"""
        return self.render_children(token, state)

    def table_body(self, token, state):
        """表格体"""
        return self.render_children(token, state)

    def table_row(self, token, state):
        """表格行"""
        return self.render_children(token, state)

    def table_cell(self, token, state):
        """表格单元格"""
        return self.render_children(token, state)

    def image(self, token, state):
        """处理图片"""
        attrs = token.get('attrs', {})
        self.elements.append({
            'type': 'image',
            'src': attrs.get('url', ''),
            'title': attrs.get('title', None),
            'alt': attrs.get('alt', '')
        })
        return ''

    def strong(self, token, state):
        """粗体 - 保持原样"""
        return self.render_children(token, state)

    def emphasis(self, token, state):
        """斜体 - 保持原样"""
        return self.render_children(token, state)

    def codespan(self, token, state):
        """行内代码 - 保持原样"""
        return token.get('raw', '')

    def linebreak(self, token, state):
        """换行"""
        return '\n'

    def link(self, token, state):
        """链接 - 保持文本"""
        return self.render_children(token, state)

    def blank_line(self, token, state):
        """空行 - 忽略"""
        return ''

    def thematic_break(self, token, state):
        """分隔线 - 忽略"""
        return ''

    def text(self, token, state):
        """普通文本"""
        return token.get('raw', '')

    def softbreak(self, token, state):
        """软换行"""
        return ' '

    def block_html(self, token, state):
        """HTML 块 - 忽略或提取文本"""
        # 可以选择忽略 HTML，或者尝试提取其中的文本
        return ''

    def inline_html(self, token, state):
        """行内 HTML - 忽略"""
        return ''

    def newline(self, token, state):
        """新行"""
        return '\n'

    def block_text(self, token, state):
        """块文本 - 用于列表项内容"""
        return self.render_children(token, state)

    def render_children(self, token, state):
        """渲染子元素"""
        children = token.get('children', [])
        if not children:
            return ''

        result = []
        for child in children:
            child_type = child.get('type', '')
            method = getattr(self, child_type, None)

            if method:
                rendered = method(child, state)
                if rendered:
                    result.append(rendered)
            elif 'raw' in child:
                result.append(child['raw'])

        return ''.join(result)
