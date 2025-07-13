from textnode import TextNode, TextType
from text_to_text_nodes import text_to_textnodes


def test_text_to_textnodes():
    # Test 1: Simple text with bold and italic
    text = "This is **bold** and _italic_ text."
    nodes = text_to_textnodes(text)
    assert nodes == [
        TextNode("This is ", TextType.TEXT),
        TextNode("bold", TextType.BOLD),
        TextNode(" and ", TextType.TEXT),
        TextNode("italic", TextType.ITALIC),
        TextNode(" text.", TextType.TEXT),
    ]

    # Test 2: Text with image and link
    text = "Here is an ![alt](img.png) and a [link](https://example.com)."
    nodes = text_to_textnodes(text)
    assert nodes == [
        TextNode("Here is an ", TextType.TEXT),
        TextNode("alt", TextType.IMAGE, "img.png"),
        TextNode(" and a ", TextType.TEXT),
        TextNode("link", TextType.LINK, "https://example.com"),
        TextNode(".", TextType.TEXT),
    ]

    # Test 3: Text with code, bold, and image
    text = "Some `code` and **bold** with ![pic](url.com)"
    nodes = text_to_textnodes(text)
    assert nodes == [
        TextNode("Some ", TextType.TEXT),
        TextNode("code", TextType.CODE),
        TextNode(" and ", TextType.TEXT),
        TextNode("bold", TextType.BOLD),
        TextNode(" with ", TextType.TEXT),
        TextNode("pic", TextType.IMAGE, "url.com"),
    ]
