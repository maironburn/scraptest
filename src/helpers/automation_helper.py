from common_config import TEMP_IMGS
import cv2
import pyautogui
from time import sleep
from src.models.boton import Boton
from os import path


def capture_screen(name="screenshot"):
    pyautogui.screenshot("{}{}{}.png".format(TEMP_IMGS, path.sep, name))
    sleep(1)
    print("captured windows: {}".format(name))


def move_and_click(boton):
    if isinstance(boton, Boton):
        pyautogui.moveTo(boton.x, boton.y)
        pyautogui.click()
        sleep(0.5)


def getElementCoords(haystack, needle):

    img = cv2.imread(haystack, cv2.IMREAD_COLOR)
    img_display = img.copy()

    templ = cv2.imread(needle, cv2.IMREAD_COLOR)
    result = cv2.matchTemplate(img, templ, cv2.TM_CCORR_NORMED)
    cv2.normalize(result, result, 0, 1, cv2.NORM_MINMAX, -1)
    _minVal, _maxVal, minLoc, maxLoc = cv2.minMaxLoc(result, None)
    matchLoc = maxLoc
    h, w, _ = templ.shape

    center = (int((matchLoc[0] + w / 2)), int((matchLoc[1] + templ.shape[0]) - h / 2))
    x_center = int(matchLoc[0] + w / 2)
    y_center = int((matchLoc[1] + templ.shape[0]) - h / 2)

    return x_center, y_center
