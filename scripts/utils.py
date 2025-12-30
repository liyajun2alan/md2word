"""
工具函数模块
"""

from pathlib import Path


def validate_file_exists(file_path: str, file_desc: str = "文件") -> Path:
    """验证文件是否存在

    Args:
        file_path: 文件路径
        file_desc: 文件描述（用于错误提示）

    Returns:
        Path: 文件路径对象

    Raises:
        FileNotFoundError: 文件不存在或不是有效文件
    """
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"{file_desc}不存在: {file_path}")
    if not path.is_file():
        raise FileNotFoundError(f"{file_desc}不是有效文件: {file_path}")
    return path


def get_default_template() -> Path:
    """获取默认模板路径

    Returns:
        Path: 默认模板文件路径

    Raises:
        FileNotFoundError: 默认模板不存在
    """
    skill_dir = Path(__file__).parent.parent
    template_path = skill_dir / 'references' / 'default_template.docx'

    if not template_path.exists():
        raise FileNotFoundError(f"默认模板不存在: {template_path}")

    return template_path
