#!/bin/bash
# Scenario Recording Script for Dark Castle
# Records gameplay sessions to create test scenarios

echo "🎬 Dark Castle Scenario Recorder"
echo "================================"
echo ""
echo "This will start a recording session where you can play the game"
echo "and automatically create a test scenario from your gameplay."
echo ""
echo "Commands during recording:"
echo "  STOP_RECORDING   - Save scenario and exit"
echo "  CANCEL_RECORDING - Cancel without saving"
echo ""

python3 tests/scenario_recorder.py