#!/usr/bin/env python3
"""
Game Test Harness - End-to-end testing for Dark Castle text adventure
"""

import unittest
import sys
import os
import json
import shutil
from pathlib import Path

# Add the project root to the path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from cleesh.app_main.app_main import app_main
from cleesh.app_main.start_up import start_me_up


class GameTestHarness(unittest.TestCase):
    """End-to-end game testing framework"""
    
    def setUp(self):
        """Set up test environment"""
        self.game_name = "dark_castle"
        self.root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.test_data_dir = os.path.join(os.path.dirname(__file__), "game_test_data")
        
        # Ensure test data directory exists
        os.makedirs(self.test_data_dir, exist_ok=True)
        
        # Backup original game state
        self.backup_game_state()
        
        # Start fresh game
        start_me_up(self.game_name, self.root_path)
    
    def tearDown(self):
        """Clean up after test"""
        # Restore original game state
        self.restore_game_state()
    
    def backup_game_state(self):
        """Backup the current game state"""
        working_dir = f"{self.root_path}/cleesh/games/{self.game_name}/working"
        backup_dir = f"{self.test_data_dir}/backup"
        
        if os.path.exists(working_dir):
            if os.path.exists(backup_dir):
                shutil.rmtree(backup_dir)
            shutil.copytree(working_dir, backup_dir)
    
    def restore_game_state(self):
        """Restore the original game state"""
        working_dir = f"{self.root_path}/cleesh/games/{self.game_name}/working"
        backup_dir = f"{self.test_data_dir}/backup"
        
        if os.path.exists(backup_dir):
            if os.path.exists(working_dir):
                shutil.rmtree(working_dir)
            shutil.copytree(backup_dir, working_dir)
    
    def run_command_sequence(self, commands):
        """
        Run a sequence of commands and return all outputs
        
        Args:
            commands: List of command strings
            
        Returns:
            List of (command, output, is_end) tuples
        """
        results = []
        
        for command in commands:
            is_start, is_end, game_ending, is_bkstry, output = app_main(
                command, self.game_name, self.root_path
            )
            
            results.append((command, output, is_end))
            
            # Stop if game ended
            if is_end:
                break
        
        return results
    
    def assert_output_contains(self, output, expected_text, msg=None):
        """Assert that output contains expected text (case insensitive)"""
        self.assertIn(expected_text.lower(), output.lower(), msg)
    
    def assert_output_not_contains(self, output, unexpected_text, msg=None):
        """Assert that output does not contain unexpected text (case insensitive)"""
        self.assertNotIn(unexpected_text.lower(), output.lower(), msg)


class TestBasicGameplay(GameTestHarness):
    """Test basic game functionality"""
    
    def test_game_startup(self):
        """Test that game starts correctly"""
        results = self.run_command_sequence(["look"])
        
        command, output, is_end = results[0]
        
        # Should not end immediately
        self.assertFalse(is_end)
        
        # Should contain welcome text and room description
        self.assert_output_contains(output, "entrance")
        self.assert_output_contains(output, "you")
    
    def test_basic_movement(self):
        """Test basic movement commands"""
        commands = ["look", "up", "look", "down"]
        results = self.run_command_sequence(commands)
        
        # Should have 4 results
        self.assertEqual(len(results), 4)
        
        # Check movement worked
        look1_output = results[0][1]
        up_output = results[1][1]
        look2_output = results[2][1]
        down_output = results[3][1]
        
        # After going up, should be in different room
        self.assertNotEqual(look1_output.lower(), look2_output.lower())
    
    def test_inventory_commands(self):
        """Test inventory-related commands"""
        commands = ["inventory", "i"]
        results = self.run_command_sequence(commands)
        
        for command, output, is_end in results:
            self.assertFalse(is_end)
            # Should mention inventory or items
            self.assertTrue(
                "inventory" in output.lower() or 
                "carrying" in output.lower() or
                "have" in output.lower()
            )
    
    def test_examine_commands(self):
        """Test examine functionality"""
        commands = ["look", "examine me", "x me"]
        results = self.run_command_sequence(commands)
        
        for command, output, is_end in results:
            self.assertFalse(is_end)
            # Should produce some output
            self.assertGreater(len(output.strip()), 0)
    
    def test_invalid_commands(self):
        """Test handling of invalid commands"""
        commands = ["xyzzy", "asdfgh", ""]
        results = self.run_command_sequence(commands)
        
        for command, output, is_end in results:
            self.assertFalse(is_end)
            # Should produce error message
            self.assertGreater(len(output.strip()), 0)
    
    def test_quit_command(self):
        """Test quit functionality"""
        commands = ["quit"]
        results = self.run_command_sequence(commands)
        
        command, output, is_end = results[0]
        
        # Should end the game
        self.assertTrue(is_end)
        self.assert_output_contains(output, "quit")


