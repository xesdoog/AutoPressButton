import pyautogui
import time
def main():
 start_playing = False
 time.sleep(5)
 while not start_playing :
  try:
   x1, y1 = pyautogui.center(pyautogui.locateOnScreen('button.png', confidence = 0.7)) 
   time.sleep(2)
   pyautogui.click(x1, y1)
   print('Button Pressed')
   start_playing = True
   time.sleep(50)
  except:
    print(f'Button not found! Trying again in 5 seconds...')
    time.sleep(5)
while True:
 main()
