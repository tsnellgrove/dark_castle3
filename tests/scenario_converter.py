#!/usr/bin/env python3
"""
Scenario Converter - Convert recorded scenarios to test scenarios
"""

import json
import os
import re
from pathlib import Path


def extract_key_phrases(text):
    """Extract key phrases from game output for expected_outputs"""
    # Remove extra whitespace and newlines
    clean_text = re.sub(r'\s+', ' ', text.strip())
    
    # Extract room names (text between *** ***)
    room_matches = re.findall(r'\*\*\* (.*?) \*\*\*', clean_text)
    
    # Extract common game phrases
    key_phrases = []
    
    # Add room names
    key_phrases.extend(room_matches)
    
    # Look for inventory-related text
    if 'possess' in clean_text.lower():
        key_phrases.append('possess')
    
    # Look for movement confirmations
    if 'you go' in clean_text.lower():
        key_phrases.append('you go')
    
    # Look for examination results
    if any(word in clean_text.lower() for word in ['examine', 'look', 'see']):
        # Extract object names that appear after "you see" or similar
        see_matches = re.findall(r'you see:? (.*?)\.', clean_text, re.IGNORECASE)
        key_phrases.extend(see_matches)
    
    # Remove duplicates and empty strings
    return list(set([phrase.strip() for phrase in key_phrases if phrase.strip()]))


def convert_recorded_scenario(scenario_file):
    """Convert a recorded scenario to a proper test scenario"""
    
    with open(scenario_file, 'r') as f:
        scenario = json.load(f)
    
    print(f"📝 Converting scenario: {scenario['name']}")
    print(f"📊 Commands: {len(scenario['commands'])}")
    
    # Extract expected outputs from recorded outputs
    all_expected = []
    
    for i, output in enumerate(scenario.get('recorded_outputs', [])):
        command = scenario['commands'][i]
        key_phrases = extract_key_phrases(output)
        
        print(f"\n🔍 Command {i+1}: '{command}'")
        print(f"   Suggested expected outputs: {key_phrases}")
        
        # Ask user which phrases to include
        for phrase in key_phrases:
            include = input(f"   Include '{phrase}'? (y/n/enter=yes): ").strip().lower()
            if include in ['', 'y', 'yes']:
                all_expected.append(phrase)
    
    # Remove duplicates
    all_expected = list(set(all_expected))
    
    # Update scenario
    scenario['expected_outputs'] = all_expected
    
    # Remove recorded_outputs to clean up the file
    if 'recorded_outputs' in scenario:
        del scenario['recorded_outputs']
    
    # Save updated scenario
    with open(scenario_file, 'w') as f:
        json.dump(scenario, f, indent=2)
    
    print(f"\n✅ Scenario converted successfully!")
    print(f"📋 Final expected outputs: {all_expected}")
    print(f"💾 Saved to: {scenario_file}")


def list_recorded_scenarios():
    """List all recorded scenarios that need conversion"""
    scenario_dir = os.path.join(os.path.dirname(__file__), "game_test_data", "scenarios")
    
    if not os.path.exists(scenario_dir):
        print("❌ No scenarios directory found")
        return []
    
    recorded_scenarios = []
    
    for filename in os.listdir(scenario_dir):
        if filename.endswith('.json'):
            filepath = os.path.join(scenario_dir, filename)
            
            with open(filepath, 'r') as f:
                scenario = json.load(f)
            
            # Check if it has recorded_outputs (indicating it needs conversion)
            if 'recorded_outputs' in scenario:
                recorded_scenarios.append((filename, filepath, scenario))
    
    return recorded_scenarios


def interactive_converter():
    """Interactive scenario conversion"""
    print("🔄 Scenario Converter")
    print("=" * 30)
    
    recorded_scenarios = list_recorded_scenarios()
    
    if not recorded_scenarios:
        print("✅ No recorded scenarios found that need conversion")
        return
    
    print(f"📋 Found {len(recorded_scenarios)} recorded scenarios:")
    
    for i, (filename, filepath, scenario) in enumerate(recorded_scenarios, 1):
        print(f"  {i}. {scenario['name']} ({filename})")
    
    print()
    
    try:
        choice = input("Enter scenario number to convert (or 'all' for all): ").strip()
        
        if choice.lower() == 'all':
            for filename, filepath, scenario in recorded_scenarios:
                print(f"\n{'='*50}")
                convert_recorded_scenario(filepath)
        else:
            index = int(choice) - 1
            if 0 <= index < len(recorded_scenarios):
                filename, filepath, scenario = recorded_scenarios[index]
                convert_recorded_scenario(filepath)
            else:
                print("❌ Invalid choice")
                
    except ValueError:
        print("❌ Invalid input")
    except KeyboardInterrupt:
        print("\n⚠️  Conversion cancelled by user")


if __name__ == '__main__':
    interactive_converter()