class TestSpecificScenarios(GameTestHarness):
    """Test specific game scenarios"""
    
    def test_entrance_exploration(self):
        """Test exploring the entrance area"""
        commands = [
            "look",
            "examine entrance",
            "north",
            "look",
            "south",
            "look"
        ]
        results = self.run_command_sequence(commands)
        
        # Should complete all commands without ending
        self.assertEqual(len(results), 6)
        for command, output, is_end in results:
            self.assertFalse(is_end, f"Game ended unexpectedly on command: {command}")
    
    def test_help_system(self):
        """Test help commands if they exist"""
        commands = ["help", "?"]
        results = self.run_command_sequence(commands)
        
        # Should not crash the game
        for command, output, is_end in results:
            self.assertFalse(is_end)


def load_test_scenario(scenario_file):
    """
    Load a test scenario from JSON file
    
    Expected format:
    {
        "name": "Test Name",
        "description": "Test description",
        "commands": ["command1", "command2"],
        "expected_outputs": ["text1", "text2"],
        "should_not_contain": ["error1", "error2"],
        "should_end": false
    }
    """
    with open(scenario_file, 'r') as f:
        return json.load(f)


class TestFromScenarioFiles(GameTestHarness):
    """Test scenarios loaded from JSON files"""
    
    def test_scenario_files(self):
        """Run all scenario files in test_data directory"""
        scenario_dir = os.path.join(self.test_data_dir, "scenarios")
        
        if not os.path.exists(scenario_dir):
            self.skipTest("No scenario files found")
        
        scenario_files = [f for f in os.listdir(scenario_dir) if f.endswith('.json')]
        
        if not scenario_files:
            self.skipTest("No scenario files found")
        
        print(f"\n📋 Testing {len(scenario_files)} scenarios:")
        for scenario_file in scenario_files:
            scenario_path = os.path.join(scenario_dir, scenario_file)
            with open(scenario_path, 'r') as f:
                scenario = json.load(f)
            print(f"  • {scenario['name']} ({scenario_file})")
        
        for scenario_file in scenario_files:
            with self.subTest(scenario=scenario_file):
                self.run_scenario_file(os.path.join(scenario_dir, scenario_file))
    
    def run_scenario_file(self, scenario_path):
        """Run a single scenario file"""
        scenario = load_test_scenario(scenario_path)
        
        print(f"\n🎮 Running scenario: {scenario['name']}")
        print(f"   Commands: {len(scenario['commands'])}")
        print(f"   Expected outputs: {len(scenario.get('expected_outputs', []))}")
        
        # Start fresh for each scenario
        start_me_up(self.game_name, self.root_path)
        
        results = self.run_command_sequence(scenario["commands"])
        
        # Check if game should have ended
        final_is_end = results[-1][2] if results else False
        expected_end = scenario.get("should_end", False)
        self.assertEqual(final_is_end, expected_end, 
                        f"Game end state mismatch in {scenario['name']}")
        
        # Combine all outputs for checking
        all_output = " ".join([result[1] for result in results])
        
        # Check expected outputs
        for expected in scenario.get("expected_outputs", []):
            self.assert_output_contains(all_output, expected, 
                                      f"Missing expected text in {scenario['name']}: {expected}")
        
        # Check unwanted outputs
        for unwanted in scenario.get("should_not_contain", []):
            self.assert_output_not_contains(all_output, unwanted,
                                          f"Found unwanted text in {scenario['name']}: {unwanted}")
        
        print(f"   ✅ Scenario '{scenario['name']}' passed")


if __name__ == '__main__':
    # Create sample scenario file
    test_data_dir = os.path.join(os.path.dirname(__file__), "game_test_data", "scenarios")
    os.makedirs(test_data_dir, exist_ok=True)
    
    sample_scenario = {
        "name": "Basic Movement Test",
        "description": "Test basic movement and room descriptions",
        "commands": ["look", "north", "look", "south", "look"],
        "expected_outputs": ["entrance", "you"],
        "should_not_contain": ["error", "crash"],
        "should_end": False
    }
    
    with open(os.path.join(test_data_dir, "basic_movement.json"), 'w') as f:
        json.dump(sample_scenario, f, indent=2)
    
    unittest.main()