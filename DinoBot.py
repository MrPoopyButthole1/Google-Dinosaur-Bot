from PIL import ImageGrab,ImageOps
import pyautogui as pg
import time
from numpy import *

class Cordinates():
    replayBtn = (357, 406)
    dinosaur = (169, 423)
    box = (300, 445, 315, 450)

def restartGame():
    pg.click(Cordinates.replayBtn)
    pg.keyDown('down')

def pressSpace():
    pg.keyUp('down')
    pg.keyDown('space')
    print("Jump")
    pg.keyUp('space')
    time.sleep(0.18)
    pg.keyDown('down')
    print("Duck")


def imageGrab():
     box = Cordinates.box
     image1 = ImageGrab.grab(box)
     grayImage = ImageOps.grayscale(image1)
     a = array(grayImage.getcolors())
     x = a.sum()
     print(x)
     return(x)


def main():
    restartGame()
    while True:


        if imageGrab() != 322:
            pressSpace()
            #time.sleep( 0.001)
            #restartGame( )



main()
