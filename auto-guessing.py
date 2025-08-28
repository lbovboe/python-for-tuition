import random
import time
import threading
import pyautogui
import sys
from pynput import keyboard

class AutoTypingNumberGuesser:
    def __init__(self):
        self.running = False
        self.paused = False
        self.thread = None
        self.listener = None
        self.current_numbers = []
        self.current_index = 0
        self.press_enter = True
        self.delay = 1.0
        
        # Configure pyautogui settings
        pyautogui.FAILSAFE = True
        pyautogui.PAUSE = 0.1
    
    def get_range(self):
        """Get the range of numbers from user input"""
        try:
            start = int(input("Enter the first number (start of range): "))
            end = int(input("Enter the second number (end of range): "))
            
            if start > end:
                start, end = end, start
                
            return start, end
        except ValueError:
            print("Please enter valid integers!")
            return self.get_range()
    
    def get_typing_settings(self):
        """Get user preferences for typing behavior"""
        print("\n=== Typing Settings ===")
        
        while True:
            press_enter = input("Press Enter after each number? (y/n): ").lower().strip()
            if press_enter in ['y', 'yes', 'n', 'no']:
                press_enter = press_enter in ['y', 'yes']
                break
            print("Please enter 'y' or 'n'")
        
        while True:
            try:
                delay = float(input("Delay between each guess in seconds (default 1.0): ") or "1.0")
                if delay >= 0.1:
                    break
                print("Delay must be at least 0.1 seconds")
            except ValueError:
                print("Please enter a valid number")
        
        return press_enter, delay
    
    def countdown_to_start(self, seconds=3):
        """Give user time to click on the target input field"""
        print(f"\nYou have {seconds} seconds to click on the YouTube chat box")
        print("(or wherever you want the numbers typed)")
        
        for i in range(seconds, 0, -1):
            print(f"Starting in {i}...", end='\r')
            time.sleep(1)
        print("Starting now!     ")
    
    def setup_new_range(self, start, end):
        """Setup a new range and shuffle the numbers"""
        self.current_numbers = list(range(start, end + 1))
        random.shuffle(self.current_numbers)
        self.current_index = 0
        print(f"New range set: {start} to {end} ({len(self.current_numbers)} numbers)")
    
    def on_key_press(self, key):
        """Handle keyboard input for pause/resume/adjust"""
        try:
            if key == keyboard.Key.space:
                if not self.paused:
                    self.paused = True
                    print("\n*** PAUSED ***")
                    print("Controls:")
                    print("  SPACE = Resume")
                    print("  R = Adjust Range")
                    print("  S = Adjust Settings")
                    print("  Q = Quit")
                else:
                    self.paused = False
                    print("*** RESUMED ***")
            
            elif key.char == 'r' and self.paused:
                self.adjust_range()
            elif key.char == 's' and self.paused:
                self.adjust_settings()
            elif key.char == 'q':
                self.running = False
                print("\n*** QUITTING ***")
                
        except AttributeError:
            # Special keys (like space) don't have char attribute
            pass
        except Exception as e:
            pass
    
    def adjust_range(self):
        """Allow user to adjust the range while paused"""
        print("\n=== Adjust Range ===")
        start, end = self.get_range()
        self.setup_new_range(start, end)
        print("Range updated! Press SPACE to resume with new range.")
    
    def adjust_settings(self):
        """Allow user to adjust typing settings while paused"""
        print("\n=== Adjust Settings ===")
        self.press_enter, self.delay = self.get_typing_settings()
        print("Settings updated! Press SPACE to resume.")
    
    def start_keyboard_listener(self):
        """Start listening for keyboard input"""
        self.listener = keyboard.Listener(on_press=self.on_key_press)
        self.listener.daemon = True
        self.listener.start()
    
    def type_numbers(self):
        """Type random numbers without repetition"""
        print(f"\nWill type {len(self.current_numbers)} numbers")
        print("Controls: SPACE=Pause/Resume, Q=Quit")
        print("Move mouse to top-left corner for emergency stop!")
        
        self.countdown_to_start(2)  # 2-second countdown
        
        try:
            while self.current_index < len(self.current_numbers) and self.running:
                # Check if paused
                while self.paused and self.running:
                    time.sleep(0.1)
                    continue
                
                if not self.running:
                    break
                
                number = self.current_numbers[self.current_index]
                
                # Type the number
                pyautogui.typewrite(str(number))
                
                # Press Enter if requested
                if self.press_enter:
                    pyautogui.press('enter')
                else:
                    pyautogui.typewrite(' ')
                
                print(f"Typed #{self.current_index + 1}: {number}")
                self.current_index += 1
                
                # Wait before next number (but check for pause during wait)
                if self.current_index < len(self.current_numbers):
                    elapsed = 0
                    while elapsed < self.delay and self.running:
                        if self.paused:
                            while self.paused and self.running:
                                time.sleep(0.1)
                        time.sleep(0.1)
                        elapsed += 0.1
            
            if self.running and self.current_index >= len(self.current_numbers):
                print(f"\nFinished! Typed all {len(self.current_numbers)} numbers.")
                
        except pyautogui.FailSafeException:
            print(f"\n\nEmergency stop activated! (Mouse moved to corner)")
            self.running = False
        except Exception as e:
            print(f"\n\nError occurred: {e}")
            self.running = False
    
    def start_typing_thread(self):
        """Start the typing process in a separate thread"""
        self.running = True
        self.paused = False
        self.thread = threading.Thread(target=self.type_numbers)
        self.thread.daemon = True
        self.thread.start()
    
    def run(self):
        """Main program loop"""
        print("=== Auto-Typing Random Number Guesser with Pause Control ===")
        print("This program will automatically type random numbers")
        print("into whatever text field you click on (like YouTube chat).\n")
        
        print("CONTROLS:")
        print("- SPACE = Pause/Resume")
        print("- R = Adjust Range (while paused)")
        print("- S = Adjust Settings (while paused)")  
        print("- Q = Quit")
        print("- Move mouse to top-left corner for emergency stop\n")
        
        try:
            # Initial setup
            start, end = self.get_range()
            self.press_enter, self.delay = self.get_typing_settings()
            self.setup_new_range(start, end)
            
            print(f"\n=== Configuration ===")
            print(f"Range: {start} to {end} ({len(self.current_numbers)} numbers)")
            print(f"Press Enter after each: {'Yes' if self.press_enter else 'No'}")
            print(f"Delay between numbers: {self.delay} seconds")
            
            input("\nPress Enter when ready to start...")
            
            # Start keyboard listener
            self.start_keyboard_listener()
            
            # Start typing
            self.start_typing_thread()
            
            # Keep main thread alive
            while self.running and self.thread.is_alive():
                time.sleep(0.1)
                
        except KeyboardInterrupt:
            self.running = False
            print(f"\n\nProgram interrupted by user.")
        except Exception as e:
            print(f"\n\nUnexpected error: {e}")
        finally:
            if self.listener:
                self.listener.stop()
            if self.thread and self.thread.is_alive():
                self.thread.join(timeout=1)

if __name__ == "__main__":
    print("Installing required packages...")
    print("If this is your first time running, you may need to install:")
    print("pip install pyautogui pynput")
    print()
    
    try:
        guesser = AutoTypingNumberGuesser()
        guesser.run()
    except ImportError as e:
        print(f"ERROR: Required package not installed!")
        print("Please install with: pip install pyautogui pynput")
        print("Then run this program again.")