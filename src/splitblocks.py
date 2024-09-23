import re

def markdown_to_blocks(markdown):
    blocks = list(map(lambda m: m.strip(), markdown.split("\n\n")))
    for block in blocks:
        if block == "":
            blocks.pop(blocks.index(block))
    return blocks

def block_to_block_type(block):
    if block.startswith("#"):
        return "heading"
    if block.startswith("```"):
        return "code"
    if block.startswith(">"):
        return "quote"
    if block.startswith("* ") or block.startswith("- "):
        return "unordered_list"
    if re.match(r"^(\d{1,}\.\s)", block):
        return "ordered_list"
    return "paragraph"
