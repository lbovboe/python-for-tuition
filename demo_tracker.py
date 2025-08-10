#!/usr/bin/env python3
"""
Demo script for the Keyboard and Mouse Tracker
This script provides a simple test program to demonstrate the tracker functionality.
"""

import time
import sys
import os

# Add the current directory to path to import our tracker
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    # Import the module with hyphenated name using importlib
    import importlib.util
    spec = importlib.util.spec_from_file_location("keyboard_mouse_tracker", "keyboard-mouse-tracker.py")
    tracker_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(tracker_module)
    MouseKeyboardTracker = tracker_module.MouseKeyboardTracker
except ImportError:
    print("Error: Could not import MouseKeyboardTracker")
    print("Make sure you have installed the required dependencies:")
    print("pip install pynput")
    sys.exit(1)


def main():
    print("🖱️ Keyboard and Mouse Tracker Demo")
    print("=" * 50)
    print()
    print("This demo will show you how to use the tracker:")
    print()
    print("1. First, start recording by pressing 1")
    print("2. Perform some mouse movements and clicks")
    print("3. Type some text on the keyboard")
    print("4. Stop recording by pressing 1 again")
    print("5. Replay your actions by pressing 2")
    print("6. Save your recording with 3")
    print("7. Try loop replay with 5")
    print("8. Stop loop with 6")
    print()
    print("Ready to start? Press any key to begin...")
    input()
    
    # Create and run the tracker
    tracker = MouseKeyboardTracker()
    print("\n🚀 Starting tracker... Use the number keys 1-6 as shown above!")
    
    try:
        tracker.run()
    except KeyboardInterrupt:
        print("\n👋 Demo ended by user")
    except Exception as e:
        print(f"❌ Error occurred: {e}")
        print("\nTroubleshooting:")
        print("1. Make sure you have installed: pip install pynput")
        print("2. On macOS, you may need to grant accessibility permissions")
        print("3. Try running with sudo if needed")


if __name__ == "__main__":
    main()