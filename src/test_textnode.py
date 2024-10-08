import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):

    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", "italic")
        node2 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node, node2)

    def test_is_none(self):
        node = TextNode("Boot.dev is great!", None, "https://www.boot.dev")
        self.assertIsNone(node.text_type)

    def test_invalid_text_type(self):
        node = TextNode("I strongly agree", "strong")
        self.assertRaises(Exception)

if __name__ == "__main__":
    unittest.main()