import pyscreenshot as ImageGrab
import time
from pynput.mouse import Controller, Button
from pynput.keyboard import Controller as KBoard
from pynput.keyboard import Key

fileDir = 'images/' + str.lower(input('Stream name?: ')) + '/'
mouse = Controller()
keyboard = KBoard()
mouse.position=(1000,800)
time.sleep(5)
mouse.click(Button.left, 1)
for i in range(2018 - 1984):
    im=ImageGrab.grab(bbox=(415,600,1490,1000))
    im.save(fileDir + str(i + 1984) + '.jpg', 'JPEG')
    keyboard.press(Key.right)
    keyboard.release(Key.right)