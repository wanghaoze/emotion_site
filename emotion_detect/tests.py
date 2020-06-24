# This Python file uses the following encoding: utf-8
from PIL import Image
import cv2
from keras.preprocessing import image
import os
import keras
import numpy as np
from aip import AipFace
import socket
# 百度api接口信息
APP_ID = '18058987'
API_KEY = 'wGCDWR1yw5kfjw8dSOeGPluG'
SECRET_KEY = 'jSNbdHIDIbH4i4gMxHv1Bz05CsifRoxc'
client = AipFace(APP_ID, API_KEY, SECRET_KEY)
imageType = "BASE64"
# {'error_code': 0, 'error_msg': 'SUCCESS', 'log_id': 4505258994849, 'timestamp': 1577414265, 'cached': 0,
# 'result': {'face_num': 1, 'face_list': [{'face_token': '1892252b6ee2bcd955ff91bc4b212bc0',
# 'location': {'left': 214.96, 'top': 100.7, 'width': 89, 'height': 85, 'rotation': -3}, 'face_probability': 1,
# 'angle': {'yaw': -16.46, 'pitch': 21.23, 'roll': -0.89}, 'age': 27, 'beauty': 67.24,
# 'gender': {'type': 'male', 'probability': 1}, 'landmark': [{'x': 246.57, 'y': 109.4}, {'x': 285.33, 'y': 107.16},
# {'x': 272.1, 'y': 138.36}, {'x': 269.28, 'y': 157.72}], 'landmark72': [{'x': 214.82, 'y': 100.97},
# {'x': 217.43, 'y': 117}, {'x': 221.44, 'y': 133.12}, {'x': 226.39, 'y': 149.15}, {'x': 236.95, 'y': 165.47},
# {'x': 253.46, 'y': 179.55}, {'x': 270.44, 'y': 182.79}, {'x': 283.86, 'y': 173.7}, {'x': 293.38, 'y': 156.86},
# {'x': 298.26, 'y': 141.61}, {'x': 301.29, 'y': 126.95}, {'x': 303.45, 'y': 112.3}, {'x': 304.12, 'y': 97.93},
# {'x': 237.31, 'y': 110.72}, {'x': 242.08, 'y': 107.66}, {'x': 247.36, 'y': 106.55}, {'x': 252.48, 'y': 107.6},
# {'x': 256.72, 'y': 111.74}, {'x': 252.32, 'y': 112.99}, {'x': 247.12, 'y': 113.81}, {'x': 241.62, 'y': 112.9},
# {'x': 246.57, 'y': 109.4}, {'x': 228.64, 'y': 103.85}, {'x': 236.56, 'y': 98.94}, {'x': 244.86, 'y': 99.42},
# {'x': 252.54, 'y': 100.82}, {'x': 259.8, 'y': 104.93}, {'x': 252.13, 'y': 104.95}, {'x': 244.51, 'y': 104.19},
# {'x': 236.57, 'y': 103.77}, {'x': 277.1, 'y': 110.77}, {'x': 280.82, 'y': 106}, {'x': 285.65, 'y': 104.16},
# {'x': 290.54, 'y': 104.42}, {'x': 294.64, 'y': 107.12}, {'x': 291.6, 'y': 109.81}, {'x': 286.85, 'y': 111.34},
# {'x': 281.67, 'y': 111.25}, {'x': 285.33, 'y': 107.16}, {'x': 276.71, 'y': 104.47}, {'x': 282.51, 'y': 99.4},
# {'x': 288.78, 'y': 97.12}, {'x': 295.5, 'y': 95.47}, {'x': 301.47, 'y': 99.08}, {'x': 295.98, 'y': 100.1},
# {'x': 289.79, 'y': 101.7}, {'x': 283.31, 'y': 103.33}, {'x': 262.35, 'y': 112.41}, {'x': 261.79, 'y': 122.05},
# {'x': 261.02, 'y': 131.69}, {'x': 258.86, 'y': 140.68}, {'x': 264.74, 'y': 142.13}, {'x': 276.46, 'y': 141.64},
# {'x': 279.95, 'y': 139.52}, {'x': 277.64, 'y': 130.86}, {'x': 275.48, 'y': 121.36}, {'x': 273.42, 'y': 111.86},
# {'x': 272.1, 'y': 138.36}, {'x': 253.74, 'y': 156.92}, {'x': 261.91, 'y': 154.1}, {'x': 269.95, 'y': 154.01},
# {'x': 276.62, 'y': 152.97}, {'x': 281.79, 'y': 155.33}, {'x': 277.85, 'y': 161.71}, {'x': 270.45, 'y': 165.15},
# {'x': 260.82, 'y': 163.2}, {'x': 262.21, 'y': 156.85}, {'x': 269.89, 'y': 157.21}, {'x': 276.27, 'y': 155.86},
# {'x': 276.08, 'y': 157.4}, {'x': 269.97, 'y': 158.8}, {'x': 262.41, 'y': 158.49}],
# 'race': {'type': 'yellow', 'probability': 0.84}, 'glasses': {'type': 'none', 'probability': 1},
# 'expression': {'type': 'none', 'probability': 1}, 'emotion': {'type': 'neutral', 'probability': 0.93}}]}}


