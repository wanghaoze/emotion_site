import cv2
import tensorflow as tf
from keras.preprocessing import image
import os
import keras
import numpy as np
emotions = {
    0:'anger', #生气
    1:'disgust', #厌恶
    2:'fear', #恐惧
    3:'happy', #开心
    4:'sad', #伤心
    5:'surprised', #惊讶
    6:'normal', #中性
}

num = 0
cap = cv2.VideoCapture(0)


def face_locate(pic_path):
    pic = cv2.imread(pic_path)
    pic_gray = cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY)  # 将图片转化成灰度
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    face_cascade.load("haarcascade_frontalface_default.xml")
    faces = face_cascade.detectMultiScale(pic_gray, 1.3, 5)
    # print(len(faces))
    # print(faces.shape)
    return faces    # num*4, (num,(x, y, w, h))    x:begin_col, y:begin_row w:width h:height


pic_path = 'IMG_5506.jpg'                   # 证件照
# pic_path = '20191216085415.jpg'             # 表情包
# pic_path = 'WIN_20191215_19_50_40_Pro.jpg'  # 生活照
# pic_path = 'timg.jfif'                      # 合照
# pic_path = 'timg (1).jfif'                  # 不完全合照 7个识别6个
a = face_locate(pic_path)
print(a)



