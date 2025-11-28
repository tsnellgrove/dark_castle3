#!/usr/bin/env python3
"""
List Test Scenarios - Show all available test scenarios
"""

import os
import json
from pathlib import Path


def list_scenarios():
    """List all available test scenarios with details"""
    scenario_dir = os.path.join(os.path.dirname(__file__), "tests", "game_test_data", "scenarios")
    
    if not os.path.exists(scenario_dir):
        print("❌ No scenarios directory found")
        return
    
    scenario_files = [f for f in os.listdir(scenario_dir) if f.endswith('.json')]
    
    if not scenario_files:
        print("📋 No scenario files found")
        return
    
    print("🎮 Dark Castle Test Scenarios")
    print("=" * 40)
    print(f"📊 Total scenarios: {len(scenario_files)}")
    print()
    
    for i, scenario_file in enumerate(sorted(scenario_files), 1):
        scenario_path = os.path.join(scenario_dir, scenario_file)
        
        try:
            with open(scenario_path, 'r') as f:
                scenario = json.load(f)
            
            name = scenario.get('name', 'Unnamed')
            description = scenario.get('description', 'No description')
            commands = scenario.get('commands', [])
            expected = scenario.get('expected_outputs', [])
            should_end = scenario.get('should_end', False)
            
            print(f"{i}. {name}")
            print(f"   📁 File: {scenario_file}")
            print(f"   📝 Description: {description}")
            print(f"   🎯 Commands: {len(commands)}")
            print(f"   ✅ Expectations: {len(expected)}")
            print(f"   🏁 Should end game: {'Yes' if should_end else 'No'}")
            
            if commands:
                print(f"   🎮 First command: '{commands[0]}'")
                if len(commands) > 1:
                    print(f"   🎮 Last command: '{commands[-1]}'")
            
            # Check if it needs conversion (has recorded_outputs)
            if 'recorded_outputs' in scenario:
                print("   ⚠️  Needs conversion (has recorded_outputs)")
            
            print()
            
        except Exception as e:
            print(f"{i}. {scenario_file}")
            print(f"   ❌ Error loading: {e}")
            print()


if __name__ == '__main__':
    list_scenarios()