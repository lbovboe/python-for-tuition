import pyautogui
from pynput.keyboard import Listener, Key
import time
import random
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
    # aw
    # pyautogui.moveTo(300, 820)
    # pyautogui.sleep(delay)
    # pyautogui.click(pyautogui.position())  # Move mouse to position (100, 200)
     # Press the 'E' key
    # for i in range(5):
    #     pyautogui.moveTo(870, 630)
    #     pyautogui.sleep(0.5)
    #     pyautogui.click(pyautogui.position())
    # for i in range(5):
    #     pyautogui.moveTo(870, 680)
    #     pyautogui.sleep(0.5)
    #     pyautogui.click(pyautogui.position())
    # for i in range(5):
    # pyautogui.moveTo(920, 630)
    # pyautogui.sleep(0.1)
    pyautogui.click(pyautogui.position())
    # for i in range(5):
    #     pyautogui.moveTo(920, 680)
    #     pyautogui.sleep(0.5)
    #     pyautogui.click(pyautogui.position())
    # pyautogui.press('e') 
def human_like_move(x, y):
    duration = random.uniform(0.2, 0.4)  # Random duration for the move
    pyautogui.moveTo(x, y, duration=duration, tween=pyautogui.easeInOutQuad)

def human_like_click():
    x, y = pyautogui.position()
    delay = random.uniform(0.1, 0.3)  # Random delay before click
    time.sleep(delay)
    pyautogui.click(x, y)
    time.sleep(random.uniform(0.1, 0.3))  # Random delay after click
def main():
    lis = Listener(on_press=on_press)
    lis.start()

    display_controls()
    pyautogui.moveTo(920, 630)
    while running:
        if not pause:
            # perform_actions()
            time.sleep(0.3)
            pyautogui.moveTo(920, 630)
            pyautogui.click(pyautogui.position())
            time.sleep(0.3)
            pyautogui.click(pyautogui.position())
            time.sleep(0.3)
            
            human_like_move(920, 630)
            
            # Perform a human-like click
            human_like_click()
            
            # Random delay between actions
            time.sleep(random.uniform(0.1, 0.4))
    lis.stop()

if __name__ == "__main__":
    main()
