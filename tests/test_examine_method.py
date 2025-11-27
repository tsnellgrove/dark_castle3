#!/usr/bin/env python3
"""
Unit and Integration tests for examine() method
"""

import unittest
import sys
import os
from unittest.mock import Mock, MagicMock

# Add the project root to the path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from cleesh.class_std.base_class_def import Writing, ViewOnly


class TestExamineMethod(unittest.TestCase):
    """Unit tests for the examine() method"""
    
    def setUp(self):
        """Set up test fixtures"""
        # Create test objects
        self.writing = Writing('runes', 'Ancient Runes', 'runes', 'runes_desc')
        self.simple_item = ViewOnly('stone', 'Gray Stone', 'stone', 'stone_desc', None)
        self.item_with_writing = ViewOnly('tablet', 'Stone Tablet', 'tablet', 'tablet_desc', self.writing)
        
        # Create mock GameState
        self.mock_gs = Mock()
        self.mock_gs.io = Mock()
        self.mock_gs.io.buff_d = Mock()
        self.mock_gs.io.buffer = Mock()
        self.mock_gs.io.buff_cr = Mock()
        self.mock_gs.io.buff_no_cr = Mock()
        self.mock_gs.core = Mock()
        self.mock_gs.core.hero = Mock()
    
    def test_examine_simple_item(self):
        """Test examining an item with no writing or containers"""
        # Call examine
        self.simple_item.examine(self.mock_gs)
        
        # Verify buff_d was called with correct parameters
        self.mock_gs.io.buff_d.assert_called_once_with('stone_desc', 'Gray Stone')
        
        # Verify no additional formatting methods were called
        self.mock_gs.io.buff_cr.assert_not_called()
    
    def test_examine_item_with_writing(self):
        """Test examining an item that has writing"""
        # Call examine
        self.item_with_writing.examine(self.mock_gs)
        
        # Verify buff_d was called for main description
        self.mock_gs.io.buff_d.assert_called_once_with('tablet_desc', 'Stone Tablet')
        
        # Verify additional formatting was called (since it has writing)
        self.assertEqual(self.mock_gs.io.buff_cr.call_count, 2)  # Called twice for formatting
    
    def test_examine_writing_object(self):
        """Test examining a Writing object directly"""
        # Call examine on Writing object
        self.writing.examine(self.mock_gs)
        
        # Verify buff_d was called
        self.mock_gs.io.buff_d.assert_called_once_with('runes_desc', 'Ancient Runes')


class TestExamineMethodIntegration(unittest.TestCase):
    """Integration tests for examine() method with realistic scenarios"""
    
    def setUp(self):
        """Set up more realistic test fixtures"""
        # Create mock GameState with call tracking
        self.mock_gs = Mock()
        self.mock_gs.io = Mock()
        self.mock_gs.core = Mock()
        self.mock_gs.core.hero = Mock()
        
        # Track all method calls
        self.method_calls = []
        
        def track_buff_d(desc_key, full_name):
            self.method_calls.append(('buff_d', desc_key, full_name))
        
        def track_buffer(text):
            self.method_calls.append(('buffer', text))
        
        def track_buff_cr():
            self.method_calls.append(('buff_cr',))
        
        def track_buff_no_cr(text):
            self.method_calls.append(('buff_no_cr', text))
        
        self.mock_gs.io.buff_d.side_effect = track_buff_d
        self.mock_gs.io.buffer.side_effect = track_buffer
        self.mock_gs.io.buff_cr.side_effect = track_buff_cr
        self.mock_gs.io.buff_no_cr.side_effect = track_buff_no_cr
        
        # Create test objects
        self.writing = Writing('scroll_text', 'Scroll Text', 'text', 'scroll_text_desc')
        self.readable_book = ViewOnly('book', 'Ancient Book', 'book', 'book_desc', self.writing)
        self.plain_rock = ViewOnly('rock', 'Plain Rock', 'rock', 'rock_desc', None)
    
    def test_examine_sequence_simple_item(self):
        """Test the exact sequence of calls for examining a simple item"""
        # Examine simple item
        self.plain_rock.examine(self.mock_gs)
        
        # Verify exact call sequence
        expected_calls = [
            ('buff_d', 'rock_desc', 'Plain Rock')
        ]
        self.assertEqual(self.method_calls, expected_calls)
    
    def test_examine_sequence_item_with_writing(self):
        """Test the exact sequence of calls for examining an item with writing"""
        # Examine item with writing
        self.readable_book.examine(self.mock_gs)
        
        # Verify call sequence includes formatting for writing
        self.assertTrue(any(call[0] == 'buff_d' and call[1] == 'book_desc' for call in self.method_calls))
        self.assertTrue(any(call[0] == 'buff_cr' for call in self.method_calls))
        self.assertTrue(any(call[0] == 'buff_no_cr' and 'Ancient Book' in call[1] for call in self.method_calls))
    
    def test_examine_multiple_objects(self):
        """Test examining multiple objects in sequence"""
        # Clear previous calls
        self.method_calls.clear()
        
        # Examine both objects
        self.plain_rock.examine(self.mock_gs)
        self.readable_book.examine(self.mock_gs)
        
        # Verify both objects were processed
        buff_d_calls = [call for call in self.method_calls if call[0] == 'buff_d']
        self.assertEqual(len(buff_d_calls), 2)
        
        # Verify correct descriptions were called
        desc_keys = [call[1] for call in buff_d_calls]
        self.assertIn('rock_desc', desc_keys)
        self.assertIn('book_desc', desc_keys)


if __name__ == '__main__':
    unittest.main()