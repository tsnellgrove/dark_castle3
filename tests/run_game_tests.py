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


def count_scenarios_and_commands(selected_game=None):
    """Count total scenarios and commands that will be tested"""
    scenario_dir = os.path.join(os.path.dirname(__file__), "game_test_data", "scenarios")
    
    if not os.path.exists(scenario_dir):
        return 0, 0
    
    total_scenarios = 0
    total_commands = 0
    
    # Find all game directories
    game_dirs = [d for d in os.listdir(scenario_dir) 
                if os.path.isdir(os.path.join(scenario_dir, d))]
    
    # Apply game filter if specified
    if selected_game and selected_game != "all":
        game_dirs = [g for g in game_dirs if g == selected_game]
    
    for game_name in game_dirs:
        game_scenario_dir = os.path.join(scenario_dir, game_name)
        scenario_files = [f for f in os.listdir(game_scenario_dir) if f.endswith('.json')]
        
        for scenario_file in scenario_files:
            try:
                with open(os.path.join(game_scenario_dir, scenario_file), 'r') as f:
                    scenario = json.load(f)
                total_scenarios += 1
                total_commands += len(scenario.get('commands', []))
            except Exception:
                pass  # Skip invalid scenarios
    
    return total_scenarios, total_commands


def get_available_games():
    """Get list of available games with scenarios"""
    scenario_dir = os.path.join(os.path.dirname(__file__), "game_test_data", "scenarios")
    if not os.path.exists(scenario_dir):
        return []
    
    games = [d for d in os.listdir(scenario_dir) 
             if os.path.isdir(os.path.join(scenario_dir, d))]
    return sorted(games)


def select_game():
    """Allow user to select which game to test"""
    games = get_available_games()
    
    if not games:
        print("No games with scenarios found")
        return None
    
    if len(games) == 1:
        return games[0]
    
    print("\n🎮 Available games:")
    for i, game in enumerate(games, 1):
        print(f"  {i}. {game.replace('_', ' ').title()}")
    print(f"  {len(games) + 1}. All games")
    
    while True:
        try:
            choice = input(f"\nSelect game to test (1-{len(games) + 1}): ").strip()
            if not choice:
                continue
            
            choice_num = int(choice)
            if 1 <= choice_num <= len(games):
                return games[choice_num - 1]
            elif choice_num == len(games) + 1:
                return "all"
            else:
                print(f"Please enter a number between 1 and {len(games) + 1}")
        except (ValueError, KeyboardInterrupt):
            print("\nExiting...")
            return None


def run_all_tests(selected_game=None):
    """Run all game tests"""
    print("=" * 60)
    print("COMPREHENSIVE GAME TESTING")
    print("=" * 60)
    
    # Show available scenarios
    show_available_scenarios()
    
    start_time = time.time()
    
    # Set environment variable for game selection
    if selected_game and selected_game != "all":
        os.environ['TEST_GAME_FILTER'] = selected_game
        print(f"\n🎯 Testing only: {selected_game.replace('_', ' ').title()}")
    else:
        os.environ.pop('TEST_GAME_FILTER', None)
        print("\n🎯 Testing all games")
    
    # Count scenarios and commands before running tests
    scenario_count, command_count = count_scenarios_and_commands(selected_game)
    
    # Discover and run all tests
    loader = unittest.TestLoader()
    suite = loader.discover('tests', pattern='test_game_*.py')
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    end_time = time.time()
    
    print("\n" + "=" * 60)
    print(f"TESTING COMPLETE - {end_time - start_time:.2f} seconds")
    print(f"Tests run: {result.testsRun}")
    print(f"Scenarios tested: {scenario_count}")
    print(f"Commands run: {command_count}")
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
    # Check for command line arguments
    if len(sys.argv) > 1:
        game_arg = sys.argv[1]
        if game_arg in get_available_games():
            selected_game = game_arg
        elif game_arg == "all":
            selected_game = "all"
        else:
            print(f"Unknown game: {game_arg}")
            print(f"Available games: {', '.join(get_available_games())}")
            sys.exit(1)
    else:
        selected_game = select_game()
        if selected_game is None:
            sys.exit(1)
    
    success = run_all_tests(selected_game)
    sys.exit(0 if success else 1)