#!/bin/bash
# Pre-commit test script for Dark Castle
# Run this before any git commit or merge

echo "🧪 Running pre-commit tests..."
echo ""

# Run the comprehensive game tests
python3 tests/run_game_tests.py

# Check the exit code
if [ $? -eq 0 ]; then
    echo ""
    echo "✅ All tests passed! Safe to commit."
    exit 0
else
    echo ""
    echo "❌ Tests failed! Fix issues before committing."
    exit 1
fi