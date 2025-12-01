#!/usr/bin/env python3
"""
Keyboard and Mouse Tracker
A Python program that records keyboard and mouse activities and can replay them.
Similar to TinyTask functionality.

Requirements:
pip install pynput

Usage:
- Press 1 to start/stop recording
- Press 2 to replay recorded actions once
- Press 3 to save recording to file
- Press 4 to load recording from file
- Press 5 to loop replay (continuous until stopped)
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


class MouseKeyboardTracker:
    def __init__(self):
        self.recording = False
        self.playing = False
        self.looping = False
        self.events = []
        self.start_time = None
        
        # Listeners
        self.mouse_listener = None
        self.keyboard_listener = None
        
        print("Keyboard and Mouse Tracker")
        print("=" * 40)
        print("Controls:")
        print("1 - Start/Stop Recording")
        print("2 - Replay Recording Once")
        print("3 - Save Recording")
        print("4 - Load Recording")
        print("5 - Loop Replay (Continuous)")
        print("6 - Stop Current Replay/Loop")
        print("ESC - Exit")
        print("=" * 40)
    
    def start_recording(self):
        """Start recording mouse and keyboard events"""
        if self.playing:
            print("Cannot start recording while playing back!")
            return
            
        self.recording = True
        self.events = []
        self.start_time = time.time()
        
        print(f"\n🔴 RECORDING STARTED at {datetime.now().strftime('%H:%M:%S')}")
        print("Press 1 again to stop recording...")
        
        # Start mouse and keyboard listeners
        self.mouse_listener = MouseListener(
            on_move=self.on_mouse_move,
            on_click=self.on_mouse_click,
            on_scroll=self.on_mouse_scroll
        )
        
        self.mouse_listener.start()
    
    def stop_recording(self):
        """Stop recording events"""
        if not self.recording:
            return
            
        self.recording = False
        
        if self.mouse_listener:
            self.mouse_listener.stop()
            self.mouse_listener = None
        
        print(f"⏹️  RECORDING STOPPED - Captured {len(self.events)} events")
        print("Press 2 to replay or 3 to save to file")
    
    def on_mouse_move(self, x, y):
        """Record mouse movement"""
        if self.recording:
            event = {
                'type': 'mouse_move',
                'x': x,
                'y': y,
                'timestamp': time.time() - self.start_time
            }
            self.events.append(event)
    
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
            self.events.append(event)
    
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
            self.events.append(event)
    
    def on_key_press(self, key):
        """Record key presses"""
        if self.recording:
            try:
                key_name = key.char
                if key_name is None:
                    key_name = key.name
            except AttributeError:
                key_name = key.name
            
            # Debug: print what key was detected
            print(f"[DEBUG] Key pressed detected: '{key_name}' (type: {type(key_name).__name__})")
            
            event = {
                'type': 'key_press',
                'key': key_name,
                'timestamp': time.time() - self.start_time
            }
            self.events.append(event)
    
    def on_key_release(self, key):
        """Record key releases and handle control keys"""
        if self.recording:
            try:
                key_name = key.char
                if key_name is None:
                    key_name = key.name
            except AttributeError:
                key_name = key.name
            
            event = {
                'type': 'key_release',
                'key': key_name,
                'timestamp': time.time() - self.start_time
            }
            self.events.append(event)
        
        # Handle control keys (number keys 1-6)
        try:
            key_char = key.char
            if key_char is None:
                key_char = None  # Keep as None if char is None
        except AttributeError:
            key_char = None
        
        if key_char == '1':
            if self.recording:
                self.stop_recording()
            else:
                self.start_recording()
        elif key_char == '2':
            if not self.recording and not self.playing:
                self.replay_events()
        elif key_char == '3':
            if not self.recording and self.events:
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
        """Replay recorded events"""
        if not self.events:
            print("No events recorded! Press 1 to start recording.")
            return
        
        if self.recording:
            print("Cannot replay while recording!")
            return
        
        self.playing = True
        print(f"\n▶️  REPLAYING {len(self.events)} events...")
        print("Events will be replayed with original timing...")
        
        # Run replay in separate thread to avoid blocking
        replay_thread = threading.Thread(target=self._replay_thread)
        replay_thread.daemon = True
        replay_thread.start()
    
    def loop_replay(self):
        """Continuously replay recorded events until stopped"""
        if not self.events:
            print("No events recorded! Press 1 to start recording.")
            return
        
        if self.recording:
            print("Cannot replay while recording!")
            return
        
        self.playing = True
        self.looping = True
        print(f"\n🔄 LOOPING REPLAY of {len(self.events)} events...")
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
        loop_count = 0
        while self.looping and self.playing:
            loop_count += 1
            print(f"🔄 Loop iteration {loop_count}")
            self._execute_events()
            if self.looping:
                time.sleep(0.5)  # Small delay between loops
        
        self.playing = False
        self.looping = False
        print(f"✅ LOOP COMPLETED ({loop_count} iterations)")
    
    def _execute_events(self):
        """Execute the recorded events with proper timing"""
        from pynput.mouse import Button as MouseButton
        from pynput.keyboard import Key as KeyboardKey
        
        mouse_controller = mouse.Controller()
        keyboard_controller = keyboard.Controller()
        
        try:
            last_timestamp = 0
            
            for event in self.events:
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
        """Thread function for replaying events once"""
        try:
            self._execute_events()
        finally:
            self.playing = False
            print("✅ REPLAY COMPLETED")
    
    def save_recording(self, filename=None):
        """Save recording to JSON file"""
        if not self.events:
            print("No events to save!")
            return
        
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"recording_{timestamp}.json"
        
        try:
            with open(filename, 'w') as f:
                json.dump({
                    'events': self.events,
                    'total_events': len(self.events),
                    'duration': self.events[-1]['timestamp'] if self.events else 0,
                    'created': datetime.now().isoformat()
                }, f, indent=2)
            
            print(f"💾 Recording saved to: {filename}")
            print(f"   Events: {len(self.events)}")
            print(f"   Duration: {self.events[-1]['timestamp']:.2f} seconds" if self.events else "   Duration: 0 seconds")
        
        except Exception as e:
            print(f"Error saving recording: {e}")
    
    def load_recording(self, filename=None):
        """Load recording from JSON file"""
        if filename is None:
            filename = input("Enter filename to load (or press Enter for default): ").strip()
            if not filename:
                filename = "recording.json"
        
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            
            self.events = data['events']
            print(f"📁 Recording loaded from: {filename}")
            print(f"   Events: {len(self.events)}")
            print(f"   Duration: {data.get('duration', 0):.2f} seconds")
            print("Press 2 to replay the loaded recording")
        
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
    tracker = MouseKeyboardTracker()
    try:
        tracker.run()
    except KeyboardInterrupt:
        print("\nProgram terminated by user")
    except Exception as e:
        print(f"Error: {e}")
        print("Make sure you have installed the required dependencies:")
        print("pip install pynput")
