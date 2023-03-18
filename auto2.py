import pyautogui
from pynput.keyboard import *

#  ======== settings ========
delay = 30  # in seconds
delay2 = 1
resume_key = Key.f1
pause_key = Key.f2
exit_key = Key.esc
#  ==========================

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
    print("\t F1 = Resume")
    print("\t F2 = Pause")
    print("\t F3 = Exit")
    print("-----------------------------------------------------")
    print('Press F1 to start ...')

def main():
    lis = Listener(on_press=on_press)
    lis.start()

    display_controls()
    while running:
        if not pause:
            pyautogui.moveTo(763,292,0.3)
            pyautogui.PAUSE = delay2
            pyautogui.click(pyautogui.position())
            pyautogui.PAUSE = delay2

            x,y = pyautogui.position()
            print(x,y)

            for i in range(3):
                x+=130
                pyautogui.moveTo(x,y,0.3)
                pyautogui.PAUSE = delay2
                pyautogui.click(pyautogui.position())
                pyautogui.PAUSE = delay2

            pyautogui.moveTo(1414,552,0.3)
            pyautogui.PAUSE = delay2
            pyautogui.click(pyautogui.position())
            pyautogui.PAUSE = delay2
            pyautogui.moveTo(939,596,0.3)
            pyautogui.PAUSE = delay2
            pyautogui.click(pyautogui.position())
            pyautogui.PAUSE = delay2
            pyautogui.PAUSE = 10
            pyautogui.moveTo(1116,585,0.3)
            pyautogui.PAUSE = delay2
            pyautogui.click(pyautogui.position())
            pyautogui.PAUSE = delay2
            pyautogui.PAUSE = 5


    lis.stop()


if __name__ == "__main__":
    main()