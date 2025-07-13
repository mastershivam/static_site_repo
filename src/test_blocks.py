from block_markdown import markdown_to_blocks
def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

import unittest
from block_markdown import block_to_block_type, BlockType

class TestBlockToBlockType(unittest.TestCase):
    def test_heading_block(self):
        md = "# This is a heading"
        self.assertEqual(block_to_block_type(md), BlockType.HEADING)

    def test_unordered_list_block(self):
        md = "- item one\n- item two\n- item three"
        self.assertEqual(block_to_block_type(md), BlockType.ULIST)


if __name__ == "__main__":
    unittest.main()