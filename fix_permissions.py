#!/usr/bin/env python3
"""
macOS Accessibility Permissions Helper
This script helps diagnose and fix accessibility permission issues for the tracker.
"""

import subprocess
import sys
import os
import platform


def check_macos_version():
    """Check macOS version to provide appropriate instructions"""
    try:
        version = platform.mac_ver()[0]
        major_version = int(version.split('.')[0])
        minor_version = int(version.split('.')[1]) if len(version.split('.')) > 1 else 0
        return major_version, minor_version, version
    except:
        return None, None, "Unknown"


def test_accessibility_permissions():
    """Test if accessibility permissions are granted"""
    print("🔍 Testing accessibility permissions...")
    
    try:
        import pynput
        from pynput import mouse, keyboard
        
        # Try to create listeners (this will fail if permissions not granted)
        mouse_listener = mouse.Listener(on_move=lambda x, y: None)
        keyboard_listener = keyboard.Listener(on_press=lambda key: None)
        
        # Try to start them briefly
        mouse_listener.start()
        keyboard_listener.start()
        
        # Stop them immediately
        mouse_listener.stop()
        keyboard_listener.stop()
        
        print("✅ Accessibility permissions are working!")
        return True
        
    except Exception as e:
        print(f"❌ Accessibility permissions not granted: {e}")
        return False


def open_accessibility_preferences():
    """Open macOS Accessibility preferences"""
    print("🔧 Opening Accessibility preferences...")
    try:
        subprocess.run([
            'open', 
            'x-apple.systempreferences:com.apple.preference.security?Privacy_Accessibility'
        ], check=True)
        print("✅ Accessibility preferences opened!")
        return True
    except Exception as e:
        print(f"❌ Could not open preferences: {e}")
        return False


