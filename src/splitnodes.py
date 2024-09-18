import re

from textnode import TextNode

# Iterate through valid node types to split
def text_to_node(text):
    node = [TextNode(text, "text")]
    bold = split_nodes_delimiter(node, "**", "bold")
    italic = split_nodes_delimiter(bold, "*", "italic")
    code = split_nodes_delimiter(italic, "`", "code")
    return code

# Split text nodes by delimiter
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    
    # Raise Exception if 'old_nodes' input is a list
    if not isinstance(old_nodes, list):
        raise Exception("Nodes should be in a list")
    
    new_nodes = []
    for node in old_nodes:

        # Add non-"text" nodes to 'new_nodes' for next check
        if node.text_type != "text":
            new_nodes.extend([node])
            continue

        # Recurse 'node' if it is a nested list within 'old_nodes'
        if isinstance(node, list):
            new_nodes.extend(split_nodes_delimiter(node, delimiter, text_type))
            continue

        # Set 'text_node' to 'False' if node is not plain "text"
        if node.text.startswith(delimiter):
            text_node = False

        text_node = True
        line = node.text.split(delimiter)
        nodes_list = []
        
        # Add each split text segment by "text" or other valid type
        for text in line:
            if text_node is True:
                nodes_list.append(TextNode(text, "text"))
            else:
                nodes_list.append(TextNode(text, text_type))
            text_node = not text_node
        new_nodes.extend(nodes_list)
    return new_nodes

