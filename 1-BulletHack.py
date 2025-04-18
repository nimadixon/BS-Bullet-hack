import pydivert
import keyboard
import winsound 
import time
import winsound
import win32api
import win32con


data = []
while True:
    if keyboard.is_pressed("z"):
            winsound.Beep(400, 200)
            d = pydivert.WinDivert("outbound")
            d.open()
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0)
            time.sleep(0.05)
            winsound.Beep(400, 200)
            d.close()
            time.sleep(0.05)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0,0)
            keyboard.press('3')
            keyboard.release('3')
            keyboard.press('1')
            keyboard.release('1')
            time.sleep(4.5)
            d.open()
            keyboard.press('3')
            keyboard.release('3')
            time.sleep(4.5)
            d.close()
            keyboard.press('1')
            keyboard.release('1')
            keyboard.press('3')
            keyboard.release('3')
            time.sleep(0.5)
            keyboard.press('1')
            keyboard.release('1')
            time.sleep(0.8)
            keyboard.press('r')
            keyboard.release('r')
            time.sleep(5)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0)
            time.sleep(0.2)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0,0)
            winsound.Beep(400, 200)

