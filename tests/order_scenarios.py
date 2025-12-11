#!/usr/bin/env python3
"""
Order Scenarios - Change the order scenarios are run in
"""

import os
import json


def load_test_order():
    """Load existing test order configuration"""
    order_file = os.path.join(os.path.dirname(__file__), "game_test_data", "test_order.json")
    
    if os.path.exists(order_file):
        with open(order_file, 'r') as f:
            return json.load(f)
    
    return {"order": []}


def save_test_order(order_config):
    """Save test order configuration"""
    test_data_dir = os.path.join(os.path.dirname(__file__), "game_test_data")
    os.makedirs(test_data_dir, exist_ok=True)
    
    order_file = os.path.join(test_data_dir, "test_order.json")
    
    with open(order_file, 'w') as f:
        json.dump(order_config, f, indent=2)


def get_available_scenarios():
    """Get list of all available scenario files"""
    scenario_dir = os.path.join(os.path.dirname(__file__), "game_test_data", "scenarios")
    
    if not os.path.exists(scenario_dir):
        return []
    
    scenario_files = [f for f in os.listdir(scenario_dir) if f.endswith('.json')]
    
    scenarios = []
    for scenario_file in sorted(scenario_files):
        scenario_path = os.path.join(scenario_dir, scenario_file)
        
        try:
            with open(scenario_path, 'r') as f:
                scenario = json.load(f)
            
            name = scenario.get('name', 'Unnamed')
            scenarios.append((scenario_file, name))
            
        except Exception:
            scenarios.append((scenario_file, scenario_file))
    
    return scenarios


def display_current_order():
    """Display current test order"""
    order_config = load_test_order()
    available_scenarios = get_available_scenarios()
    
    if not available_scenarios:
        print("📋 No scenarios found")
        return [], []
    
    ordered_scenarios = []
    unordered_scenarios = []
    
    # Get scenarios in specified order
    for filename in order_config.get("order", []):
        for scenario_file, name in available_scenarios:
            if scenario_file == filename:
                ordered_scenarios.append((scenario_file, name))
                break
    
    # Get scenarios not in order (new ones)
    ordered_files = [f for f, _ in ordered_scenarios]
    for scenario_file, name in available_scenarios:
        if scenario_file not in ordered_files:
            unordered_scenarios.append((scenario_file, name))
    
    print("📋 Current Test Order:")
    
    if ordered_scenarios:
        print("\n🔢 Ordered scenarios:")
        for i, (filename, name) in enumerate(ordered_scenarios, 1):
            print(f"  {i}. {name} ({filename})")
    
    if unordered_scenarios:
        print("\n❓ Unordered scenarios (will run after ordered ones):")
        for filename, name in unordered_scenarios:
            print(f"  • {name} ({filename})")
    
    if not ordered_scenarios and not unordered_scenarios:
        print("  (No scenarios found)")
    
    return ordered_scenarios, unordered_scenarios


def reorder_scenarios():
    """Interactive scenario reordering"""
    print("🔢 Reorder Test Scenarios")
    print("=" * 30)
    
    ordered_scenarios, unordered_scenarios = display_current_order()
    all_scenarios = ordered_scenarios + unordered_scenarios
    
    if not all_scenarios:
        return
    
    print(f"\n📝 Available scenarios:")
    for i, (filename, name) in enumerate(all_scenarios, 1):
        print(f"  {i}. {name} ({filename})")
    
    print("\nEnter the order you want scenarios to run in.")
    print("Type scenario numbers separated by spaces (e.g., '3 1 4 2')")
    print("Leave blank to keep current order, or type 'reset' to use alphabetical order.")
    
    try:
        user_input = input("\nNew order: ").strip()
        
        if not user_input:
            print("❌ Order unchanged")
            return
        
        if user_input.lower() == 'reset':
            # Reset to alphabetical order
            new_order = [filename for filename, _ in sorted(all_scenarios, key=lambda x: x[1].lower())]
        else:
            # Parse user input
            indices = [int(x.strip()) - 1 for x in user_input.split()]
            
            # Validate indices
            if any(i < 0 or i >= len(all_scenarios) for i in indices):
                print("❌ Invalid scenario numbers")
                return
            
            if len(set(indices)) != len(indices):
                print("❌ Duplicate scenario numbers")
                return
            
            # Create new order
            new_order = [all_scenarios[i][0] for i in indices]
            
            # Add any scenarios not specified to the end
            specified_files = set(new_order)
            for filename, _ in all_scenarios:
                if filename not in specified_files:
                    new_order.append(filename)
        
        # Save new order
        order_config = {"order": new_order}
        save_test_order(order_config)
        
        print("\n✅ Test order updated!")
        print("\n📋 New order:")
        for i, filename in enumerate(new_order, 1):
            # Find name for this filename
            name = next((name for f, name in all_scenarios if f == filename), filename)
            print(f"  {i}. {name} ({filename})")
        
    except ValueError:
        print("❌ Invalid input. Please enter numbers separated by spaces.")
    except Exception as e:
        print(f"❌ Error updating order: {e}")


if __name__ == '__main__':
    reorder_scenarios()