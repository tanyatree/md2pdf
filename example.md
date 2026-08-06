# Welcome to Markdown to PDF! 📚

This is a sample document to demonstrate the **amazing** features of our converter! 🎉

## Line Breaks ↩️

This paragraph is hard-wrapped in the source file: every line stops at around 78
characters, which is how most markdown is written and what a linter with MD013
enabled will ask you to do. In the PDF it should read as one continuous
paragraph that flows to the page width, with no breaks at those wrap points. If
you see it chopped into short lines instead, the `nl2br` extension is on and it
should not be.

Explicit line breaks still work. This line ends with two spaces,  
so this one starts on its own line.

If your markdown is written with one long line per paragraph and you *want*
every newline to become a break, run `md2pdf document.md --breaks`.

## Why Use This Tool? 🤔

Converting Markdown to PDF has never been easier! Here's what makes this tool special:

- ✅ **Full emoji support** - Express yourself! 😊 🚀 💡
- ✅ **Beautiful formatting** - Professional-looking documents
- ✅ **Code highlighting** - Perfect for technical docs
- ✅ **Tables and more** - Everything you need

## Code Examples 💻

Here's some Python code:

```python
def greet(name):
    """Greet someone warmly!"""
    return f"Hello, {name}! 👋"

# Test it out
print(greet("World"))
```

And some JavaScript:

```javascript
const calculateSum = (a, b) => {
    return a + b;
};

console.log(calculateSum(5, 3)); // Output: 8
```

## Tables Work Great! 📊

| Feature | Status | Notes |
|---------|--------|-------|
| Emojis | ✅ Working | Full Unicode support |
| Tables | ✅ Working | Clean and professional |
| Code | ✅ Working | Syntax highlighting included |
| Images | ✅ Working | Embedded images supported |

## Lists and More 📝

### Unordered Lists

- First item 🥇
- Second item 🥈
- Third item 🥉
  - Nested item
  - Another nested item

### Ordered Lists

1. Install dependencies
2. Run the converter
3. Enjoy your PDF! 🎊

## Blockquotes 💬

> "The best way to predict the future is to create it." - Peter Drucker
>
> This tool helps you create beautiful PDFs from your Markdown documents! 📄

## Links and Emphasis 🔗

Visit [GitHub](https://github.com) for more awesome projects!

You can use *italic text*, **bold text**, or even ***both combined***!

## Horizontal Rule

---

## Conclusion 🎯

This converter supports all standard Markdown features and renders them beautifully in PDF format. Try it out with your own documents! 🚀

Happy converting! 😄✨
