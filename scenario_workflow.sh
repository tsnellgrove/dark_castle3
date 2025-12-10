#!/bin/bash
# Complete Scenario Workflow Script

echo "🎮 Dark Castle Scenario Workflow"
echo "================================="
echo ""
echo "Choose an option:"
echo "1. Record new scenario (flexible)"
echo "2. Record locked-mode scenario (rigorous)"
echo "3. Create predefined locked scenarios"
echo "4. Convert recorded scenarios"
echo "5. List all scenarios"
echo "6. Delete a scenario"
echo "7. Run all tests"
echo "8. Exit"
echo ""

read -p "Enter choice (1-8): " choice

case $choice in
    1)
        echo ""
        echo "🎬 Starting scenario recording..."
        ./record_scenario.sh
        ;;
    2)
        echo ""
        echo "🎯 Recording locked-mode scenario..."
        echo "Note: This will record in deterministic mode for exact output matching"
        ./record_scenario.sh
        ;;
    3)
        echo ""
        echo "🏰 Creating predefined locked scenarios..."
        python3 tests/create_locked_scenario.py --predefined
        ;;
    4)
        echo ""
        echo "🔄 Converting recorded scenarios..."
        python3 tests/scenario_converter.py
        ;;
    5)
        echo ""
        echo "📋 Listing all scenarios..."
        python3 list_scenarios.py
        ;;
    6)
        echo ""
        echo "🗑️  Deleting scenario..."
        python3 tests/delete_scenario.py
        ;;
    7)
        echo ""
        echo "🧪 Running all tests..."
        python3 tests/run_game_tests.py
        ;;
    8)
        echo "👋 Goodbye!"
        exit 0
        ;;
    *)
        echo "❌ Invalid choice"
        exit 1
        ;;
esac