#!/usr/bin/env python3
"""
Delete Scenario - Remove test scenarios
"""

import os
import json


def list_scenarios():
    """List all available scenarios for deletion"""
    scenario_dir = os.path.join(os.path.dirname(__file__), "game_test_data", "scenarios")
    
    if not os.path.exists(scenario_dir):
        print("❌ No scenarios directory found")
        return []
    
    scenario_files = [f for f in os.listdir(scenario_dir) if f.endswith('.json')]
    
    if not scenario_files:
        print("📋 No scenario files found")
        return []
    
    scenarios = []
    print(f"📋 Found {len(scenario_files)} scenarios:")
    
    for i, scenario_file in enumerate(sorted(scenario_files), 1):
        scenario_path = os.path.join(scenario_dir, scenario_file)
        
        try:
            with open(scenario_path, 'r') as f:
                scenario = json.load(f)
            
            name = scenario.get('name', 'Unnamed')
            mode = scenario.get('mode', 'random')
            commands = len(scenario.get('commands', []))
            
            print(f"  {i}. {name} ({scenario_file}) - {mode} mode, {commands} commands")
            scenarios.append((scenario_file, scenario_path, name))
            
        except Exception as e:
            print(f"  {i}. {scenario_file} - Error loading: {e}")
            scenarios.append((scenario_file, os.path.join(scenario_dir, scenario_file), scenario_file))
    
    return scenarios


def delete_scenario():
    """Interactive scenario deletion"""
    print("🗑️  Delete Scenario")
    print("=" * 20)
    
    scenarios = list_scenarios()
    
    if not scenarios:
        return
    
    print()
    
    try:
        choice = input("Enter scenario number to delete (or 'cancel'): ").strip()
        
        if choice.lower() == 'cancel':
            print("❌ Deletion cancelled")
            return
        
        index = int(choice) - 1
        if 0 <= index < len(scenarios):
            scenario_file, scenario_path, scenario_name = scenarios[index]
            
            # Confirm deletion
            confirm = input(f"⚠️  Delete '{scenario_name}' ({scenario_file})? (y/N): ").strip().lower()
            
            if confirm in ['y', 'yes']:
                os.remove(scenario_path)
                print(f"✅ Deleted scenario: {scenario_file}")
            else:
                print("❌ Deletion cancelled")
        else:
            print("❌ Invalid choice")
            
    except ValueError:
        print("❌ Invalid input")
    except Exception as e:
        print(f"❌ Error deleting scenario: {e}")


if __name__ == '__main__':
    delete_scenario()