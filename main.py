import cv2
from play import *

if __name__ == '__main__':
    video = cv2.VideoCapture(u"video.mp4")
    play(video)
