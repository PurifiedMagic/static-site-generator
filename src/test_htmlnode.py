import unittest

from htmlnode import HTMLNode, ParentNode, LeafNode

class TestHTMLNode(unittest.TestCase):

    def test_eq(self):
        node = HTMLNode(
            "img",
            None,
            None,
            {
                "alt": "boot dot dev logo",
                "href": "https://www.boot.dev"
            }
        )
        node2 = node
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = HTMLNode(
            "h1",
            "Test Heading",
            None,
            {}
        )
        node2 = HTMLNode(
            "span",
            "Test Heading",
            None,
            {
                "role": "heading",
                "aria-level": "1"
            }
        )
        self.assertNotEqual(node, node2)

    def test_no_props(self):
        node = HTMLNode(
            "button",
            "Inaccessible Button",
            None,
            None
        )
        self.assertIsNone(node.props)

    def test_props_to_html(self):
        node = HTMLNode(
            "input",
            None,
            None,
            {
                "aria-labelledby": "input-label",
                "aria-invalid": "false",
                "aria-describedby": "input-error"
            }
        )
        print(node.props_to_html())
        self.assertIsNot(node.props_to_html(), "")

class TestParentNode(unittest.TestCase):
    def test_parent_tag(self):
        node = ParentNode(
            None,
            None,
            [
                "li",
                "li",
                "li"
            ],
            {
                "class": "ordered_list_style"
            }
        )
        self.assertRaises(ValueError)

    def test_no_children(self):
        node = ParentNode(
            "ul",
            None,
            [],
            None
        )
        node2 = ParentNode(
            "ol",
            None,
            None,
            None
        )
        self.assertRaises(ValueError)

    def test_parent_children(self):
        node = ParentNode(
            "ul",
            [
                LeafNode(
                    "li",
                    "list item one",
                    None, 
                    {
                        "class": "list-item"
                    }
                ),
                LeafNode(
                    "li",
                    "list item two",
                    [
                        LeafNode(
                            "strong",
                            None,
                            None,
                            None
                        )
                    ]
                ),
                LeafNode(
                    "li",
                    "list item three",
                    [
                        LeafNode(
                            "a",
                            "Boot.dev",
                            None,
                            {
                                "href": "https://www.boot.dev",
                                "aria-label": 
                                "Boot dot dev, gamifying back-end development concepts"
                            }
                        )
                    ]
                )
            ]
        )
        print(f"{node.to_html()}")

class TestLeafNode(unittest.TestCase):

    def test_leaf_props(self):
        node = LeafNode(
            "span",
            "Leaf node with props",
            None,
            {
                "role": "heading",
                "aria-level": "4"
            }
        )
        node2 = LeafNode(
            "span",
            "Leaf node with no props",
            None,
            None
        )
        node3 = LeafNode(
            "span",
            "Leaf node with empty props dictionary",
            None,
            {}
        )
        print(f"{node.to_html()}\n{node2.to_html()}\n{node3.to_html()}")

    def test_leaf_value_error(self):
        node = LeafNode(
            "h1",
            None,
            None,
            None
        )
        self.assertRaises(ValueError)

    def test_leaf_children_error(self):
        node = LeafNode(
            "strong",
            "Strong tag should not have children",
            [
                "Invalid child"
            ],
            None
        )
        self.assertRaises(ValueError)

if __name__ == "__main__":
    unittest.main()