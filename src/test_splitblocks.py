import unittest

from textnode import TextNode
from splitblocks import *
from block_to_html import *

class TestSplitBlock(unittest.TestCase):
    def test_eq_example(self):
        input = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""

        output = [
        "# This is a heading",
        "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
        """* This is the first list item in a list block
* This is a list item
* This is another list item"""
        ]
        
        self.assertEqual(markdown_to_blocks(input), output)

class TestBlockType(unittest.TestCase):
    def test_eq_types(self):
        input = [
            "###Heading 3",
            "```print('Hello World!')```",
            "> To be, or not to be",
            "* unordered list type one",
            "- unordered list type two",
            "1. ordered list item one",
            "10. ordered list item two",
            "Test paragraph"
        ]
        output = [
            "heading",
            "code",
            "quote",
            "unordered_list",
            "unordered_list",
            "ordered_list",
            "ordered_list",
            "paragraph"
        ]
        
        for i in range(len(input)):
            self.assertEqual(block_to_block_type(input[i]), output[i])

class TestBlockToHTML(unittest.TestCase):
    def test_eq(self):
        input = """\
# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""

        output = """<div><h1>This is a heading</h1>\
<p>This is a paragraph of text. It has some <b>bold</b> and <i>italic</i> words inside of it.</p>\
<ul><li>This is the first list item in a list block</li>\
<li>This is a list item</li>\
<li>This is another list item</li></ul></div>\
"""
        self.assertEqual(markdown_to_html_node(input), output)