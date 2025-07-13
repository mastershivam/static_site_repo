from textnode import TextNode, TextType
from regex_functions import extract_markdown_images,extract_markdown_links
def split_nodes_delimiter(old_nodes, delimiter, text_type):

    new_nodes = []
    
    for node in old_nodes:

        # Only split nodes of type TEXT
        
        if getattr(node, "text_type", None) != TextType.TEXT:
            new_nodes.append(node)
            continue

        text = node.text
        parts = text.split(delimiter)
        # If delimiter not found or not paired, just keep as is
        if len(parts) == 1:
            new_nodes.append(node)
            continue

        # If odd number of delimiters, treat as normal text (no unclosed formatting)
        if len(parts) % 2 == 0:
            # Even number of splits means odd number of delimiters, so ignore
            new_nodes.append(node)
            continue

        for i, part in enumerate(parts):
            if part == "":
                continue  # skip empty segments (e.g. at start/end)
            if i % 2 == 0:
                # Even index: normal text
                if part:
                    new_nodes.append(TextNode(part, TextType.TEXT))
            else:
                # Odd index: delimited text
                if part:
                    new_nodes.append(TextNode(part, text_type))
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    
    for node in old_nodes:
        # Only split nodes of type TEXT
        if getattr(node, "text_type", None) != TextType.TEXT:
            new_nodes.append(node)
            continue

        text = node.text
        images = extract_markdown_images(text)
        
        if not images:
            new_nodes.append(node)
            continue

        # Split text by image patterns
        remaining_text = text
        for alt_text, url in images:
            # Find the image pattern in the remaining text
            image_pattern = f"![{alt_text}]({url})"
            parts = remaining_text.split(image_pattern, 1)
            
            if len(parts) == 2:
                # Add text before image
                if parts[0]:
                    new_nodes.append(TextNode(parts[0], TextType.TEXT))
                
                # Add image node
                new_nodes.append(TextNode(alt_text, TextType.IMAGE, url))
                
                # Update remaining text
                remaining_text = parts[1]
            else:
                # Pattern not found, keep as is
                new_nodes.append(node)
                break
        
        # Add any remaining text
        if remaining_text:
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))
            
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    
    for node in old_nodes:
        # Only split nodes of type TEXT
        if getattr(node, "text_type", None) != TextType.TEXT:
            new_nodes.append(node)
            continue

        text = node.text
        links = extract_markdown_links(text)
        
        if not links:
            new_nodes.append(node)
            continue

        # Split text by link patterns
        remaining_text = text
        for link_text, url in links:
            # Find the link pattern in the remaining text
            link_pattern = f"[{link_text}]({url})"
            parts = remaining_text.split(link_pattern, 1)
            
            if len(parts) == 2:
                # Add text before link
                if parts[0]:
                    new_nodes.append(TextNode(parts[0], TextType.TEXT))
                
                # Add link node
                new_nodes.append(TextNode(link_text, TextType.LINK, url))
                
                # Update remaining text
                remaining_text = parts[1]
            else:
                # Pattern not found, keep as is
                new_nodes.append(node)
                break
        
        # Add any remaining text
        if remaining_text:
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))
            
    return new_nodes



