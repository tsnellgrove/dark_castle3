#!/usr/bin/env python3
"""
Rename Scenario - Rename test scenarios
"""

import os
import json
import shutil


def list_scenarios():
    """List all available scenarios for renaming"""
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
            scenarios.append((scenario_file, scenario_path, name, scenario))
            
        except Exception as e:
            print(f"  {i}. {scenario_file} - Error loading: {e}")
            scenarios.append((scenario_file, os.path.join(scenario_dir, scenario_file), scenario_file, None))
    
    return scenarios


def rename_scenario():
    """Interactive scenario renaming"""
    print("✏️  Rename Scenario")
    print("=" * 20)
    
    scenarios = list_scenarios()
    
    if not scenarios:
        return
    
    print()
    
    try:
        choice = input("Enter scenario number to rename (or 'cancel'): ").strip()
        
        if choice.lower() == 'cancel':
            print("❌ Rename cancelled")
            return
        
        index = int(choice) - 1
        if 0 <= index < len(scenarios):
            scenario_file, scenario_path, current_name, scenario_data = scenarios[index]
            
            if scenario_data is None:
                print("❌ Cannot rename corrupted scenario file")
                return
            
            print(f"\nCurrent name: {current_name}")
            print(f"Current file: {scenario_file}")
            
            # Get new name
            new_name = input("Enter new scenario name: ").strip()
            if not new_name:
                print("❌ Name cannot be empty")
                return
            
            # Get new filename (optional)
            suggested_filename = new_name.lower().replace(' ', '_').replace('-', '_') + '.json'
            new_filename = input(f"Enter new filename (or press Enter for '{suggested_filename}'): ").strip()
            
            if not new_filename:
                new_filename = suggested_filename
            
            if not new_filename.endswith('.json'):
                new_filename += '.json'
            
            # Check if new filename already exists
            scenario_dir = os.path.dirname(scenario_path)
            new_path = os.path.join(scenario_dir, new_filename)
            
            if os.path.exists(new_path) and new_path != scenario_path:
                print(f"❌ File '{new_filename}' already exists")
                return
            
            # Update scenario data
            scenario_data['name'] = new_name
            
            # Save with new name and filename
            with open(new_path, 'w') as f:
                json.dump(scenario_data, f, indent=2)
            
            # Remove old file if filename changed
            if new_path != scenario_path:
                os.remove(scenario_path)
                print(f"✅ Renamed scenario: '{current_name}' → '{new_name}'")
                print(f"✅ Renamed file: '{scenario_file}' → '{new_filename}'")
            else:
                print(f"✅ Renamed scenario: '{current_name}' → '{new_name}'")
            
        else:
            print("❌ Invalid choice")
            
    except ValueError:
        print("❌ Invalid input")
    except Exception as e:
        print(f"❌ Error renaming scenario: {e}")


if __name__ == '__main__':
    rename_scenario()