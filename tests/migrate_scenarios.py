#!/usr/bin/env python3
"""
Scenario Migration Script - Move existing scenarios to game-specific directories
"""

import os
import json
import shutil
from pathlib import Path

def migrate_scenarios():
    """Migrate existing scenarios to game-specific directory structure"""
    
    # Paths
    test_dir = os.path.dirname(__file__)
    old_scenarios_dir = os.path.join(test_dir, "game_test_data", "scenarios")
    new_scenarios_dir = os.path.join(old_scenarios_dir, "dark_castle")
    
    print("🔄 Migrating scenarios to game-specific structure...")
    
    # Create dark_castle directory if it doesn't exist
    os.makedirs(new_scenarios_dir, exist_ok=True)
    
    # Find all JSON files in the old scenarios directory (not in subdirectories)
    json_files = []
    if os.path.exists(old_scenarios_dir):
        for file in os.listdir(old_scenarios_dir):
            if file.endswith('.json') and os.path.isfile(os.path.join(old_scenarios_dir, file)):
                json_files.append(file)
    
    if not json_files:
        print("ℹ️  No scenarios found to migrate")
        return
    
    print(f"📁 Found {len(json_files)} scenarios to migrate:")
    
    migrated_count = 0
    for filename in json_files:
        old_path = os.path.join(old_scenarios_dir, filename)
        new_path = os.path.join(new_scenarios_dir, filename)
        
        try:
            # Read the existing scenario
            with open(old_path, 'r') as f:
                scenario = json.load(f)
            
            # Add game_name if not present
            if 'game_name' not in scenario:
                scenario['game_name'] = 'dark_castle'
                print(f"  ✏️  {filename} - Added game_name field")
            
            # Write to new location
            with open(new_path, 'w') as f:
                json.dump(scenario, f, indent=2)
            
            # Remove old file
            os.remove(old_path)
            
            print(f"  ✅ {filename} - Migrated successfully")
            migrated_count += 1
            
        except Exception as e:
            print(f"  ❌ {filename} - Error: {e}")
    
    # Migrate test order file if it exists
    old_order_file = os.path.join(test_dir, "game_test_data", "test_order.json")
    new_order_file = os.path.join(test_dir, "game_test_data", "test_order_dark_castle.json")
    
    if os.path.exists(old_order_file):
        try:
            shutil.move(old_order_file, new_order_file)
            print(f"  ✅ test_order.json - Migrated to test_order_dark_castle.json")
        except Exception as e:
            print(f"  ❌ test_order.json - Error: {e}")
    
    print(f"\n🎉 Migration complete! {migrated_count} scenarios migrated to dark_castle directory")
    print(f"📂 New location: {new_scenarios_dir}")
    
    # Show final structure
    print(f"\n📋 Final structure:")
    if os.path.exists(new_scenarios_dir):
        scenarios = [f for f in os.listdir(new_scenarios_dir) if f.endswith('.json')]
        for scenario in sorted(scenarios):
            print(f"  • {scenario}")

if __name__ == '__main__':
    migrate_scenarios()