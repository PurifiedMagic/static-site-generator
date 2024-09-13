class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag # string for HTML tags scu has p, a, h1
        self.value = value # string for values within HTML tags
        self.children = children # list of child HTML nodes for current node
        self.props = props # dictionary of key-value pairs of HTML node attributes (e.g. a: href)

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props is None or self.props == 0:
            return ""
        return " ".join(
            list(
                map(
                    lambda prop: f"{prop}=\x22{self.props[prop]}\x22", self.props
                )
            )
        )
    
    def __repr__(self):
        print(f"HTML ag: {self.tag}",
              f"Tag content: {self.value}",
              f"Child nodes: {self.children}",
              f"HTML node attributes: {self.props}"
              )
        
class LeafNode(HTMLNode):
    def __init__(self, tag, value, children=None, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Value cannot be NoneType. All leaf nodes must have a value")
        if self.tag is None:
            return str(self.value)
        if self.children is not None:
            return ValueError("LeafNode cannot have children")
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
