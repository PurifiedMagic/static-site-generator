import unittest

from htmlnode import HTMLNode

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


if __name__ == "__main__":
    unittest.main()