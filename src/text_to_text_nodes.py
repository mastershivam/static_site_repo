from textnode import TextNode, TextType
from split_node_delim import split_nodes_delimiter, split_nodes_image, split_nodes_link

def text_to_textnodes(text):
    """
    Converts a markdown string into a list of TextNode objects,
    splitting by images, links, bold, italic, and code formatting.
    """
    # Start with a single TEXT node
    nodes = [TextNode(text, TextType.TEXT)]

    # Split out images first (since they can contain other delimiters)
    nodes = split_nodes_image(nodes)
    # Split out links next
    nodes = split_nodes_link(nodes)
    # Split out code blocks (backticks)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    # Split out bold (**)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    # Split out italic (_)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)

    # Filter out empty text nodes
    nodes = [node for node in nodes if node.text]
    return nodes

