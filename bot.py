import pyautogui
from PIL import ImageGrab

#get params
# pyautogui.displayMousePosition()

positionY = 526
positionXD = 660
positionXF = 743
positionXJ = 826
positionXK = 908
color = 1
colorCyan = list(range(14, 45))

while True:
    key1 = ImageGrab.grab().getpixel((positionXD, positionY))[0]
    key2 = ImageGrab.grab().getpixel((positionXF, positionY))[0]
    key3 = ImageGrab.grab().getpixel((positionXJ, positionY))[0]
    key4 = ImageGrab.grab().getpixel((positionXK, positionY))[0]

    if color == key1:
        pyautogui.click(positionXD, positionY)
    if color == key2:
        pyautogui.click(positionXF, positionY)
    if color == key3:
        pyautogui.click(positionXJ, positionY)
    if color == key4:
        pyautogui.click(positionXK, positionY)

    if key1 in colorCyan:
        pyautogui.click(positionXD, positionY)
        print('aqui')
    if key2 in colorCyan:
        print('aqui2')
        pyautogui.click(positionXF, positionY)
    if key3 in colorCyan:
        print('aqui3')
        pyautogui.click(positionXJ, positionY)
    if key4 in colorCyan:
        print('aqui4')
        pyautogui.click(positionXK, positionY)
    