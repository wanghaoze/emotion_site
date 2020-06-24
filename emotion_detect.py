# 输入人脸的截图，返回情绪对应的中文
import os
import keras
import cv2
from keras.preprocessing import image
from PIL import Image
import numpy as np
emotions = {
    0: 'anger',      # 生气
    1: 'disgust',    # 厌恶
    2: 'fear',       # 恐惧
    3: 'happy',      # 开心
    4: 'sad',        # 伤心
    5: 'surprised',  # 惊讶
    6: 'normal',     # 中性
}


def is_valid(file):
    valid = True
    try:
        Image.open(file).load()
    except OSError:
        valid = False
    return valid


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

# text = emotion_detect('Pizigani_1367_Chart_10MB.jpg', 'my_model3.h5')
text = emotion_detect('111', 'my_model3.h5')
# text = emotion_detect('0.jpg', 'my_model0.h5')
# text = emotion_detect('0.jpg', 'my_model3.h5')
# text = emotion_detect('1.jpg', 'my_model3.h5')
# text = emotion_detect('2.jpg', 'my_model3.h5')
# text = emotion_detect('3.jpg', 'my_model3.h5')
# text = emotion_detect('4.jpg', 'my_model3.h5')
# text = emotion_detect('5.jpg', 'my_model3.h5')
# text = emotion_detect('6.jpg', 'my_model3.h5')
# text = emotion_detect('7.jpg', 'my_model3.h5')
print(text)

    # x,y,
    #         img_name = "%d.jpg" % num
    #         image_pix = pic[y - 10:y + h + 10, x - 10:x + w + 10, :]
    #         img_name_save = "%d.jpg" % (num % 5)
    #         cv2.imwrite(img_name_save, image_pix)
    #         img = image.load_img(img_name_save, target_size=(48, 48),color_mode="grayscale")
    #         xaa = image.img_to_array(img)
    #         xaa = np.expand_dims(xaa, axis=0)
    #
    #         images = np.vstack([xaa])
    #         classes = model.predict(images, batch_size=10)
    #         print(classes)
    #         tmp = 0.0
    #         num = -1
    #         for i in range(7):
    #             if classes[0][i] > tmp:
    #                 tmp = classes[0][i]
    #                 num = i
    #         emo = emotions[num]
    #         num += 1
    #         if num > 1000:
    #             break
    #         cv2.rectangle(pic, (x, y), (x + w, y + h), (0, 255, 0), 2)
    #         font = cv2.FONT_HERSHEY_SIMPLEX
    #         cv2.putText(pic, emo, (x + 30, y + 30), font, 1, (255, 0, 255))
    # return pic

