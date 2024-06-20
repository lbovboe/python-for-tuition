import pyautogui
from pynput.keyboard import Listener, Key

# ======== settings ========
delay = 1  # in seconds
resume_key = Key.backspace
pause_key = Key.tab
exit_key = Key.esc

# ==========================
pause = True
running = True
positions = []

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

def calculate_positions(center_x, center_y, offset=150):
    return [
        (center_x - offset, center_y - offset), (center_x, center_y - offset), (center_x + offset, center_y - offset),
        (center_x - offset, center_y), (center_x, center_y), (center_x + offset, center_y),
        (center_x - offset, center_y + offset), (center_x, center_y + offset), (center_x + offset, center_y + offset)
    ]

def perform_actions():
    global positions
    if not positions:
        # Get the current mouse position as the center
        center_x, center_y = pyautogui.position()
        positions = calculate_positions(center_x, center_y)

    for position in positions:
        if not running or pause:
            break
        pyautogui.moveTo(position)
        pyautogui.sleep(1)
        pyautogui.click(pyautogui.position())
        pyautogui.sleep(delay)

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