# {'error_code': 0, 'error_msg': 'SUCCESS', 'log_id': 7935750584001, 'timestamp': 1577414214, 'cached': 0,
# 'result': {'face_num': 2,
# 'face_list': [{'face_token': 'c6d82e55f888d19a439eb3bc5f1606bd',
# 'location': {'left': 259.99, 'top': 248.46, 'width': 129, 'height': 132, 'rotation': -23}, 'face_probability': 0.68,
# 'angle': {'yaw': -17.27, 'pitch': 19.55, 'roll': -24.42}, 'age': 36, 'beauty': 39.82,
# 'gender': {'type': 'male', 'probability': 0.93}, 'landmark': [{'x': 308.08, 'y': 252.89}, {'x': 359.04, 'y': 230.56},
# {'x': 355.82, 'y': 274.85}, {'x': 365.21, 'y': 306.7}], 'landmark72': [{'x': 268.11, 'y': 268.06},
# {'x': 277.75, 'y': 288.71}, {'x': 290.5, 'y': 308.28}, {'x': 306.93, 'y': 325.67}, {'x': 330.27, 'y': 338.41},
# {'x': 356.58, 'y': 344.65}, {'x': 379.9, 'y': 340.39}, {'x': 393.73, 'y': 322.74}, {'x': 400.37, 'y': 299.16},
# {'x': 402.89, 'y': 275.62}, {'x': 400.77, 'y': 253.66}, {'x': 394.56, 'y': 233.17}, {'x': 386.03, 'y': 213.94},
# {'x': 296.53, 'y': 258.85}, {'x': 301.77, 'y': 254}, {'x': 307.33, 'y': 250.68}, {'x': 313.48, 'y': 248.59},
# {'x': 320.59, 'y': 249.19}, {'x': 315.28, 'y': 252.78}, {'x': 309.6, 'y': 255.82}, {'x': 303.25, 'y': 257.82},
# {'x': 308.08, 'y': 252.89}, {'x': 281.95, 'y': 247.27}, {'x': 287.35, 'y': 237.14}, {'x': 297.06, 'y': 231.94},
# {'x': 307.7, 'y': 229.17}, {'x': 319.36, 'y': 231.45}, {'x': 309.86, 'y': 235.19}, {'x': 299.7, 'y': 238.82},
# {'x': 290.44, 'y': 243.07}, {'x': 350.77, 'y': 235.98}, {'x': 354.25, 'y': 231.31}, {'x': 358.99, 'y': 228.4},
# {'x': 364.57, 'y': 226.62}, {'x': 370.63, 'y': 226.44}, {'x': 366.47, 'y': 229.89}, {'x': 361.43, 'y': 232.8},
# {'x': 355.97, 'y': 234.44}, {'x': 359.04, 'y': 230.56}, {'x': 340.17, 'y': 223.03}, {'x': 344.86, 'y': 214.89},
# {'x': 351.89, 'y': 210.12}, {'x': 359.86, 'y': 206.97}, {'x': 368.75, 'y': 208.61}, {'x': 361.93, 'y': 212.8},
# {'x': 354.69, 'y': 216.49}, {'x': 347.38, 'y': 219.81}, {'x': 329.41, 'y': 246.64}, {'x': 333.53, 'y': 260.34},
# {'x': 337.36, 'y': 274.3}, {'x': 339.3, 'y': 288.5}, {'x': 350.08, 'y': 286.85}, {'x': 365.67, 'y': 279.03},
# {'x': 371.49, 'y': 271.22}, {'x': 361.99, 'y': 261.4}, {'x': 353.07, 'y': 250.63}, {'x': 344.1, 'y': 239.59},
# {'x': 355.82, 'y': 274.85}, {'x': 341.19, 'y': 315.28}, {'x': 352.4, 'y': 306.15}, {'x': 364.43, 'y': 300.9},
# {'x': 373.74, 'y': 296.67}, {'x': 383.74, 'y': 294.79}, {'x': 379.55, 'y': 306.94}, {'x': 370.08, 'y': 315.27},
# {'x': 355.9, 'y': 318.42}, {'x': 353.93, 'y': 310.07}, {'x': 366.06, 'y': 305.74}, {'x': 374.94, 'y': 300.53},
# {'x': 375.63, 'y': 302.48}, {'x': 366.49, 'y': 308.01}, {'x': 354.88, 'y': 312.59}],
# 'race': {'type': 'yellow', 'probability': 1}, 'glasses': {'type': 'common', 'probability': 1},
# 'expression': {'type': 'none', 'probability': 1}, 'emotion': {'type': 'neutral', 'probability': 0.76}},
# {'face_token': '9cfba81d01d3dc0a71337c26ebded0cf',
# 'location': {'left': 424.3, 'top': 287.56, 'width': 123, 'height': 121, 'rotation': 2}, 'face_probability': 1,
# 'angle': {'yaw': -1.02, 'pitch': 8.6, 'roll': 0.22}, 'age': 9, 'beauty': 19.52,
# 'gender': {'type': 'male', 'probability': 0.99}, 'landmark': [{'x': 462.83, 'y': 309.86}, {'x': 512.94, 'y': 311.92},
# {'x': 489.03, 'y': 344.99}, {'x': 486.03, 'y': 375.62}], 'landmark72': [{'x': 423.29, 'y': 306.77},
# {'x': 423.75, 'y': 327.3}, {'x': 425.99, 'y': 348.08}, {'x': 430.43, 'y': 368.83}, {'x': 443.9, 'y': 390.12},
# {'x': 464.16, 'y': 406.05}, {'x': 484.89, 'y': 411.09}, {'x': 504.76, 'y': 405.78}, {'x': 523.54, 'y': 390.46},
# {'x': 536.43, 'y': 370.94}, {'x': 542, 'y': 351.29}, {'x': 545.19, 'y': 331.51}, {'x': 546.75, 'y': 311.77},
# {'x': 452.14, 'y': 310.59}, {'x': 458.29, 'y': 309.92}, {'x': 463.36, 'y': 309.83}, {'x': 467.68, 'y': 309.68},
# {'x': 472.81, 'y': 310.86}, {'x': 468.03, 'y': 310.96}, {'x': 463.45, 'y': 311.31}, {'x': 458.21, 'y': 310.96},
# {'x': 462.83, 'y': 309.86}, {'x': 444.22, 'y': 297.96}, {'x': 452.12, 'y': 290.25}, {'x': 461.57, 'y': 288.8},
# {'x': 470.63, 'y': 289.65}, {'x': 478.68, 'y': 295.24}, {'x': 470.31, 'y': 296.22}, {'x': 461.5, 'y': 297.27},
# {'x': 452.74, 'y': 298.56}, {'x': 503.76, 'y': 312.35}, {'x': 508.56, 'y': 311.46}, {'x': 512.95, 'y': 311.95},
# {'x': 517.69, 'y': 312.19}, {'x': 523.27, 'y': 313.27}, {'x': 517.95, 'y': 313.35}, {'x': 512.89, 'y': 313.23},
# {'x': 508.43, 'y': 312.57}, {'x': 512.94, 'y': 311.92}, {'x': 500.96, 'y': 296.13}, {'x': 508.9, 'y': 291.29},
# {'x': 517.13, 'y': 291.11}, {'x': 525.22, 'y': 293.28}, {'x': 531.26, 'y': 301.02}, {'x': 523.93, 'y': 301.12},
# {'x': 516.35, 'y': 299.56}, {'x': 508.45, 'y': 297.66}, {'x': 481.27, 'y': 312.48}, {'x': 478.16, 'y': 324.57},
# {'x': 474.86, 'y': 336.7}, {'x': 469.52, 'y': 348.97}, {'x': 478.43, 'y': 351.1}, {'x': 497.5, 'y': 351.75},
# {'x': 505.43, 'y': 350.13}, {'x': 501.15, 'y': 337.59}, {'x': 498.77, 'y': 325.46}, {'x': 496.36, 'y': 313.22},
# {'x': 489.03, 'y': 344.99}, {'x': 463.92, 'y': 372.97}, {'x': 475.11, 'y': 369.23}, {'x': 486.57, 'y': 370.19},
# {'x': 497.47, 'y': 370.09}, {'x': 506.78, 'y': 374.38}, {'x': 498.02, 'y': 382.14}, {'x': 486.23, 'y': 384.64},
# {'x': 473.58, 'y': 381.63}, {'x': 475, 'y': 372.73}, {'x': 486.29, 'y': 374.18}, {'x': 497.16, 'y': 373.36},
# {'x': 496.79, 'y': 377.69}, {'x': 486.42, 'y': 378.35}, {'x': 475.1, 'y': 377.08}],
# 'race': {'type': 'yellow','probability': 1}, 'glasses': {'type': 'none', 'probability': 1},
# 'expression': {'type': 'none', 'probability': 1}, 'emotion': {'type': 'sad', 'probability': 1}}]}}
# 定义参数变量
options = {}
options["max_face_num"] = 10
options["face_field"] = "age,beauty,gender,landmark,race,glasses,expression,emotion"
## 百度接口信息

