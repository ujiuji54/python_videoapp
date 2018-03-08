import numpy as np
import cv2

def facerect(image):

    #カスケード分類器の特徴量を取得する
    cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    facerect = cascade.detectMultiScale(image_gray, scaleFactor=1.1, minNeighbors=1, minSize=(10, 10))

    #顔が認識された場合
    color = (255, 255, 255) #白
    if len(facerect) > 0:
        #顔を囲む矩形の作成
        for rect in facerect:
            cv2.rectangle(image, tuple(rect[0:2]),tuple(rect[0:2]+rect[2:4]), color, thickness = 4)
    return image
