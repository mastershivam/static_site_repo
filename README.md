# Static Site Generator

A Python-based static site generator that converts Markdown content into HTML pages with a clean, responsive design.

## Features

- **Markdown to HTML Conversion**: Converts Markdown files to HTML using custom parsing
- **Template System**: Uses HTML templates with placeholders for dynamic content
- **Static Asset Management**: Automatically copies CSS, images, and other static files
- **Multiple Content Types**: Supports paragraphs, headings, code blocks, lists, quotes, and more
- **Text Formatting**: Handles bold, italic, code, links, and images within text
- **Local Development Server**: Built-in HTTP server for testing

## Project Structure

```
static_site_repo/
├── src/                    # Source code
│   ├── main.py            # Main entry point
│   ├── gencontent.py      # Content generation logic
│   ├── block_markdown.py  # Markdown block parsing
│   ├── text_to_html.py    # Text node to HTML conversion
│   ├── htmlnode.py        # HTML node classes
│   ├── textnode.py        # Text node classes
│   └── test_*.py          # Unit tests
├── content/               # Markdown content
│   ├── index.md          # Homepage content
│   ├── blog/             # Blog posts
│   └── contact/          # Contact page
├── static/               # Static assets
│   ├── index.css         # Stylesheet
│   └── images/           # Image files
├── public/               # Generated output (created by build)
├── template.html         # HTML template
├── build.sh              # Build script
├── main.sh               # Development server script
└── test.sh               # Test runner
```

## Usage

### Building the Site

1. **Generate the static site:**
   ```bash
   chmod +x build.sh
   ./build.sh
   ```

2. **Start the development server:**
   ```bash
   chmod +x main.sh
   ./main.sh
   ```

3. **Run tests:**
   ```bash
   chmod +x test.sh
   ./test.sh
   ```

### Development Workflow

1. Add or modify Markdown files in the `content/` directory
2. Add static assets (CSS, images) to the `static/` directory
3. Run `./build.sh` to generate the site
4. Run `./main.sh` to start the local server at `http://localhost:8888`
5. View your changes in the browser

## Markdown Features Supported

- **Headings**: `# H1`, `## H2`, etc.
- **Paragraphs**: Regular text blocks
- **Code Blocks**: ```code```
- **Blockquotes**: `> quoted text`
- **Unordered Lists**: `- item`
- **Ordered Lists**: `1. item`
- **Text Formatting**: `**bold**`, `*italic*`, `` `code` ``
- **Links**: `[text](url)`
- **Images**: `![alt](image.png)`

## Template System

The site uses `template.html` as a base template with placeholders:
- `{{ Title }}`: Page title extracted from the first H1 heading
- `{{ Content }}`: Generated HTML content from Markdown

## Technologies Used

- **Python 3**: Core language
- **Markdown**: Content format
- **HTML/CSS**: Output format and styling
- **Unit Testing**: Comprehensive test suite

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Run the test suite
6. Submit a pull request

## License

This project is part of the Boot.dev curriculum and is for educational purposes.

