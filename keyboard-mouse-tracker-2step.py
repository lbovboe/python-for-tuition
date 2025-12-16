#!/usr/bin/env python3
"""
Keyboard and Mouse Tracker - Two-Step Recording Version
A Python program that records TWO separate sequences of keyboard and mouse activities 
and can replay them in sequence with custom repetition counts.

Requirements:
pip install pynput

Usage:
- Press 1 to start two-step recording (record sequence 1, then sequence 2)
- Press 2 to replay both sequences once
- Press 3 to save both recordings to file
- Press 4 to load both recordings from file
- Press 5 to loop replay (continuous cycle: sequence 1 x N times, then sequence 2 x M times, repeat)
- Press 6 to stop current replay/loop
- Press ESC to exit
"""

import json
import time
import threading
from datetime import datetime
from pynput import mouse, keyboard
from pynput.mouse import Button, Listener as MouseListener
from pynput.keyboard import Key, Listener as KeyboardListener


class TwoStepMouseKeyboardTracker:
    def __init__(self):
        self.recording = False
        self.playing = False
        self.looping = False
        self.recording_step = 0  # 0 = not recording, 1 = recording first, 2 = recording second
        self.accepting_input = False  # Flag to ignore control keys during input prompts
        
        self.events_step1 = []
        self.events_step2 = []
        self.repeat_count_step1 = 1
        self.repeat_count_step2 = 1
        
        self.current_events = []
        self.start_time = None
        
        # Listeners
        self.mouse_listener = None
        self.keyboard_listener = None
        
        print("Keyboard and Mouse Tracker - Two-Step Version")
        print("=" * 50)
        print("Controls:")
        print("1 - Start Two-Step Recording")
        print("    (Records Sequence 1, then Sequence 2)")
        print("2 - Replay Both Sequences Once")
        print("3 - Save Both Recordings")
        print("4 - Load Both Recordings")
        print("5 - Loop Replay (Continuous Cycle)")
        print("6 - Stop Current Replay/Loop")
        print("ESC - Exit")
        print("=" * 50)
    
    def start_two_step_recording(self):
        """Start the two-step recording process"""
        if self.playing:
            print("Cannot start recording while playing back!")
            return
        
        self.recording_step = 1
        self.start_recording_step(1)
    
    def start_recording_step(self, step):
        """Start recording for a specific step"""
        self.recording = True
        self.current_events = []
        self.start_time = time.time()
        
        print(f"\n🔴 RECORDING STEP {step} STARTED at {datetime.now().strftime('%H:%M:%S')}")
        print(f"Perform your actions for sequence {step}...")
        print("Press 1 again to stop recording this step...")
        
        # Start mouse and keyboard listeners
        self.mouse_listener = MouseListener(
            on_move=self.on_mouse_move,
            on_click=self.on_mouse_click,
            on_scroll=self.on_mouse_scroll
        )
        
        self.mouse_listener.start()
    
    def stop_recording_step(self):
        """Stop recording current step and prompt for next action"""
        if not self.recording:
            return
        
        self.recording = False
        
        if self.mouse_listener:
            self.mouse_listener.stop()
            self.mouse_listener = None
        
        print(f"⏹️  RECORDING STEP {self.recording_step} STOPPED - Captured {len(self.current_events)} events")
        
        # Store events for current step
        if self.recording_step == 1:
            self.events_step1 = self.current_events.copy()
            
            # Ask for repeat count for step 1
            print("\n" + "=" * 50)
            self.accepting_input = True  # Disable control key handling during input
            try:
                count = input(f"How many times should Sequence 1 repeat? (default: 1): ").strip()
                self.repeat_count_step1 = int(count) if count and count.isdigit() else 1
                print(f"✓ Sequence 1 will repeat {self.repeat_count_step1} time(s)")
            except ValueError:
                self.repeat_count_step1 = 1
                print(f"✓ Using default: Sequence 1 will repeat 1 time")
            finally:
                time.sleep(0.3)  # Wait for any pending key events to be processed
                self.accepting_input = False  # Re-enable control key handling
            
            # Start recording step 2
            print("\n" + "=" * 50)
            print("Ready to record Sequence 2...")
            print("Press 1 to start recording Sequence 2")
            self.recording_step = 2
            
        elif self.recording_step == 2:
            self.events_step2 = self.current_events.copy()
            
            # Step 2 defaults to 1 time (no prompt needed)
            self.repeat_count_step2 = 1
            print(f"\n✓ Sequence 2 will repeat 1 time (default)")
            
            # Recording complete
            self.recording_step = 0
            print("\n" + "=" * 50)
            print("✅ TWO-STEP RECORDING COMPLETE!")
            print(f"   Sequence 1: {len(self.events_step1)} events × {self.repeat_count_step1} repetition(s)")
            print(f"   Sequence 2: {len(self.events_step2)} events × {self.repeat_count_step2} repetition(s)")
            print("=" * 50)
            print("Press 2 to replay once, or 5 to loop continuously")
    
    def on_mouse_move(self, x, y):
        """Record mouse movement"""
        if self.recording:
            event = {
                'type': 'mouse_move',
                'x': x,
                'y': y,
                'timestamp': time.time() - self.start_time
            }
            self.current_events.append(event)
    
    def on_mouse_click(self, x, y, button, pressed):
        """Record mouse clicks"""
        if self.recording:
            event = {
                'type': 'mouse_click',
                'x': x,
                'y': y,
                'button': button.name,
                'pressed': pressed,
                'timestamp': time.time() - self.start_time
            }
            self.current_events.append(event)
    
    def on_mouse_scroll(self, x, y, dx, dy):
        """Record mouse scroll"""
        if self.recording:
            event = {
                'type': 'mouse_scroll',
                'x': x,
                'y': y,
                'dx': dx,
                'dy': dy,
                'timestamp': time.time() - self.start_time
            }
            self.current_events.append(event)
    
    def on_key_press(self, key):
        """Record key presses"""
        if self.recording:
            try:
                key_name = key.char if hasattr(key, 'char') else None
                if key_name is None:
                    key_name = key.name if hasattr(key, 'name') else str(key)
            except AttributeError:
                key_name = str(key)
            
            event = {
                'type': 'key_press',
                'key': key_name,
                'timestamp': time.time() - self.start_time
            }
            self.current_events.append(event)
    
    def on_key_release(self, key):
        """Record key releases and handle control keys"""
        if self.recording:
            try:
                key_name = key.char if hasattr(key, 'char') else None
                if key_name is None:
                    key_name = key.name if hasattr(key, 'name') else str(key)
            except AttributeError:
                key_name = str(key)
            
            event = {
                'type': 'key_release',
                'key': key_name,
                'timestamp': time.time() - self.start_time
            }
            self.current_events.append(event)
        
        # Handle control keys (number keys 1-6) only if not accepting input
        if self.accepting_input:
            return  # Ignore all control keys during input prompts
        
        try:
            key_char = key.char if hasattr(key, 'char') else None
        except AttributeError:
            key_char = None
        
        if key_char == '1':
            if self.recording:
                self.stop_recording_step()
            elif self.recording_step == 0:
                # Start new two-step recording
                self.start_two_step_recording()
            elif self.recording_step == 2:
                # Start recording step 2
                self.start_recording_step(2)
        elif key_char == '2':
            if not self.recording and not self.playing:
                self.replay_events()
        elif key_char == '3':
            if not self.recording and (self.events_step1 or self.events_step2):
                self.save_recording()
        elif key_char == '4':
            if not self.recording and not self.playing:
                self.load_recording()
        elif key_char == '5':
            if not self.recording and not self.playing:
                self.loop_replay()
        elif key_char == '6':
            self.stop_replay()
        elif key == Key.esc:
            print("\nExiting...")
            return False  # Stop listener
    
    def replay_events(self):
        """Replay both recorded sequences once"""
        if not self.events_step1 and not self.events_step2:
            print("No events recorded! Press 1 to start two-step recording.")
            return
        
        if self.recording:
            print("Cannot replay while recording!")
            return
        
        self.playing = True
        print(f"\n▶️  REPLAYING BOTH SEQUENCES...")
        print(f"   First: ALL Sequence 1 repetitions ({self.repeat_count_step1}×)")
        print(f"   Then: ALL Sequence 2 repetitions ({self.repeat_count_step2}×)")
        
        # Run replay in separate thread to avoid blocking
        replay_thread = threading.Thread(target=self._replay_thread)
        replay_thread.daemon = True
        replay_thread.start()
    
    def loop_replay(self):
        """Continuously replay both sequences until stopped"""
        if not self.events_step1 and not self.events_step2:
            print("No events recorded! Press 1 to start two-step recording.")
            return
        
        if self.recording:
            print("Cannot replay while recording!")
            return
        
        self.playing = True
        self.looping = True
        print(f"\n🔄 LOOPING REPLAY of both sequences...")
        print(f"   Each cycle:")
        print(f"      1. Complete ALL Sequence 1 repetitions ({self.repeat_count_step1}×)")
        print(f"      2. Complete ALL Sequence 2 repetitions ({self.repeat_count_step2}×)")
        print(f"      3. Repeat from step 1")
        print("Press 6 to stop the loop...")
        
        # Run replay in separate thread to avoid blocking
        replay_thread = threading.Thread(target=self._loop_replay_thread)
        replay_thread.daemon = True
        replay_thread.start()
    
    def stop_replay(self):
        """Stop current replay or loop"""
        if self.playing:
            self.playing = False
            self.looping = False
            print("\n⏹️  REPLAY STOPPED")
        else:
            print("No replay in progress")
    
    def _loop_replay_thread(self):
        """Thread function for looping replay"""
        cycle_count = 0
        while self.looping and self.playing:
            cycle_count += 1
            print(f"\n🔄 Cycle {cycle_count}")
            self._execute_both_sequences()
            if self.looping:
                time.sleep(0.5)  # Small delay between cycles
        
        self.playing = False
        self.looping = False
        print(f"\n✅ LOOP COMPLETED ({cycle_count} cycle(s))")
    
    def _execute_both_sequences(self):
        """Execute both sequences with their respective repeat counts"""
        # Execute sequence 1 ALL times first
        if self.events_step1:
            print(f"  📍 Starting Sequence 1 ({self.repeat_count_step1} repetition(s))")
            for i in range(self.repeat_count_step1):
                if not self.playing:
                    break
                print(f"     Sequence 1, repetition {i+1}/{self.repeat_count_step1}")
                self._execute_events(self.events_step1)
                if i < self.repeat_count_step1 - 1 and self.playing:
                    time.sleep(0.1)  # Small delay between repetitions
        
        # Then execute sequence 2 ALL times
        if self.events_step2 and self.playing:
            print(f"  📍 Starting Sequence 2 ({self.repeat_count_step2} repetition(s))")
            for i in range(self.repeat_count_step2):
                if not self.playing:
                    break
                print(f"     Sequence 2, repetition {i+1}/{self.repeat_count_step2}")
                self._execute_events(self.events_step2)
                if i < self.repeat_count_step2 - 1 and self.playing:
                    time.sleep(0.1)  # Small delay between repetitions
    
    def _execute_events(self, events):
        """Execute a sequence of events with proper timing"""
        from pynput.mouse import Button as MouseButton
        from pynput.keyboard import Key as KeyboardKey
        
        mouse_controller = mouse.Controller()
        keyboard_controller = keyboard.Controller()
        
        try:
            last_timestamp = 0
            
            for event in events:
                if not self.playing:  # Allow interruption
                    break
                
                # Wait for the appropriate time delay
                time_delay = event['timestamp'] - last_timestamp
                if time_delay > 0:
                    time.sleep(time_delay)
                
                # Execute the event
                if event['type'] == 'mouse_move':
                    mouse_controller.position = (event['x'], event['y'])
                
                elif event['type'] == 'mouse_click':
                    button = MouseButton.left if event['button'] == 'left' else MouseButton.right
                    if event['pressed']:
                        mouse_controller.press(button)
                    else:
                        mouse_controller.release(button)
                
                elif event['type'] == 'mouse_scroll':
                    mouse_controller.scroll(event['dx'], event['dy'])
                
                elif event['type'] == 'key_press':
                    try:
                        key_value = event['key']
                        if key_value and isinstance(key_value, str) and len(key_value) == 1:
                            keyboard_controller.press(key_value)
                        else:
                            # Handle special keys
                            key = getattr(KeyboardKey, key_value, None)
                            if key:
                                keyboard_controller.press(key)
                    except Exception as e:
                        print(f"[WARNING] Failed to replay key press: {event.get('key')} - {e}")
                
                elif event['type'] == 'key_release':
                    try:
                        key_value = event['key']
                        if key_value and isinstance(key_value, str) and len(key_value) == 1:
                            keyboard_controller.release(key_value)
                        else:
                            key = getattr(KeyboardKey, key_value, None)
                            if key:
                                keyboard_controller.release(key)
                    except Exception as e:
                        print(f"[WARNING] Failed to replay key release: {event.get('key')} - {e}")
                
                last_timestamp = event['timestamp']
        
        except Exception as e:
            print(f"Error during execution: {e}")
    
    def _replay_thread(self):
        """Thread function for replaying both sequences once"""
        try:
            self._execute_both_sequences()
        finally:
            self.playing = False
            print("\n✅ REPLAY COMPLETED")
    
    def save_recording(self, filename=None):
        """Save both recordings to JSON file"""
        if not self.events_step1 and not self.events_step2:
            print("No events to save!")
            return
        
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"recording_2step_{timestamp}.json"
        
        try:
            with open(filename, 'w') as f:
                json.dump({
                    'step1': {
                        'events': self.events_step1,
                        'repeat_count': self.repeat_count_step1,
                        'total_events': len(self.events_step1),
                        'duration': self.events_step1[-1]['timestamp'] if self.events_step1 else 0
                    },
                    'step2': {
                        'events': self.events_step2,
                        'repeat_count': self.repeat_count_step2,
                        'total_events': len(self.events_step2),
                        'duration': self.events_step2[-1]['timestamp'] if self.events_step2 else 0
                    },
                    'created': datetime.now().isoformat()
                }, f, indent=2)
            
            print(f"\n💾 Recording saved to: {filename}")
            print(f"   Sequence 1: {len(self.events_step1)} events × {self.repeat_count_step1} repetition(s)")
            if self.events_step1:
                print(f"      Duration: {self.events_step1[-1]['timestamp']:.2f} seconds")
            print(f"   Sequence 2: {len(self.events_step2)} events × {self.repeat_count_step2} repetition(s)")
            if self.events_step2:
                print(f"      Duration: {self.events_step2[-1]['timestamp']:.2f} seconds")
        
        except Exception as e:
            print(f"Error saving recording: {e}")
    
    def load_recording(self, filename=None):
        """Load both recordings from JSON file"""
        if filename is None:
            self.accepting_input = True  # Disable control key handling during input
            try:
                filename = input("Enter filename to load (or press Enter for default): ").strip()
                if not filename:
                    # Try to find most recent 2-step recording
                    import glob
                    files = glob.glob("recording_2step_*.json")
                    if files:
                        filename = max(files, key=lambda x: x)
                        print(f"Using most recent file: {filename}")
                    else:
                        filename = "recording_2step.json"
            finally:
                time.sleep(0.3)  # Wait for any pending key events to be processed
                self.accepting_input = False  # Re-enable control key handling
        
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            
            self.events_step1 = data['step1']['events']
            self.repeat_count_step1 = data['step1']['repeat_count']
            
            self.events_step2 = data['step2']['events']
            self.repeat_count_step2 = data['step2']['repeat_count']
            
            print(f"\n📁 Recording loaded from: {filename}")
            print(f"   Sequence 1: {len(self.events_step1)} events × {self.repeat_count_step1} repetition(s)")
            print(f"      Duration: {data['step1'].get('duration', 0):.2f} seconds")
            print(f"   Sequence 2: {len(self.events_step2)} events × {self.repeat_count_step2} repetition(s)")
            print(f"      Duration: {data['step2'].get('duration', 0):.2f} seconds")
            print("\nPress 2 to replay once, or 5 to loop continuously")
        
        except FileNotFoundError:
            print(f"File not found: {filename}")
        except Exception as e:
            print(f"Error loading recording: {e}")
    
    def run(self):
        """Start the tracker"""
        # Start keyboard listener for control keys
        with KeyboardListener(
            on_press=self.on_key_press,
            on_release=self.on_key_release
        ) as listener:
            try:
                listener.join()
            except KeyboardInterrupt:
                print("\nProgram interrupted")


if __name__ == "__main__":
    tracker = TwoStepMouseKeyboardTracker()
    try:
        tracker.run()
    except KeyboardInterrupt:
        print("\nProgram terminated by user")
    except Exception as e:
        print(f"Error: {e}")
        print("Make sure you have installed the required dependencies:")
        print("pip install pynput")

