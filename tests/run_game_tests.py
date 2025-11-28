#!/usr/bin/env python3
"""
Game Test Runner - Run comprehensive game tests before commits
"""

import unittest
import sys
import os
import time

# Add the project root to the path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import json


def show_available_scenarios():
    """Show available test scenarios"""
    scenario_dir = os.path.join(os.path.dirname(__file__), "game_test_data", "scenarios")
    
    if not os.path.exists(scenario_dir):
        print("📋 No scenarios directory found")
        return
    
    scenario_files = [f for f in os.listdir(scenario_dir) if f.endswith('.json')]
    
    if not scenario_files:
        print("📋 No scenario files found")
        return
    
    print(f"📋 Found {len(scenario_files)} test scenarios:")
    
    for scenario_file in sorted(scenario_files):
        scenario_path = os.path.join(scenario_dir, scenario_file)
        try:
            with open(scenario_path, 'r') as f:
                scenario = json.load(f)
            
            name = scenario.get('name', 'Unnamed')
            commands = len(scenario.get('commands', []))
            expected = len(scenario.get('expected_outputs', []))
            
            print(f"  • {name} - {commands} commands, {expected} expectations")
            
        except Exception as e:
            print(f"  • {scenario_file} - Error loading: {e}")
    
    print()


def run_all_tests():
    """Run all game tests"""
    print("=" * 60)
    print("DARK CASTLE - COMPREHENSIVE GAME TESTING")
    print("=" * 60)
    
    # Show available scenarios
    show_available_scenarios()
    
    start_time = time.time()
    
    # Discover and run all tests
    loader = unittest.TestLoader()
    suite = loader.discover('tests', pattern='test_game_*.py')
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    end_time = time.time()
    
    print("\n" + "=" * 60)
    print(f"TESTING COMPLETE - {end_time - start_time:.2f} seconds")
    print(f"Tests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    
    if result.failures:
        print("\n❌ FAILURES:")
        for test, traceback in result.failures:
            # Extract scenario name if it's a scenario test
            if 'scenario=' in str(test):
                scenario_match = str(test).split('scenario=')[1].split(')')[0].strip("'\"")
                print(f"- Scenario '{scenario_match}': {traceback.split('AssertionError:')[-1].strip()}")
            else:
                print(f"- {test}: {traceback.split('AssertionError:')[-1].strip()}")
    
    if result.errors:
        print("\n⚠️ ERRORS:")
        for test, traceback in result.errors:
            if 'scenario=' in str(test):
                scenario_match = str(test).split('scenario=')[1].split(')')[0].strip("'\"")
                print(f"- Scenario '{scenario_match}': {traceback.split('Exception:')[-1].strip()}")
            else:
                print(f"- {test}: {traceback.split('Exception:')[-1].strip()}")
    
    success = len(result.failures) == 0 and len(result.errors) == 0
    
    # Count scenario tests
    scenario_tests = sum(1 for test, _ in result.failures + result.errors if 'scenario=' in str(test))
    total_scenarios = len([f for f in os.listdir(os.path.join(os.path.dirname(__file__), "game_test_data", "scenarios")) if f.endswith('.json')]) if os.path.exists(os.path.join(os.path.dirname(__file__), "game_test_data", "scenarios")) else 0
    
    if success:
        print(f"\n✅ ALL TESTS PASSED - READY FOR COMMIT!")
        if total_scenarios > 0:
            print(f"🎮 All {total_scenarios} scenarios passed")
    else:
        print(f"\n❌ TESTS FAILED - DO NOT COMMIT!")
        if scenario_tests > 0:
            print(f"🎮 {scenario_tests} scenario(s) failed out of {total_scenarios}")
    
    print("=" * 60)
    
    return success


if __name__ == '__main__':
    success = run_all_tests()
    sys.exit(0 if success else 1)