import pyautogui
from pynput.keyboard import Listener, Key

# ======== settings ========
delay = 2  # in seconds
resume_key = Key.backspace
pause_key = Key.tab
exit_key = Key.esc

# ==========================

pause = True
running = True

def on_press(key):
    global running, pause

    if key == resume_key:
        pause = False
        print("[Resumed]")
    elif key == pause_key:
        pause = True
        print("[Paused]")
    elif key == exit_key:
        running = False
        print("[Exit]")

def display_controls():
    print("// AutoClicker by Paul")
    print("// - Settings: ")
    print("\t delay = " + str(delay) + ' sec' + '\n')
    print("// - Controls:")
    print("\t backspace = Resume")
    print("\t tab = Pause")
    print("\t Esc = Exit")
    print("-----------------------------------------------------")
    print('Press F1 to start ...')

def perform_actions():
    # Example actions: move mouse to a specific location and press 'E'
    pyautogui.sleep(1)
    pyautogui.moveTo(300, 820)
    pyautogui.sleep(delay)
    pyautogui.click(pyautogui.position())  # Move mouse to position (100, 200)
     # Press the 'E' key
    pyautogui.sleep(5)
    pyautogui.moveTo(400, 820)
    pyautogui.sleep(1)
    pyautogui.click(pyautogui.position())
    # pyautogui.press('e') 

def main():
    lis = Listener(on_press=on_press)
    lis.start()

    display_controls()
    while running:
        if not pause:
            perform_actions()
    lis.stop()

if __name__ == "__main__":
    main()
