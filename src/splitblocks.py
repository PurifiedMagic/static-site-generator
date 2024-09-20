from textnode import TextNode

def markdown_to_blocks(markdown):
    blocks = list(map(lambda m: m.strip(), markdown.split("\n")))
    for block in blocks:
        if block == "":
            blocks.pop(blocks.index(block))
    return blocks


    
