import htmlnode
import splitnodes
from textnode import TextNode
from splitblocks import block_to_block_type, markdown_to_blocks

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html_nodes = []
    for block in blocks:
        html_nodes.append(block_to_html(block, block_to_block_type(block)))
    tag = ""
    for node in html_nodes:
        tag += node
    content = htmlnode.LeafNode.to_html(htmlnode.LeafNode("div", tag))
    return content

def block_to_html(block, type):
    match(type):
        case "heading":
            return heading_to_html(block)
        case "code":
            return code_to_html(block)
        case "quote":
            return quote_to_html(block)
        case "unordered_list":
            return unordered_list_to_html(block)
        case "ordered_list":
            return ordered_list_to_html(block)
        case "paragraph":
            return paragraph_to_html(block)

        case _:
            raise NotImplementedError

def heading_to_html(block):
    heading_level = 0
    for char in block:
        if char == "#":
            heading_level += 1
    text_nodes = block[heading_level+1:]
    heading_text = splitnodes.text_to_node(text_nodes)
    html_nodes = [TextNode.text_node_to_html_node(node) for node in heading_text]
    parent = htmlnode.ParentNode.to_html(htmlnode.ParentNode(f"h{heading_level}", html_nodes))
    return parent

def code_to_html(block):
    code_text = splitnodes.text_to_node(block)
    html_nodes = [TextNode.text_node_to_html_node(node) for node in code_text]
    child_node = htmlnode.ParentNode("code", html_nodes)
    parent = htmlnode.ParentNode.to_html(htmlnode.ParentNode("pre", child_node))
    return parent

def quote_to_html(block):
    content = []
    for line in block.split("\n"):
        content.append(line[2:])
    quote_text = splitnodes.text_to_node("\n".join(content))
    html_nodes = [TextNode.text_node_to_html_node(node) for node in quote_text]
    parent = htmlnode.ParentNode.to_html(htmlnode.ParentNode("blockquote", html_nodes))
    return parent

def unordered_list_to_html(block):
    content = []
    for line in block.split("\n"):
        content.append(line[2:])
    list_item = list_item_to_html(content)
    html_node = htmlnode.ParentNode.to_html(htmlnode.ParentNode("ul", list_item))
    return html_node

def ordered_list_to_html(block):
    content = []
    for line in block.split("\n"):
        content.append(line[2:])
    list_item = list_item_to_html(content)
    html_node = htmlnode.ParentNode.to_html(htmlnode.ParentNode("ol", list_item))
    return html_node

def list_item_to_html(content):
    html_node = [htmlnode.LeafNode("li", line) for line in content]
    return html_node

def paragraph_to_html(block):
    paragraph_text = splitnodes.text_to_node(block)
    html_nodes = [TextNode.text_node_to_html_node(node) for node in paragraph_text]
    parent = htmlnode.ParentNode.to_html(htmlnode.ParentNode("p", html_nodes))
    return parent