emotions = {
    0: '愤怒',        # 生气
    1: '厌恶',        # 厌恶
    2: '恐惧',        # 恐惧
    3: '高兴',        # 开心
    4: '伤心',        # 伤心
    5: '惊讶',        # 惊讶
    6: '无情绪',      # 中性
}
# Create your tests here.


def isNetOK(testserver):
    s=socket.socket()
    s.settimeout(3)
    try:
        status = s.connect_ex(testserver)
        if status == 0:
            s.close()
            return True
        else:
            return False
    except Exception as e:
        return False


def isNetChainOK(testserver=('ai.baidu.com', 80)):
    isOK = isNetOK(testserver)
    return isOK


print(isNetChainOK())
def face_locate(pic_path):
    pic = cv2.imread(pic_path, 1)
    # print(pic_path)
    pic_gray = cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY)  # 将图片转化成灰度
    # cv2.imshow('?', pic_gray)
    # cv2.waitKey()
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    face_cascade.load("haarcascade_frontalface_default.xml")
    faces = face_cascade.detectMultiScale(pic_gray, 1.3, 5)
    print(len(faces))
    # print(faces.shape)
    return faces


def is_valid(file):
    valid = True
    try:
        Image.open(file).load()
    except OSError:
        valid = False
    return valid


def process_img(pic_path, model_path, dist_path='static/image/target_img.jpg'):
    faces = face_locate(pic_path)
    number = 0
    picture = cv2.imread(pic_path)
    pic = picture
    if len(faces) > 0:
        if len(faces) == 1:
            for (x, y, w, h) in faces:
                pic = picture
                image_pix = pic[y - 10:y + h + 10, x - 10:x + w + 10, :]
                img_name_save = "%d.jpg" % (number % 5)
                cv2.imwrite(img_name_save, image_pix)
                emo = emotion_detect(pic_path, model_path)
                number += 1
                if number > 1000:
                    break
                cv2.rectangle(pic, (x, y), (x + w, y + h), (0, 255, 0), 2)
                # font = cv2.FONT_HERSHEY_SIMPLEX
                # cv2.putText(pic, emo, (x + 30, y + 30), font, 1, (255, 0, 255))
            print(dist_path)
            cv2.imwrite(dist_path, pic)
            return emotion_detect(pic_path, model_path), len(faces)
        else:
            my_emotions = []
            for (x, y, w, h) in faces:
                pic = cv2.imread(pic_path)
                image_pix = pic[y - 10:y + h + 10, x - 10:x + w + 10, :]
                img_name_save = "%d.jpg" % number
                cv2.imwrite(img_name_save, image_pix)
                emo = emotion_detect(img_name_save, model_path)
                my_emotions.append(emo)
                dist_path = 'static/image/target_img%d.jpg' % number
                number += 1
                if number > 1000:
                    break
                cv2.rectangle(pic, (x, y), (x + w, y + h), (0, 255, 0), 2)
                print(dist_path)
                cv2.imwrite(dist_path, pic)
                # font = cv2.FONT_HERSHEY_SIMPLEX
                # cv2.putText(pic, emo, (x + 30, y + 30), font, 1, (255, 0, 255))
            return my_emotions, len(faces)
    print(dist_path)
    cv2.imwrite(dist_path, pic)
    return emotion_detect(pic_path, model_path), len(faces)


