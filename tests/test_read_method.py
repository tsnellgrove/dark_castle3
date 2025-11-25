#!/usr/bin/env python3
"""
Unit tests for read() method - demonstrates testing methods that require GameState
"""

import unittest
import sys
import os
from unittest.mock import Mock, MagicMock

# Add the project root to the path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from cleesh.class_std.base_class_def import Writing, ViewOnly


class TestReadMethod(unittest.TestCase):
    """Test cases for the read() method"""
    
    def setUp(self):
        """Set up test fixtures"""
        # Create a Writing object
        self.test_writing = Writing('scroll_text', 'Ancient Scroll Text', 'text', 'scroll_text_key')
        
        # Create a ViewOnly object with writing
        self.readable_item = ViewOnly('scroll', 'Ancient Scroll', 'scroll', 'scroll_desc', self.test_writing)
        
        # Create a mock GameState
        self.mock_gs = Mock()
        self.mock_gs.io = Mock()
        self.mock_gs.io.buffer = Mock()
        self.mock_gs.io.get_str = Mock(return_value="Ancient scroll text")
        self.mock_gs.core = Mock()
        self.mock_gs.core.hero = Mock()
    
    def test_read_with_writing(self):
        """Test reading an object that has writing"""
        # Call the read method
        self.readable_item.read(self.mock_gs)
        
        # Verify that buffer was called with formatted text
        self.mock_gs.io.buffer.assert_called_once()
        call_args = self.mock_gs.io.buffer.call_args[0][0]
        self.assertIn('Ancient Scroll', call_args)
        self.assertIn('Ancient Scroll Text', call_args)
    
    def test_read_without_writing(self):
        """Test reading an object that has no writing"""
        # Create an object without writing
        no_writing_item = ViewOnly('rock', 'Plain Rock', 'rock', 'rock_desc', None)
        
        # Call the read method
        no_writing_item.read(self.mock_gs)
        
        # Verify that buffer was not called (since there's no writing)
        self.mock_gs.io.buffer.assert_not_called()


class TestReadMethodIntegration(unittest.TestCase):
    """Integration tests that test read() with more realistic GameState"""
    
    def setUp(self):
        """Set up more realistic test fixtures"""
        # Create a more complete mock GameState
        self.mock_gs = Mock()
        self.mock_gs.io = Mock()
        self.mock_gs.io.buffer = Mock()
        self.mock_gs.io.get_str = Mock(return_value="Ancient magical text")
        
        # Track what gets buffered
        self.buffered_content = []
        self.mock_gs.io.buffer.side_effect = lambda text: self.buffered_content.append(text)
        
        # Create test objects
        self.writing = Writing('magic_runes', 'Magic Runes', 'runes', 'magic_runes_desc')
        self.magic_tablet = ViewOnly('tablet', 'Magic Tablet', 'tablet', 'tablet_desc', self.writing)
    
    def test_read_buffers_correct_content(self):
        """Test that read() buffers the correct writing description"""
        # Call read
        self.magic_tablet.read(self.mock_gs)
        
        # Check that buffer was called with the expected text format
        self.assertEqual(len(self.buffered_content), 1)
        expected_text = "On the Magic Tablet, written in Magic Runes, you read: Ancient magical text."
        self.assertEqual(self.buffered_content[0], expected_text)
    
    def test_multiple_reads(self):
        """Test reading multiple objects"""
        # Create another readable object
        second_writing = Writing('old_text', 'Old Text', 'text', 'old_text_desc')
        old_book = ViewOnly('book', 'Old Book', 'book', 'book_desc', second_writing)
        
        # Read both objects
        self.magic_tablet.read(self.mock_gs)
        old_book.read(self.mock_gs)
        
        # Check that both were buffered
        self.assertEqual(len(self.buffered_content), 2)
        self.assertTrue(any('Magic Tablet' in text for text in self.buffered_content))
        self.assertTrue(any('Old Book' in text for text in self.buffered_content))


if __name__ == '__main__':
    unittest.main()