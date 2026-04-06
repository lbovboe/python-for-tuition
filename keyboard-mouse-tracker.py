#!/usr/bin/env python3
"""
Keyboard and Mouse Tracker
A Python program that records keyboard and mouse activities and can replay them.
Similar to TinyTask functionality.

Requirements:
pip install pynput

Usage:
- Press 1 to start/stop recording (prompts for filename to save when stopped)
- Press 2 to replay recorded actions once
- Press 3 to save current recording to a named file
- Press 4 to load a saved recording from file (can then use option 5)
- Press 5 to loop replay continuously until stopped
- Press 6 to stop current replay/loop (only key that works during loop)
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
        # State flags
        self.recording = False   # True while recording is active
        self.playing = False     # True while any replay (single or loop) is running
        self.looping = False     # True only during loop replay (option 5)

        self.events = []         # Holds all recorded events in memory
        self.start_time = None   # Reference timestamp for recording timing

        # Listeners for mouse input during recording
        self.mouse_listener = None
        self.keyboard_listener = None

        # Flag to prevent multiple simultaneous prompts (e.g. save dialog)
        self._prompting = False

        print("Keyboard and Mouse Tracker")
        print("=" * 40)
        print("Controls:")
        print("1 - Start / Stop Recording")
        print("    (on stop, you will be asked for a filename to save)")
        print("2 - Replay Recording Once")
        print("3 - Save Recording to Named File")
        print("4 - Load Recording from File")
        print("    (after loading, use 5 to loop-replay the file)")
        print("5 - Loop Replay (Continuous, only 6 can stop it)")
        print("6 - Stop Current Replay / Loop")
        print("ESC - Exit")
        print("=" * 40)

    # ------------------------------------------------------------------
    # FEATURE 1: Record
    # Start/stop recording with key 1.
    # On stop, the user is immediately prompted for a filename so the
    # recording is saved right away (no need to press 3 separately).
    # ------------------------------------------------------------------

    def start_recording(self):
        """Begin capturing all mouse and keyboard events."""
        if self.playing:
            print("Cannot start recording while a replay is running!")
            return

        self.recording = True
        self.events = []
        self.start_time = time.time()

        print(f"\n[REC] RECORDING STARTED at {datetime.now().strftime('%H:%M:%S')}")
        print("Press 1 again to stop recording...")

        # Start the mouse listener so mouse events are captured
        self.mouse_listener = MouseListener(
            on_move=self.on_mouse_move,
            on_click=self.on_mouse_click,
            on_scroll=self.on_mouse_scroll
        )
        self.mouse_listener.start()

    def stop_recording(self):
        """
        Stop capturing events, then immediately ask the user for a filename
        and auto-save the recording so nothing is lost.
        """
        if not self.recording:
            return

        self.recording = False

        # Stop the mouse listener
        if self.mouse_listener:
            self.mouse_listener.stop()
            self.mouse_listener = None

        print(f"\n[STOP] RECORDING STOPPED — captured {len(self.events)} events")

        # Automatically prompt for save so the user never loses a recording
        self._prompt_and_save()

    def _prompt_and_save(self):
        """
        Run the filename prompt in a background thread so it does not block
        the main keyboard listener while the user types.
        """
        if self._prompting:
            return  # Avoid overlapping prompts

        def _ask():
            self._prompting = True
            try:
                name = input("\nEnter a filename to save (without .json, e.g. my_macro): ").strip()
                if not name:
                    # Default name if the user just presses Enter
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    name = f"recording_{timestamp}"
                self.save_recording(filename=f"{name}.json")
            finally:
                self._prompting = False

        t = threading.Thread(target=_ask, daemon=True)
        t.start()

    # ------------------------------------------------------------------
    # Mouse event handlers — called by MouseListener during recording
    # ------------------------------------------------------------------

    def on_mouse_move(self, x, y):
        """Record the current mouse position as a timestamped event."""
        if self.recording:
            self.events.append({
                'type': 'mouse_move',
                'x': x,
                'y': y,
                'timestamp': time.time() - self.start_time
            })

    def on_mouse_click(self, x, y, button, pressed):
        """Record a mouse button press or release with position."""
        if self.recording:
            self.events.append({
                'type': 'mouse_click',
                'x': x,
                'y': y,
                'button': button.name,
                'pressed': pressed,
                'timestamp': time.time() - self.start_time
            })

    def on_mouse_scroll(self, x, y, dx, dy):
        """Record a scroll wheel movement with direction and distance."""
        if self.recording:
            self.events.append({
                'type': 'mouse_scroll',
                'x': x,
                'y': y,
                'dx': dx,
                'dy': dy,
                'timestamp': time.time() - self.start_time
            })

    # ------------------------------------------------------------------
    # Keyboard event handlers — called by the main KeyboardListener
    # ------------------------------------------------------------------

    def on_key_press(self, key):
        """
        Record a key press during recording.
        Control keys (1-6, ESC) are handled in on_key_release instead,
        so they are not accidentally included in macro recordings.
        """
        if self.recording:
            try:
                key_name = key.char if key.char is not None else key.name
            except AttributeError:
                key_name = key.name

            self.events.append({
                'type': 'key_press',
                'key': key_name,
                'timestamp': time.time() - self.start_time
            })

    def on_key_release(self, key):
        """
        Handle control keys on release.

        IMPORTANT: While option 5 (loop replay) is active, only key 6
        is allowed to take effect. Keys 1-4 are silently ignored so they
        cannot accidentally stop or interfere with the running loop.
        """
        # Record the key release event if we are currently recording
        if self.recording:
            try:
                key_name = key.char if key.char is not None else key.name
            except AttributeError:
                key_name = key.name

            self.events.append({
                'type': 'key_release',
                'key': key_name,
                'timestamp': time.time() - self.start_time
            })

        # Determine which character was pressed
        try:
            key_char = key.char
        except AttributeError:
            key_char = None

        # --- Key 6: Stop replay / loop ---
        # This is the ONLY key that works during loop replay (option 5).
        if key_char == '6':
            self.stop_replay()
            return

        # If loop replay is running, ignore all other number keys so they
        # do not accidentally trigger recording, single replay, save, or load.
        if self.looping:
            return

        # --- Key 1: Start / stop recording ---
        if key_char == '1':
            if self.recording:
                self.stop_recording()
            else:
                self.start_recording()

        # --- Key 2: Replay once (only when idle and events are loaded) ---
        elif key_char == '2':
            if not self.recording and not self.playing:
                self.replay_events()

        # --- Key 3: Manually save recording to a user-chosen filename ---
        # This is useful if the user wants to save again under a different name,
        # or if they loaded a file and want to save a modified version.
        elif key_char == '3':
            if not self.recording and self.events and not self._prompting:
                print("\n[SAVE] Saving current recording...")
                self._prompt_and_save()

        # --- Key 4: Load a previously saved recording ---
        # After loading, the user can immediately press 5 to loop-replay it.
        elif key_char == '4':
            if not self.recording and not self.playing and not self._prompting:
                self._prompt_and_load()

        # --- Key 5: Loop replay (runs until key 6 is pressed) ---
        elif key_char == '5':
            if not self.recording and not self.playing:
                self.loop_replay()

        # --- ESC: Exit the program ---
        elif key == Key.esc:
            print("\nExiting...")
            return False  # Returning False stops the KeyboardListener

    # ------------------------------------------------------------------
    # FEATURE 2: Replay once
    # Plays back the recorded (or loaded) events a single time.
    # ------------------------------------------------------------------

    def replay_events(self):
        """
        Replay all captured events exactly once with their original timing.
        Runs in a background thread so the main listener stays responsive.
        """
        if not self.events:
            print("No events to replay! Press 1 to record or 4 to load a file.")
            return

        self.playing = True
        print(f"\n[PLAY] REPLAYING {len(self.events)} events once...")

        replay_thread = threading.Thread(target=self._replay_thread, daemon=True)
        replay_thread.start()

    def _replay_thread(self):
        """Thread target: execute all events once, then clear the playing flag."""
        try:
            self._execute_events()
        finally:
            self.playing = False
            print("[DONE] REPLAY COMPLETED")

    # ------------------------------------------------------------------
    # FEATURE 3: Save recording to file (manual save via key 3)
    # The user types in the filename. Also called automatically after
    # recording stops (via _prompt_and_save).
    # ------------------------------------------------------------------

    def save_recording(self, filename=None):
        """
        Serialise the current event list to a JSON file.
        If filename is not provided it will be generated from the timestamp.
        """
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

            duration = self.events[-1]['timestamp'] if self.events else 0
            print(f"\n[SAVE] Recording saved to:  {filename}")
            print(f"       Events: {len(self.events)}")
            print(f"       Duration: {duration:.2f} seconds")
            print("You can reload this file later with option 4 and loop-replay it with option 5.")

        except Exception as e:
            print(f"Error saving recording: {e}")

    def _prompt_and_load(self):
        """
        Ask the user for a filename to load in a background thread so the
        main keyboard listener stays alive while the user types.
        """
        if self._prompting:
            return

        def _ask():
            self._prompting = True
            try:
                self.load_recording()
            finally:
                self._prompting = False

        t = threading.Thread(target=_ask, daemon=True)
        t.start()

    # ------------------------------------------------------------------
    # FEATURE 4: Load recording from file
    # Loads a previously saved JSON file into memory so it can be
    # replayed with option 2 (once) or option 5 (loop).
    # ------------------------------------------------------------------

    def load_recording(self, filename=None):
        """
        Load a JSON recording file into self.events.
        After loading, the user can press 2 for a single replay or
        5 for a continuous loop replay.
        """
        if filename is None:
            filename = input("\nEnter filename to load (e.g. my_macro.json): ").strip()
            if not filename:
                print("No filename entered. Load cancelled.")
                return

            # Be helpful: append .json if the user forgot it
            if not filename.endswith('.json'):
                filename += '.json'

        try:
            with open(filename, 'r') as f:
                data = json.load(f)

            self.events = data['events']
            duration = data.get('duration', 0)
            print(f"\n[LOAD] Recording loaded from:  {filename}")
            print(f"       Events: {len(self.events)}")
            print(f"       Duration: {duration:.2f} seconds")
            print("Press 2 to replay once, or 5 to loop-replay continuously.")

        except FileNotFoundError:
            print(f"File not found: {filename}")
        except Exception as e:
            print(f"Error loading recording: {e}")

    # ------------------------------------------------------------------
    # FEATURE 5: Loop replay
    # Continuously replays the loaded/recorded events until key 6 is
    # pressed. While looping, keys 1-4 are ignored (see on_key_release).
    # ------------------------------------------------------------------

    def loop_replay(self):
        """
        Start a continuous loop that replays events repeatedly.
        Only key 6 can stop this loop; all other number keys (1-4) are
        ignored while it is running to prevent accidental interruption.
        """
        if not self.events:
            print("No events to replay! Press 1 to record or 4 to load a file.")
            return

        self.playing = True
        self.looping = True
        print(f"\n[LOOP] LOOP REPLAY started — {len(self.events)} events per cycle.")
        print("       Press 6 to stop the loop.")

        replay_thread = threading.Thread(target=self._loop_replay_thread, daemon=True)
        replay_thread.start()

    def _loop_replay_thread(self):
        """Thread target: keep replaying events until self.looping is cleared."""
        loop_count = 0
        while self.looping and self.playing:
            loop_count += 1
            print(f"[LOOP] Iteration {loop_count}")
            self._execute_events()
            if self.looping:
                time.sleep(0.5)   # Short pause between loop cycles

        self.playing = False
        self.looping = False
        print(f"[LOOP] Loop stopped after {loop_count} iteration(s).")

    # ------------------------------------------------------------------
    # FEATURE 6: Stop replay / loop
    # Sets the flags that cause running replay threads to exit cleanly.
    # ------------------------------------------------------------------

    def stop_replay(self):
        """
        Signal any running replay or loop to stop at the next event boundary.
        This is the only action that is always allowed, even during loop replay.
        """
        if self.playing:
            self.playing = False
            self.looping = False
            print("\n[STOP] Replay/Loop stop requested — finishing current event...")
        else:
            print("[INFO] No replay is currently running.")

    # ------------------------------------------------------------------
    # Core event executor — shared by both single replay and loop replay
    # ------------------------------------------------------------------

    def _execute_events(self):
        """
        Iterate through self.events and simulate each mouse / keyboard action
        with its original inter-event timing. Checks self.playing before each
        event so the loop can be interrupted cleanly by key 6.
        """
        from pynput.mouse import Button as MouseButton
        from pynput.keyboard import Key as KeyboardKey

        mouse_controller = mouse.Controller()
        keyboard_controller = keyboard.Controller()

        try:
            last_timestamp = 0

            for event in self.events:
                # Check if we should abort (key 6 was pressed)
                if not self.playing:
                    break

                # Reproduce the original delay between events
                time_delay = event['timestamp'] - last_timestamp
                if time_delay > 0:
                    time.sleep(time_delay)

                event_type = event['type']

                if event_type == 'mouse_move':
                    mouse_controller.position = (event['x'], event['y'])

                elif event_type == 'mouse_click':
                    btn = MouseButton.left if event['button'] == 'left' else MouseButton.right
                    if event['pressed']:
                        mouse_controller.press(btn)
                    else:
                        mouse_controller.release(btn)

                elif event_type == 'mouse_scroll':
                    mouse_controller.scroll(event['dx'], event['dy'])

                elif event_type == 'key_press':
                    try:
                        kv = event['key']
                        if kv and isinstance(kv, str) and len(kv) == 1:
                            keyboard_controller.press(kv)
                        else:
                            k = getattr(KeyboardKey, kv, None)
                            if k:
                                keyboard_controller.press(k)
                    except Exception as e:
                        print(f"[WARN] Could not replay key_press '{event.get('key')}': {e}")

                elif event_type == 'key_release':
                    try:
                        kv = event['key']
                        if kv and isinstance(kv, str) and len(kv) == 1:
                            keyboard_controller.release(kv)
                        else:
                            k = getattr(KeyboardKey, kv, None)
                            if k:
                                keyboard_controller.release(k)
                    except Exception as e:
                        print(f"[WARN] Could not replay key_release '{event.get('key')}': {e}")

                last_timestamp = event['timestamp']

        except Exception as e:
            print(f"[ERROR] Unexpected error during event execution: {e}")

    # ------------------------------------------------------------------
    # Entry point
    # ------------------------------------------------------------------

    def run(self):
        """
        Start the main keyboard listener. This listener handles all control
        keys (1-6, ESC) and also captures keyboard events during recording.
        """
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