def emotion_detect(pic_path, model_path):
    if not pic_path.endswith('.jpg'):
        if not pic_path.endswith('.png'):
            if not pic_path.endswith('.jepg'):
                return '输入非图片格式！'

    fsize = os.path.getsize(pic_path)
    fsize /= float(1024 * 1024)
    if fsize > 9:
        return '文件过大！'

    if not is_valid(pic_path):
        return '文件损毁！'
    try:
        f = os.open(model_path, 0)
        os.close(f)
    except FileNotFoundError:
        return '模型文件丢失！'
    model = keras.models.load_model("my_model3.h5")
    img = image.load_img(pic_path, target_size=(48, 48), color_mode="grayscale")
    xaa = image.img_to_array(img)
    xaa = np.expand_dims(xaa, axis=0)

    images = np.vstack([xaa])
    classes = model.predict(images, batch_size=10)
    tmp = 0.0
    num = -1
    for i in range(7):
        if classes[0][i] > tmp:
            tmp = classes[0][i]
            num = i
    emo = emotions[num]
    num += 1
    return emo


def bd_emo(emotion):
    if emotion == 'neutral':
        return '无情绪'
    elif emotion == 'happy':
        return '高兴'
    elif emotion == 'surprise':
        return '惊讶'
    elif emotion == 'sad':
        return '伤心'
    elif emotion == 'angry':
        return '愤怒'
    elif emotion == 'disgust':
        return '厌恶'
    elif emotion == 'fear':
        return '恐惧'
    elif emotion == 'pouty':
        return '撇嘴'
    elif emotion == 'grimace':
        return '鬼脸'
    else:
        return emotion


def bd_expression(expression):
    if expression == 'none':
        return '不笑'
    elif expression == 'smile':
        return '微笑'
    elif expression == 'laugh':
        return '大笑'
    else:
        return expression


def bd_glasses(glasses):
    if glasses == 'none':
        return '无眼镜'
    elif glasses == 'common':
        return '眼镜'
    elif glasses == 'sun':
        return '太阳镜'
    else:
        return glasses


# process_img('../static/image/original_img.jpg', 'my_model4.h5')


def bd_race(race):
    if race == 'yellow':
        return '亚洲人'
    elif race == 'white':
        return '白人'
    elif race == 'black':
        return '黑人'
    else:
        return race
