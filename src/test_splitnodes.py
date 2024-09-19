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

class TestImageNodes(unittest.TestCase):
    def test_eq_image(self):
        input = [
            TextNode(
                "This is the ![boot.dev logo](https://www.boot.dev/img/bootdev-logo-full-small.webp) from boot.dev",
                "text"
                )
        ]
        output = [
            TextNode(
                "This is the ",
                "text"
            ),
            TextNode(
                "boot.dev logo",
                "image",
                "https://www.boot.dev/img/bootdev-logo-full-small.webp"
            ),
            TextNode(
                " from boot.dev",
                "text"
            )
        ]

        self.assertEqual(split_nodes_image(input), split_nodes_image(output))

class TestLinkNodes(unittest.TestCase):
    def test_eq_link(self):
        input = [
            TextNode(
                "This is the [boot.dev homepage](https://www.boot.dev/) in text",
                "text"
                )
        ]
        output = [
            TextNode(
                "This is the ",
                "text"
            ),
            TextNode(
                "boot.dev homepage",
                "link",
                "https://www.boot.dev/"
            ),
            TextNode(
                " in text",
                "text"
            )
        ]

        self.assertEqual(split_nodes_link(input), split_nodes_link(output))