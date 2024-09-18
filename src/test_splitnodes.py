import unittest

from textnode import TextNode
from splitnodes import *

class TestDelimiterPosition(unittest.TestCase):
    def test_eq_delimiters(self):
        input = [
            [TextNode("Multi-line delimiter test *italics* included", "text")],
            [TextNode("**Bold** first check", "text")],
            [TextNode("and last node as **Bold**", "text")]
        ]
        output = [
            [
                [TextNode("Multi-line delimiter test ", "text")],
                [TextNode("italics", "italic")],
                [TextNode(" included", "text")]
            ], [
                [TextNode("Bold", "bold")],
                [TextNode(" first check", "text")]
            ], [
                [TextNode("and last node as ", "text")],
                [TextNode("Bold", "bold")]
            ]
        ]

        self.assertEqual((input), (input), output)

class TestSplitNodes(unittest.TestCase):
    
    def test_eq_text(self):
        input = "This is just text"
        output = [
            TextNode("This is just text", "text")
            ]

        self.assertEqual(text_to_node(input), output)

    def test_eq_bold(self):
        input = "This sentence contains **bold** text."
        output = [
            TextNode("This sentence contains ", "text"),
            TextNode("bold", "bold"),
            TextNode(" text.", "text")
        ]

        self.assertEqual(text_to_node(input), output)

    def test_eq_italic(self):
        input = "There is *italicised* text here."
        output = [
            TextNode("There is ", "text"),
            TextNode("italicised", "italic"),
            TextNode(" text here.", "text")
        ]

        self.assertEqual(text_to_node(input), output)

    def test_eq_code(self):
        input = "Some `code` is present in this node!"
        output = [
            TextNode("Some ", "text"),
            TextNode("code", "code"),
            TextNode(" is present in this node!", "text")
        ]

        self.assertEqual(text_to_node(input), output)
        