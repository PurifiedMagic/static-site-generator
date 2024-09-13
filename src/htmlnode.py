class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag # string for HTML tags scu has p, a, h1
        self.value = value # string for values within HTML tags
        self.children = children # list of child HTML nodes for current node
        self.props = props # dictionary of key-value pairs of HTML node attributes (e.g. a: href)

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props is None:
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
    