#!/usr/bin/env python3
"""
Unit tests for Item class and subclasses
"""

import unittest
import sys
import os

# Add the project root to the path so we can import cleesh modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from cleesh.class_std.item_class_def import Item, Food, Liquid, Garment, Weapon
from cleesh.class_std.base_class_def import Writing


class TestItem(unittest.TestCase):
    """Test cases for the Item class"""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.test_item = Item('test_sword', 'Test Sword', 'sword', 'test_sword_desc', None, 5)
        self.test_writing = Writing('test_writing', 'Test Writing', 'writing', 'test_writing_desc')
        self.item_with_writing = Item('inscribed_ring', 'Inscribed Ring', 'ring', 'ring_desc', self.test_writing, 2)
    
    def test_item_creation(self):
        """Test that Item objects are created with correct attributes"""
        self.assertEqual(self.test_item.name, 'test_sword')
        self.assertEqual(self.test_item.full_name, 'Test Sword')
        self.assertEqual(self.test_item.root_name, 'sword')
        self.assertEqual(self.test_item.descript_key, 'test_sword_desc')
        self.assertEqual(self.test_item.writing, None)
        self.assertEqual(self.test_item.weight, 5)
    
    def test_item_with_writing(self):
        """Test Item with writing attribute"""
        self.assertEqual(self.item_with_writing.writing, self.test_writing)
        self.assertTrue(self.item_with_writing.has_writing())
    
    def test_weight_management(self):
        """Test weight increment and decrement methods"""
        original_weight = self.test_item.weight
        
        # Test increment
        self.test_item.increment_weight(3)
        self.assertEqual(self.test_item.weight, original_weight + 3)
        
        # Test decrement
        self.test_item.decrement_weight(2)
        self.assertEqual(self.test_item.weight, original_weight + 1)
    
    def test_identity_methods(self):
        """Test that Item identity methods return correct values"""
        self.assertTrue(self.test_item.is_item())
        self.assertFalse(self.test_item.is_liquid())
        self.assertFalse(self.test_item.is_food())
        self.assertFalse(self.test_item.is_garment())
        self.assertFalse(self.test_item.is_weapon())


class TestFood(unittest.TestCase):
    """Test cases for the Food class"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.test_food = Food('apple', 'Red Apple', 'apple', 'apple_desc', None, 1)
    
    def test_food_creation(self):
        """Test Food object creation"""
        self.assertEqual(self.test_food.name, 'apple')
        self.assertEqual(self.test_food.weight, 1)
    
    def test_food_identity(self):
        """Test Food identity methods"""
        self.assertTrue(self.test_food.is_item())
        self.assertTrue(self.test_food.is_food())
        self.assertFalse(self.test_food.is_liquid())


class TestLiquid(unittest.TestCase):
    """Test cases for the Liquid class"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.test_liquid = Liquid('water', 'Clear Water', 'water', 'water_desc', None, 1)
    
    def test_liquid_identity(self):
        """Test Liquid identity methods"""
        self.assertTrue(self.test_liquid.is_item())
        self.assertTrue(self.test_liquid.is_liquid())
        self.assertFalse(self.test_liquid.is_food())


class TestGarment(unittest.TestCase):
    """Test cases for the Garment class"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.test_garment = Garment('hat', 'Blue Hat', 'hat', 'hat_desc', None, 1, 'hat')
    
    def test_garment_creation(self):
        """Test Garment object creation with garment_type"""
        self.assertEqual(self.test_garment.garment_type, 'hat')
    
    def test_garment_identity(self):
        """Test Garment identity methods"""
        self.assertTrue(self.test_garment.is_item())
        self.assertTrue(self.test_garment.is_garment())
        self.assertFalse(self.test_garment.is_weapon())


class TestWeapon(unittest.TestCase):
    """Test cases for the Weapon class"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.attack_desc = [['slashes', 'quick strike'], ['stabs', 'powerful thrust']]
        self.test_weapon = Weapon('dagger', 'Sharp Dagger', 'dagger', 'dagger_desc', None, 3, self.attack_desc)
    
    def test_weapon_creation(self):
        """Test Weapon object creation with attack descriptions"""
        self.assertEqual(self.test_weapon.desc_lst, self.attack_desc)
    
    def test_weapon_identity(self):
        """Test Weapon identity methods"""
        self.assertTrue(self.test_weapon.is_item())
        self.assertTrue(self.test_weapon.is_weapon())
        self.assertFalse(self.test_weapon.is_garment())


if __name__ == '__main__':
    unittest.main()