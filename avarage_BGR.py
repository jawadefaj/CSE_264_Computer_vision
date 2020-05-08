import cv2
import numpy as np


def find_avarage(img):
    average = img.mean(axis=0).mean(axis=0)
    #print(average)
    return average