def get_current_terminal():
    """Detect the current terminal application"""
    parent_process = os.getppid()
    try:
        result = subprocess.run(['ps', '-p', str(parent_process), '-o', 'comm='], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            terminal = result.stdout.strip()
            if 'Terminal' in terminal:
                return 'Terminal.app'
            elif 'iTerm' in terminal:
                return 'iTerm.app'
            elif 'zsh' in terminal or 'bash' in terminal:
                # Try to find the actual terminal
                try:
                    result2 = subprocess.run(['ps', '-ax', '-o', 'pid,comm'], 
                                           capture_output=True, text=True)
                    if 'Terminal' in result2.stdout:
                        return 'Terminal.app'
                    elif 'iTerm' in result2.stdout:
                        return 'iTerm.app'
                except:
                    pass
            return terminal
    except:
        pass
    return 'your terminal application'


def print_manual_instructions():
    """Print detailed manual instructions"""
    major, minor, version = check_macos_version()
    terminal = get_current_terminal()
    
    print("\n" + "="*60)
    print("📋 MANUAL ACCESSIBILITY SETUP INSTRUCTIONS")
    print("="*60)
    print(f"macOS Version: {version}")
    print(f"Detected Terminal: {terminal}")
    print()
    
    if major and major >= 13:  # macOS Ventura and later
        print("🍎 For macOS Ventura (13.0) and later:")
        print("1. Open 'System Settings' (not System Preferences)")
        print("2. Go to 'Privacy & Security' in the sidebar")
        print("3. Click on 'Accessibility'")
        print(f"4. Click the '+' button and add '{terminal}'")
        print("5. Make sure the toggle next to your terminal is ON")
    else:
        print("🍎 For macOS Monterey (12.0) and earlier:")
        print("1. Open 'System Preferences'")
        print("2. Go to 'Security & Privacy'")
        print("3. Click the 'Privacy' tab")
        print("4. Select 'Accessibility' from the left sidebar")
        print("5. Click the lock icon (🔒) to make changes")
        print("6. Enter your admin password")
        print(f"7. Click the '+' button and add '{terminal}'")
        print("8. Make sure the checkbox next to your terminal is checked")
    
    print("\n🔍 Finding your terminal application:")
    print("- Terminal.app is usually in /Applications/Utilities/")
    print("- iTerm.app is usually in /Applications/")
    print("- VS Code terminal: Add 'Visual Studio Code.app'")
    print("- PyCharm terminal: Add 'PyCharm.app'")
    
    print("\n⚠️  IMPORTANT:")
    print("- You may need to RESTART your terminal after granting permissions")
    print("- Some terminals require you to add 'Python' or 'python3' instead")
    print("- If it still doesn't work, try adding both the terminal AND Python")
    
    print("\n🔄 After making changes:")
    print("1. Close this terminal completely")
    print("2. Open a new terminal window")
    print("3. Run the tracker again")


def try_alternative_solutions():
    """Suggest alternative solutions"""
    print("\n" + "="*60)
    print("🛠️  ALTERNATIVE SOLUTIONS")
    print("="*60)
    
    print("1. 🐍 Try running with sudo (not recommended for regular use):")
    print("   sudo python3 keyboard-mouse-tracker.py")
    print()
    
    print("2. 🔧 Add Python itself to accessibility:")
    print("   - Find your Python installation:")
    print("     which python3")
    python_path = subprocess.run(['which', 'python3'], capture_output=True, text=True)
    if python_path.returncode == 0:
        print(f"     Your Python is at: {python_path.stdout.strip()}")
    print("   - Add this Python executable to Accessibility preferences")
    print()
    
    print("3. 📱 Create an Automator app:")
    print("   - Open Automator")
    print("   - Create a new 'Application'")
    print("   - Add 'Run Shell Script' action")
    print("   - Set the script to run your tracker")
    print("   - Save and add the Automator app to Accessibility")
    print()
    
    print("4. 🖥️  Use a different approach:")
    print("   - Consider using AppleScript for simpler automation")
    print("   - Use built-in macOS tools like 'Shortcuts' app")


def main():
    """Main function to guide through permission setup"""
    print("🖱️ macOS Accessibility Permissions Helper")
    print("="*50)
    print()
    
    # Check if we're on macOS
    if platform.system() != 'Darwin':
        print("❌ This script is for macOS only!")
        sys.exit(1)
    
    # Check current permissions
    if test_accessibility_permissions():
        print("🎉 Great! Your permissions are already working.")
        print("You can now run the tracker without issues.")
        return
    
    print("📝 Accessibility permissions need to be granted.")
    print("Let me help you fix this...")
    print()
    
    # Try to open preferences automatically
    print("Option 1: Automatic setup")
    if input("Would you like me to open Accessibility preferences? (y/N): ").lower().startswith('y'):
        if open_accessibility_preferences():
            print("\n✅ Preferences opened!")
            print("Now follow these steps in the preferences window that opened:")
            print("1. Click the lock icon (🔒) and enter your password")
            print("2. Click the '+' button")
            print("3. Navigate to and select your terminal application")
            print("4. Make sure the checkbox/toggle is enabled")
            print("\nAfter making changes, close your terminal and open a new one.")
        else:
            print("❌ Couldn't open preferences automatically.")
    
    # Show manual instructions
    print("\nOption 2: Manual setup")
    if input("Would you like detailed manual instructions? (Y/n): ").lower() != 'n':
        print_manual_instructions()
    
    # Show alternative solutions
    print("\nOption 3: Alternative solutions")
    if input("Would you like to see alternative solutions? (y/N): ").lower().startswith('y'):
        try_alternative_solutions()
    
    print("\n" + "="*60)
    print("🔄 After granting permissions:")
    print("1. Close this terminal completely")
    print("2. Open a new terminal")
    print("3. Run: python3 keyboard-mouse-tracker.py")
    print("4. If it still doesn't work, run this helper again")
    print("="*60)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Setup cancelled by user")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("Please try the manual setup instructions above.")