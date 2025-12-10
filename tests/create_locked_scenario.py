#!/usr/bin/env python3
"""
Create Locked Mode Scenario - Generate rigorous test scenarios for locked mode
"""

import sys
import os
import json
from pathlib import Path

# Add the project root to the path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from cleesh.app_main.app_main import app_main
from cleesh.app_main.start_up import start_me_up


def create_locked_scenario(commands, scenario_name, description=""):
    """
    Create a locked-mode scenario from a list of commands
    
    Args:
        commands: List of command strings
        scenario_name: Name for the scenario
        description: Optional description
    
    Returns:
        Dictionary containing the scenario data
    """
    game_name = "dark_castle"
    root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    print(f"🎯 Creating locked scenario: {scenario_name}")
    print(f"📝 Commands: {commands}")
    
    # Start game in locked mode
    start_me_up(game_name, root_path, 'locked')
    
    # Execute commands and capture outputs
    results = []
    for i, command in enumerate(commands):
        print(f"   Executing {i+1}/{len(commands)}: '{command}'")
        
        is_start, is_end, game_ending, is_bkstry, output = app_main(
            command, game_name, root_path
        )
        
        results.append({
            "command": command,
            "output": output,
            "is_end": is_end
        })
        
        if is_end:
            print(f"   Game ended: {game_ending}")
            break
    
    # Create scenario data
    scenario_data = {
        "name": scenario_name,
        "description": description or f"Locked mode test for {scenario_name}",
        "commands": [r["command"] for r in results],
        "mode": "locked",
        "expected_full_outputs": [r["output"] for r in results],
        "should_not_contain": ["error", "crash", "traceback"],
        "should_end": any(r["is_end"] for r in results)
    }
    
    print(f"✅ Scenario created with {len(results)} command/output pairs")
    return scenario_data


def save_scenario(scenario_data, filename=None):
    """Save scenario to JSON file"""
    if filename is None:
        filename = f"{scenario_data['name'].lower().replace(' ', '_')}.json"
    
    scenario_dir = os.path.join(os.path.dirname(__file__), "game_test_data", "scenarios")
    os.makedirs(scenario_dir, exist_ok=True)
    
    filepath = os.path.join(scenario_dir, filename)
    
    with open(filepath, 'w') as f:
        json.dump(scenario_data, f, indent=2)
    
    print(f"💾 Scenario saved to: {filepath}")
    return filepath


def create_predefined_scenarios():
    """Create a set of predefined locked-mode scenarios"""
    
    scenarios = [
        {
            "name": "Basic Entrance Exploration",
            "description": "Test basic commands in the entrance area",
            "commands": ["look", "inventory", "examine postbox", "open postbox", "examine certificate"]
        },
        {
            "name": "Tree Climbing Sequence", 
            "description": "Test climbing the tree and getting the ruby",
            "commands": ["look", "up", "look", "examine hollow", "take ruby", "down"]
        },
        {
            "name": "Gate Opening Sequence",
            "description": "Test opening the front gate with the rusty key",
            "commands": ["look", "unlock gate with rusty key", "open gate", "north"]
        },
        {
            "name": "Sword Acquisition",
            "description": "Test getting the shiny sword from the gatehouse",
            "commands": ["north", "look", "take sword", "examine sword"]
        },
        {
            "name": "Simple Combat Test",
            "description": "Test basic combat with the guard goblin",
            "commands": ["north", "take sword", "north", "attack goblin with sword"]
        }
    ]
    
    created_scenarios = []
    
    for scenario_info in scenarios:
        try:
            scenario_data = create_locked_scenario(
                scenario_info["commands"],
                scenario_info["name"], 
                scenario_info["description"]
            )
            
            filepath = save_scenario(scenario_data)
            created_scenarios.append(filepath)
            
        except Exception as e:
            print(f"❌ Failed to create scenario '{scenario_info['name']}': {e}")
    
    return created_scenarios


def interactive_scenario_creator():
    """Interactive scenario creation"""
    print("🎯 Locked Mode Scenario Creator")
    print("=" * 40)
    
    scenario_name = input("Enter scenario name: ").strip()
    if not scenario_name:
        print("❌ Scenario name is required")
        return
    
    description = input("Enter description (optional): ").strip()
    
    print("\nEnter commands (one per line, empty line to finish):")
    commands = []
    while True:
        command = input(f"Command {len(commands)+1}: ").strip()
        if not command:
            break
        commands.append(command)
    
    if not commands:
        print("❌ At least one command is required")
        return
    
    try:
        scenario_data = create_locked_scenario(commands, scenario_name, description)
        filepath = save_scenario(scenario_data)
        print(f"\n🎉 Successfully created scenario: {filepath}")
        
    except Exception as e:
        print(f"❌ Failed to create scenario: {e}")


if __name__ == '__main__':
    import argparse
    
    parser = argparse.ArgumentParser(description='Create locked-mode test scenarios')
    parser.add_argument('--predefined', action='store_true', 
                       help='Create predefined scenarios')
    parser.add_argument('--interactive', action='store_true',
                       help='Interactive scenario creation')
    
    args = parser.parse_args()
    
    if args.predefined:
        print("🏭 Creating predefined scenarios...")
        created = create_predefined_scenarios()
        print(f"\n🎉 Created {len(created)} scenarios")
        
    elif args.interactive:
        interactive_scenario_creator()
        
    else:
        print("Usage:")
        print("  python3 create_locked_scenario.py --predefined")
        print("  python3 create_locked_scenario.py --interactive")