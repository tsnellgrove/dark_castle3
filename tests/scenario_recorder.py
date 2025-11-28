#!/usr/bin/env python3
"""
Scenario Recorder - Record gameplay sessions to create test scenarios
"""

import sys
import os
import json
import datetime
from pathlib import Path

# Add the project root to the path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from cleesh.app_main.app_main import app_main
from cleesh.app_main.start_up import start_me_up


class ScenarioRecorder:
    """Records gameplay sessions for creating test scenarios"""
    
    def __init__(self, game_name="dark_castle"):
        self.game_name = game_name
        self.root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.recording = []
        self.is_recording = False
        
    def start_recording(self, scenario_name=None):
        """Start recording a new scenario"""
        if scenario_name is None:
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            scenario_name = f"recorded_scenario_{timestamp}"
        
        self.scenario_name = scenario_name
        self.recording = []
        self.is_recording = True
        
        # Start fresh game
        print("🎬 Starting scenario recording...")
        print(f"📝 Scenario name: {scenario_name}")
        print("🎮 Starting fresh game...")
        
        startup_output = start_me_up(self.game_name, self.root_path)
        print(startup_output)
        
        print("\n" + "="*60)
        print("🔴 RECORDING STARTED")
        print("Type 'STOP_RECORDING' to finish and save scenario")
        print("Type 'CANCEL_RECORDING' to cancel without saving")
        print("="*60 + "\n")
        
    def record_command(self, user_input):
        """Record a single command and its output"""
        if not self.is_recording:
            return None, None, None, None, None
            
        # Handle recording control commands
        if user_input.upper() == 'STOP_RECORDING':
            return self.stop_recording()
        elif user_input.upper() == 'CANCEL_RECORDING':
            return self.cancel_recording()
        
        # Execute command and capture output
        is_start, is_end, game_ending, is_bkstry, output = app_main(
            user_input, self.game_name, self.root_path
        )
        
        # Record the command and output
        self.recording.append({
            "command": user_input,
            "output": output,
            "is_end": is_end
        })
        
        return is_start, is_end, game_ending, is_bkstry, output
    
    def stop_recording(self):
        """Stop recording and save scenario"""
        if not self.is_recording:
            print("❌ No recording in progress")
            return None, None, None, None, None
            
        self.is_recording = False
        
        print("\n" + "="*60)
        print("⏹️  RECORDING STOPPED")
        print("="*60)
        
        # Show recording summary
        print(f"\n📊 Recorded {len(self.recording)} commands:")
        for i, entry in enumerate(self.recording, 1):
            print(f"  {i}. {entry['command']}")
        
        # Get scenario details from user
        print(f"\n📝 Creating scenario file...")
        description = input("Enter scenario description (optional): ").strip()
        if not description:
            description = f"Recorded gameplay scenario from {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}"
        
        # Create scenario data
        scenario_data = {
            "name": self.scenario_name,
            "description": description,
            "commands": [entry["command"] for entry in self.recording],
            "recorded_outputs": [entry["output"] for entry in self.recording],
            "expected_outputs": [],
            "should_not_contain": ["error", "crash", "traceback"],
            "should_end": any(entry["is_end"] for entry in self.recording)
        }
        
        # Save scenario file
        scenario_dir = os.path.join(os.path.dirname(__file__), "game_test_data", "scenarios")
        os.makedirs(scenario_dir, exist_ok=True)
        
        scenario_file = os.path.join(scenario_dir, f"{self.scenario_name}.json")
        with open(scenario_file, 'w') as f:
            json.dump(scenario_data, f, indent=2)
        
        print(f"✅ Scenario saved to: {scenario_file}")
        print(f"\n💡 To use this scenario in tests:")
        print(f"   1. Edit {scenario_file}")
        print(f"   2. Add expected text to 'expected_outputs' array")
        print(f"   3. Run: python3 tests/run_game_tests.py")
        
        return None, True, "recording_stopped", False, "Recording completed successfully."
    
    def cancel_recording(self):
        """Cancel recording without saving"""
        self.is_recording = False
        self.recording = []
        
        print("\n" + "="*60)
        print("❌ RECORDING CANCELLED")
        print("="*60)
        
        return None, True, "recording_cancelled", False, "Recording cancelled."


def interactive_recorder():
    """Interactive recording session"""
    recorder = ScenarioRecorder()
    
    print("🎬 Dark Castle Scenario Recorder")
    print("=" * 40)
    
    scenario_name = input("Enter scenario name (or press Enter for auto-generated): ").strip()
    if not scenario_name:
        scenario_name = None
    
    recorder.start_recording(scenario_name)
    
    try:
        while recorder.is_recording:
            user_input = input("> ").strip()
            
            if not user_input:
                continue
                
            is_start, is_end, game_ending, is_bkstry, output = recorder.record_command(user_input)
            
            if output:
                print(output)
            
            if is_end and recorder.is_recording:
                print("\n🎮 Game ended. Recording will stop after next command.")
                
    except KeyboardInterrupt:
        print("\n\n⚠️  Recording interrupted by user")
        recorder.cancel_recording()
    except Exception as e:
        print(f"\n❌ Error during recording: {e}")
        recorder.cancel_recording()


if __name__ == '__main__':
    interactive_recorder()