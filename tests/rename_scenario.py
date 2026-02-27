#!/usr/bin/env python3
"""
Rename Scenario - Rename test scenarios
"""

import os
import json
import shutil


def list_scenarios():
    """List all available scenarios for renaming"""
    base_scenario_dir = os.path.join(os.path.dirname(__file__), "game_test_data", "scenarios")
    
    if not os.path.exists(base_scenario_dir):
        print("❌ No scenarios directory found")
        return []
    
    # Find all game directories
    game_dirs = [d for d in os.listdir(base_scenario_dir) 
                if os.path.isdir(os.path.join(base_scenario_dir, d))]
    
    if not game_dirs:
        print("📋 No game directories found")
        return []
    
    scenarios = []
    total_count = 0
    
    for game_name in sorted(game_dirs):
        game_scenario_dir = os.path.join(base_scenario_dir, game_name)
        scenario_files = [f for f in os.listdir(game_scenario_dir) if f.endswith('.json')]
        
        if scenario_files:
            print(f"\n🎮 {game_name.replace('_', ' ').title()}:")
            
            for scenario_file in sorted(scenario_files):
                scenario_path = os.path.join(game_scenario_dir, scenario_file)
                total_count += 1
                
                try:
                    with open(scenario_path, 'r') as f:
                        scenario = json.load(f)
                    
                    name = scenario.get('name', 'Unnamed')
                    mode = scenario.get('mode', 'random')
                    commands = len(scenario.get('commands', []))
                    
                    print(f"  {total_count}. {name} ({scenario_file}) - {mode} mode, {commands} commands")
                    scenarios.append((scenario_file, scenario_path, name, scenario, game_name))
                    
                except Exception as e:
                    print(f"  {total_count}. {scenario_file} - Error loading: {e}")
                    scenarios.append((scenario_file, scenario_path, scenario_file, None, game_name))
    
    print(f"\n📋 Total: {total_count} scenarios")
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
            scenario_file, scenario_path, current_name, scenario_data, game_name = scenarios[index]
            
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