import re

from textnode import TextNode

# Iterate through valid node types to split
def text_to_node(text):
    node = [TextNode(text, "text")]
    bold = split_nodes_delimiter(node, "**", "bold")
    italic = split_nodes_delimiter(bold, "*", "italic")
    code = split_nodes_delimiter(italic, "`", "code")
    image = split_nodes_image(code)
    link = split_nodes_link(image)
    return link

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

# Split image nodes by RegEx
def split_nodes_image(nodes):
    new_nodes = []
    for node in nodes:
        content = []

        # Add 'node' to content if 'node' is a list and check next node
        if type(node) == "list":
            content.extend(node)
            continue

        # Ensure node text is a string and has a type
        if isinstance(node.text, str) and node.text_type != None:
            extract_image = extract_markdown_images(node.text)

            # Split extracted image alt-text and link into proper format if not empty
            if len(extract_image) > 0:
                split_node = node.text.split(
                    f"![{extract_image[0][0]}]({extract_image[0][1]})", 1
                )
                if not split_node[0] == "":
                    content.append(TextNode(split_node[0], "text"))
                content.append(TextNode(extract_image[0][0], "image", extract_image[0][1]))
                if len(split_node[1]) >= 2 and not split_node[1] == "":
                    for link in split_nodes_image([TextNode(split_node[1], "text")]):
                        content.append(link)
            else:
                content.append(node)
        new_nodes.extend(content)
    return new_nodes

# Split link nodes by RegEx
def split_nodes_link(nodes):
    new_nodes = []
    for node in nodes:
        content = []

        # Add 'node' to content if 'node' is a list and check next node
        if type(node) == "list":
            content.extend(node)
            continue

        # Ensure node text is a string and has a type
        if isinstance(node.text, str) and node.text_type != None:
            extract_link = extract_markdown_links(node.text)

            # Split extracted link text and address into proper format if not empty
            if len(extract_link) > 0:
                split_node = node.text.split(
                    f"[{extract_link[0][0]}]({extract_link[0][1]})", 1
                )
                if not split_node[0] == "":
                    content.append(TextNode(split_node[0], "text"))
                content.append(TextNode(extract_link[0][0], "link", extract_link[0][1]))
                if len(split_node[1]) >= 2 and not split_node[1] == "":
                    for link in split_nodes_link([TextNode(split_node[1], "text")]):
                        content.append(link)
            else:
                content.append(node)
        new_nodes.extend(content)
    return new_nodes

# Extract image from text by RegEx
def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

# Extract link from text by RegEx
def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)