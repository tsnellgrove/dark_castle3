#!/bin/bash
# Complete Scenario Workflow Script

echo "🎮 Dark Castle Scenario Workflow"
echo "================================="
echo ""
echo "Choose an option:"
echo "1. Record new scenario"
echo "2. Convert recorded scenarios"
echo "3. List all scenarios"
echo "4. Run all tests"
echo "5. Exit"
echo ""

read -p "Enter choice (1-5): " choice

case $choice in
    1)
        echo ""
        echo "🎬 Starting scenario recording..."
        ./record_scenario.sh
        ;;
    2)
        echo ""
        echo "🔄 Converting recorded scenarios..."
        python3 tests/scenario_converter.py
        ;;
    3)
        echo ""
        echo "📋 Listing all scenarios..."
        python3 list_scenarios.py
        ;;
    4)
        echo ""
        echo "🧪 Running all tests..."
        python3 tests/run_game_tests.py
        ;;
    5)
        echo "👋 Goodbye!"
        exit 0
        ;;
    *)
        echo "❌ Invalid choice"
        exit 1
        ;;
esac