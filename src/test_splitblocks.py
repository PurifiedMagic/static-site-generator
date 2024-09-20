import unittest

from textnode import TextNode
from splitblocks import *

class TestSplitBlock(unittest.TestCase):
    def test_eq_example(self):
        input = """\
        # This is a heading
        
        This is a paragraph of text. It has some **bold** and *italic* words inside of it.
        
        * This is the first list item in a list block
        * This is a list item
        * This is another list item"""

        output = [
        "# This is a heading",
        "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
        "* This is the first list item in a list block",
        "* This is a list item",
        "* This is another list item"
        ]
        
        self.assertEqual(markdown_to_blocks(input), output)