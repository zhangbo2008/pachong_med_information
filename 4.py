#老办法. 模拟鼠标来进行存网页.
import pyautogui
pyautogui.FAILSAFE =False 

print(pyautogui.size())   # 返回所用显示器的分辨率； 输出：Size(width=1920, height=1080)
width,height = pyautogui.size()
print(width,height)  # 1920 1080

import time
time.sleep(3)
while 100:
  
  
  

  
  
  pyautogui.moveTo(1228,541)

  pyautogui.click(clicks=1) #点击
  time.sleep(0.3)
  pyautogui.hotkey('ctrl','s')

  pyautogui.press('enter')

  pyautogui.press('enter')
  
  
  