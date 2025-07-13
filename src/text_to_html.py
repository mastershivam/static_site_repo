from htmlnode import LeafNode
from textnode import TextType

def text_node_to_html_node(text_node):

    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    elif text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    elif text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    elif text_node.text_type == TextType.LINK:
        if not text_node.url:
            raise ValueError("LINK type TextNode must have a url")
        return LeafNode("a", text_node.text, props={"href": text_node.url})
    elif text_node.text_type == TextType.IMAGE:
        if not text_node.url:
            raise ValueError("IMAGE type TextNode must have a url")
        return LeafNode("img", "", props={"src": text_node.url, "alt": text_node.text})
    else:
        raise Exception(f"Invalid text type: {text_node.text_type}")