# Installation Guide

## Quick Install

```bash
# Install in development mode (recommended for local use)
pip install -e .

# Or install normally
pip install .
```

After installation, you can use `md2pdf` from anywhere:

```bash
md2pdf document.md
```

## Uninstall

```bash
pip uninstall md2pdf
```

## Build Distribution Package

If you want to create a distributable package:

```bash
# Install build tools
pip install build

# Build the package
python -m build

# This creates dist/md2pdf-1.0.0.tar.gz and dist/md2pdf-1.0.0-py3-none-any.whl
```

## Install from Distribution

```bash
pip install dist/md2pdf-1.0.0-py3-none-any.whl
```

## Publish to PyPI (Optional)

```bash
# Install twine
pip install twine

# Upload to PyPI
twine upload dist/*
```
