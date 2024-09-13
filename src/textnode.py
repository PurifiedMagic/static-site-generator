import htmlnode

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (
            self.text == other.text) and (
                self.text_type == other.text_type) and (
                    self.url == other.url
                    )
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    
    def text_node_to_html_node(text_node):
        match text_node.text_type:
            case "text":
                return htmlnode.LeafNode(None, text_node.text)
            case "bold":
                return htmlnode.LeafNode("b", text_node.text)
            case "italic":
                return htmlnode.LeafNode("i", text_node.text)
            case "code":
                return htmlnode.LeafNode("code", text_node.text)
            case "link":
                return htmlnode.LeafNode("a", text_node.text, {"href": text_node.url})
            case "image":
                return htmlnode.LeafNode("img", "",{"src": text_node.url,
                                                    "alt": text_node.text})
            case _:
                raise Exception(f"Invalid text node type: {text_node.text_type}")
