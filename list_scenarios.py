#!/usr/bin/env python3
"""
List Test Scenarios - Show all available test scenarios
"""

import os
import json
from pathlib import Path


def list_scenarios():
    """List all available test scenarios with details"""
    base_scenario_dir = os.path.join(os.path.dirname(__file__), "tests", "game_test_data", "scenarios")
    
    if not os.path.exists(base_scenario_dir):
        print("❌ No scenarios directory found")
        return
    
    # Find all game directories
    game_dirs = [d for d in os.listdir(base_scenario_dir) 
                if os.path.isdir(os.path.join(base_scenario_dir, d))]
    
    if not game_dirs:
        print("📋 No game directories found")
        return
    
    total_scenarios = 0
    total_commands = 0
    
    print("🎮 Test Scenarios")
    print("=" * 40)
    
    for game_name in sorted(game_dirs):
        game_scenario_dir = os.path.join(base_scenario_dir, game_name)
        scenario_files = [f for f in os.listdir(game_scenario_dir) if f.endswith('.json')]
        
        if not scenario_files:
            continue
        
        print(f"\n🎮 {game_name.replace('_', ' ').title()}")
        print(f"📊 {len(scenario_files)} scenarios")
        print()
        
        for i, scenario_file in enumerate(sorted(scenario_files), 1):
            scenario_path = os.path.join(game_scenario_dir, scenario_file)
            
            try:
                with open(scenario_path, 'r') as f:
                    scenario = json.load(f)
                
                name = scenario.get('name', 'Unnamed')
                description = scenario.get('description', 'No description')
                commands = scenario.get('commands', [])
                mode = scenario.get('mode', 'random')
                expected = scenario.get('expected_outputs', [])
                expected_full = scenario.get('expected_full_outputs', [])
                should_end = scenario.get('should_end', False)
                
                total_scenarios += 1
                total_commands += len(commands)
                
                print(f"{i}. {name}")
                print(f"   📁 File: {scenario_file}")
                print(f"   📝 Description: {description}")
                print(f"   🎯 Commands: {len(commands)}")
                print(f"   🔒 Mode: {mode}")
                if mode == 'locked':
                    print(f"   ✅ Full output checks: {len(expected_full)}")
                else:
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
    
    print("=" * 40)
    print(f"📊 Total: {total_scenarios} scenarios, {total_commands} commands")


if __name__ == '__main__':
    list_scenarios()