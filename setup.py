#!/usr/bin/env python3
"""Setup script for md2pdf CLI tool."""

from setuptools import setup, find_packages
from pathlib import Path

# Read the README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding='utf-8')

setup(
    name='md2pdf',
    version='1.0.0',
    description='Convert Markdown files to beautiful PDFs with emoji support',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/md2pdf',
    packages=find_packages(),
    py_modules=['md2pdf'],
    install_requires=[
        'markdown==3.5.1',
        'weasyprint==62.3',
        'pydyf==0.11.0',
        'pygments==2.17.2',
        'click==8.1.7',
    ],
    entry_points={
        'console_scripts': [
            'md2pdf=md2pdf:main',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Text Processing :: Markup',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
    ],
    python_requires='>=3.8',
    keywords='markdown pdf converter cli emoji',
)
