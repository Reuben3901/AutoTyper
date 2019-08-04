import pyautogui, time, pyperclip

# Copy text into clipboard then run program
time.sleep(5)
pyautogui.typewrite(pyperclip.paste(), interval=.02)
