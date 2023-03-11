import pyautogui
from datetime import datetime

now = datetime.now()

# dd/mm/YY H:M:S
dt_string = now.strftime("%d_%m_%Y_%H_%M_%S")
print("date and time =", dt_string)

myScreenshot = pyautogui.screenshot()
myScreenshot.save(r'C:\Users\prati\OneDrive\Desktop\New folder\Screenshot_'+dt_string+'.png')
