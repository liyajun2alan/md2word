#!/usr/bin/env python3
"""
Setup script for md2word
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read README
readme_file = Path(__file__).parent / "README.md"
long_description = readme_file.read_text(encoding="utf-8") if readme_file.exists() else ""

# Read requirements
requirements_file = Path(__file__).parent / "requirements.txt"
requirements = []
if requirements_file.exists():
    with open(requirements_file, encoding="utf-8") as f:
        requirements = [line.strip() for line in f if line.strip() and not line.startswith("#")]

setup(
    name="md2word",
    version="1.0.0",
    description="Convert Markdown to Word documents with template formatting",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="李亚军",
    author_email="744191027@qq.com",
    url="https://github.com/liyajun2alan/md2word",
    packages=find_packages(),
    package_data={
        "": ["references/*.docx"],
    },
    include_package_data=True,
    install_requires=requirements,
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "md2word=scripts.main:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Documentation",
        "Topic :: Text Processing :: Markup",
        "Topic :: Utilities",
    ],
    keywords="markdown word docx converter document",
    project_urls={
        "Bug Reports": "https://github.com/liyajun2alan/md2word/issues",
        "Source": "https://github.com/liyajun2alan/md2word",
    },
)
