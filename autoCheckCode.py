import pyautogui
from pynput.keyboard import Listener, Key
import itertools

# ======== settings ========
delay = 1  # in seconds
resume_key = Key.backspace
pause_key = Key.tab
exit_key = Key.esc
# ==========================

pause = True
running = True

# Existing code
base_code = "QAJQRZYGZV"
# Possible characters
chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
# Generate all combinations
# Generate all combinations
# Generate all combinations
combinations = [''.join(item) for item in itertools.product(chars, repeat=2)]

# Sort combinations to start with A0, A1, ..., A9, AA, ..., AZ, B0, ...
combinations.sort(key=lambda x: (x[0], int(x[1]) if x[1].isdigit() else ord(x[1])))

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
    print("\t alt = Resume")
    print("\t tab = Pause")
    print("\t Esc = Exit")
    print("-----------------------------------------------------")
    print('Press F1 to start ...')

def perform_actions(code):
    # go to redeem button
    pyautogui.moveTo(850, 900) 
    pyautogui.click(pyautogui.position())
    pyautogui.sleep(0.5)
    # # go to input field
    pyautogui.moveTo(500, 690) 
    pyautogui.click(pyautogui.position())
    pyautogui.sleep(0.5)
    # # paste the code, help me fill in here

    # # Paste the code
    pyautogui.typewrite(code)
    pyautogui.sleep(0.5)
    # # go to confirm button and click confirm button
    pyautogui.moveTo(500, 820)
    pyautogui.sleep(0.5) 
    pyautogui.click(pyautogui.position())
    pyautogui.sleep(0.5)
    
    # # go to repeat button
    pyautogui.moveTo(500, 840) 
    pyautogui.sleep(0.5)
    pyautogui.click(pyautogui.position())
    pyautogui.sleep(0.5)

def main():
    lis = Listener(on_press=on_press)
    lis.start()

    display_controls()
    while running:
        # if not pause:
        #     perform_actions()
        for comb in combinations:
            if not pause:
                full_code = base_code + comb
                perform_actions(full_code)
                pyautogui.sleep(delay)

    
    lis.stop()
if __name__ == "__main__":
    main()
    