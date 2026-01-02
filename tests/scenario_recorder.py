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
    
    def __init__(self, game_name="dark_castle", locked_mode=False, verbosity_mode="verbose"):
        self.game_name = game_name
        self.root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.recording = []
        self.is_recording = False
        self.locked_mode = locked_mode
        self.verbosity_mode = verbosity_mode
        
    def start_recording(self, scenario_name=None):
        """Start recording a new scenario"""
        if scenario_name is None:
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            mode_suffix = "_locked" if self.locked_mode else ""
            verbosity_suffix = f"_{self.verbosity_mode}" if self.verbosity_mode != "verbose" else ""
            scenario_name = f"recorded_scenario_{timestamp}{mode_suffix}{verbosity_suffix}"
        
        self.scenario_name = scenario_name
        self.recording = []
        self.is_recording = True
        
        # Start fresh game
        print("🎬 Starting scenario recording...")
        print(f"📝 Scenario name: {scenario_name}")
        print(f"🎯 Mode: {'Locked (deterministic)' if self.locked_mode else 'Random'}")
        print(f"📖 Verbosity: {self.verbosity_mode}")
        print("🎮 Starting fresh game...")
        
        rand_mode = 'locked' if self.locked_mode else 'random'
        startup_output = start_me_up(self.game_name, self.root_path, rand_mode)
        print(startup_output)
        
        # Set verbosity mode if not verbose
        if self.verbosity_mode != "verbose":
            print(f"\n🔧 Setting verbosity to {self.verbosity_mode}...")
            _, _, _, _, verbosity_output = app_main(self.verbosity_mode, self.game_name, self.root_path)
            print(verbosity_output)
        
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
            "game_name": self.game_name,
            "commands": [entry["command"] for entry in self.recording],
            "mode": "locked" if self.locked_mode else "random",
            "verbosity_mode": self.verbosity_mode,
            "should_not_contain": ["crash", "traceback"],
            "should_end": any(entry["is_end"] for entry in self.recording)
        }
        
        if self.locked_mode:
            # For locked mode, store exact outputs for rigorous comparison
            scenario_data["expected_full_outputs"] = [entry["output"] for entry in self.recording]
        else:
            # For random mode, use flexible phrase matching
            scenario_data["recorded_outputs"] = [entry["output"] for entry in self.recording]
            scenario_data["expected_outputs"] = []
        
        # Save scenario file
        scenario_dir = os.path.join(os.path.dirname(__file__), "game_test_data", "scenarios", self.game_name)
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
    print("🎬 Cleesh Game Engine Scenario Recorder")
    print("=" * 40)
    
    # Choose game
    print("\nAvailable games:")
    print("  1. dark_castle - A classic Zork-like adventure")
    print("  2. cup_of_tea - Simple test game")
    
    game_choice = input("Choose game (1-2, default=1): ").strip()
    games = {"1": "dark_castle", "2": "cup_of_tea"}
    game_name = games.get(game_choice, "dark_castle")
    
    # Choose mode
    mode_choice = input("\nRecord in locked mode for rigorous testing? (y/N): ").strip().lower()
    locked_mode = mode_choice in ['y', 'yes']
    
    # Choose verbosity mode
    print("\nVerbosity modes:")
    print("  1. verbose (default) - Full room descriptions")
    print("  2. brief - Full descriptions only on first visit")
    print("  3. superbrief - Minimal descriptions")
    
    verbosity_choice = input("Choose verbosity mode (1-3, default=1): ").strip()
    verbosity_modes = {"1": "verbose", "2": "brief", "3": "superbrief"}
    verbosity_mode = verbosity_modes.get(verbosity_choice, "verbose")
    
    recorder = ScenarioRecorder(game_name=game_name, locked_mode=locked_mode, verbosity_mode=verbosity_mode)
    
    scenario_name = input("\nEnter scenario name (or press Enter for auto-generated): ").strip()
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