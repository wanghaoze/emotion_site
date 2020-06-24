# This Python file uses the following encoding: utf-8
from django.shortcuts import render, redirect
from django.urls import reverse
# Create your views here.
from django.views import generic
from emotion_detect.models import Img
from PIL import ImageDraw
# from PIL import Image
# import cv2
# from keras.preprocessing import image
# import os
# import keras
# import numpy as np
# from aip import AipFace
import base64
import json
from .tests import *


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'


def begin(request):
    if request.method == "POST":
        file = request.FILES.get('myfile')
        print(file)
        with open('static/image/2222.jpg', 'wb') as f:
            for chunk in file.chunks():
                f.write(chunk)
        process_img('static/image/2222.jpg', 'my_model4.h5')
        return redirect(reverse("show_file"))
    return render(request, 'emotion_detect/begin.html')


def home(request):
    return render(request, "emotion_detect/base.html")


def begin_input(request):
    return render(request, "emotion_detect/begin_input.html")


def show_file(request):
    content = {}
    if request.method == 'POST':
        file = request.FILES.get("myfile")
        if file is None:
            return render(request, 'emotion_detect/begin.html', context=content)
        with open('static/image/' + str(request.FILES['myfile']), 'wb') as f:  # 写文件
            for chunk in file.chunks():
                f.write(chunk)
        with open('static/image/original_img.jpg', 'wb') as f:  # 写文件
            for chunk in file.chunks():
                f.write(chunk)
    content['Photo'] = "./static/image/" + str(request.FILES['myfile'])
    # 将百度接口返回的数据转成json对象
    if isNetChainOK():  # 有网络情况下使用百度api进行识别
        with open("./static/image/" + str(request.FILES['myfile']), "rb") as f:  # 读文件
            base64_data = base64.b64encode(f.read())
            image = str(base64_data, encoding='utf-8')
            result = client.detect(image, imageType, options)
        json_str = json.dumps(result)
        print(json_str)
        # 对数据进行解码
        json_data = json.loads(json_str)
        print(json_data)
        if 'result' not in json_data.keys():
            return render(request, 'emotion_detect/begin.html')
        if json_data['result'] is None:
            content['no_face'] = 1
            return render(request, 'emotion_detect/begin_no_face.html')
        if json_data['result']['face_num'] == 1:
            content['age'] = json_data['result']['face_list'][0]['age']
            content['beauty'] = json_data['result']['face_list'][0]['beauty']
            gender = json_data['result']['face_list'][0]['gender']['type']
            content['gender_pro'] = str(json_data['result']['face_list'][0]['gender']['probability'] * 100) + '%'
            if gender == 'female':
                content['gender'] = "女性"
            else:
                content['gender'] = "男性"
            emotion = json_data['result']['face_list'][0]['emotion']['type']
            content['emotion'] = bd_emo(emotion)
            content['emotion_pro'] = str(json_data['result']['face_list'][0]['emotion']['probability'] * 100) + '%'
            expression = json_data['result']['face_list'][0]['expression']['type']
            content['expression'] = bd_expression(expression)
            content['expression_pro'] = str(
                json_data['result']['face_list'][0]['expression']['probability'] * 100) + '%'
            race = json_data['result']['face_list'][0]['race']['type']
            content['race'] = bd_race(race)
            content['race_pro'] = str(json_data['result']['face_list'][0]['race']['probability'] * 100) + '%'
            glasses = json_data['result']['face_list'][0]['glasses']['type']
            content['glasses'] = bd_glasses(glasses)
            content['glasses_pro'] = str(json_data['result']['face_list'][0]['glasses']['probability'] * 100) + '%'
            landmark72 = json_data['result']['face_list'][0]['landmark72']
            # or1 = Image.open("./static/image/" + str(request.FILES['myfile']))
            # or1.save("static/image/original_img.jpg")
            im1 = Image.open("./static/image/" + str(request.FILES['myfile']))
            draw = ImageDraw.Draw(im1)
            # 保存图片比例为100：1左右
            width = im1.size[0]
            height = im1.size[1]
            siz = 1
            if min(width, height) > 100:
                siz = int(min(width, height) / 100)
            for index in range(72):
                xy = landmark72[index]
                yy = xy['y'] - int(siz / 2)
                for i in range(siz):
                    xx = xy['x'] - int(siz / 2)
                    for j in range(siz):
                        draw.point((xx, yy))
                        # print(xx, yy)
                        xx += 1
                    yy += 1
                    # draw.point((xy['x'], xy['y']))
                # draw.text((xy['x'], xy['y']), "o", (255, 255, 0))
            draw = ImageDraw.Draw(im1)
            im1.save("static/image/target_img.jpg")
            content['target_img'] = "/static/image/target_img.jpg"
            content['original_img'] = "/static/image/original_img.jpg"  #
        if json_data['result']['face_num'] != 1:
            arr = []
            fkk = 0
            for xxx in range(json_data['result']['face_num']):
                arr.append(str(fkk))
                fkk += 1
            content['img_num'] = arr
            for i in range(json_data['result']['face_num']):
                content['age'+str(i)] = json_data['result']['face_list'][i]['age']
                content['beauty'+str(i)] = json_data['result']['face_list'][i]['beauty']
                gender = json_data['result']['face_list'][i]['gender']['type']
                content['gender_pro'+str(i)] = str(json_data['result']['face_list'][i]['gender']['probability']*100)+'%'
                if gender == 'female':
                    content['gender'+str(i)] = "女性"
                else:
                    content['gender'+str(i)] = "男性"
                emotion = json_data['result']['face_list'][i]['emotion']['type']
                content['emotion'+str(i)] = bd_emo(emotion)
                content['emotion_pro'+str(i)] = str(json_data['result']['face_list'][i]['emotion']['probability']*100)+'%'
                expression = json_data['result']['face_list'][i]['expression']['type']
                content['expression'+str(i)] = bd_expression(expression)
                content['expression_pro'+str(i)] = str(
                    json_data['result']['face_list'][i]['expression']['probability'] * 100) + '%'
                race = json_data['result']['face_list'][i]['race']['type']
                content['race'+str(i)] = bd_race(race)
                content['race_pro'+str(i)] = str(json_data['result']['face_list'][i]['race']['probability'] * 100) + '%'
                glasses = json_data['result']['face_list'][i]['glasses']['type']
                content['glasses'+str(i)] = bd_glasses(glasses)
                content['glasses_pro'+str(i)] = str(json_data['result']['face_list'][i]['glasses']['probability']*100)+'%'
                landmark72 = json_data['result']['face_list'][i]['landmark72']
                or1 = Image.open("./static/image/" + str(request.FILES['myfile']))
                or1.save("static/image/original_img.jpg")
                im1 = Image.open("./static/image/" + str(request.FILES['myfile']))
                draw = ImageDraw.Draw(im1)
                # 保存图片比例为100：1左右
                width = im1.size[0]
                height = im1.size[1]
                siz = 1
                if min(width, height) > 100:
                    siz = int(min(width, height) / 100)
                for index in range(72):
                    xy = landmark72[index]
                    yy = xy['y'] - int(siz / 2)
                    for lll in range(siz):
                        xx = xy['x'] - int(siz / 2)
                        for j in range(siz):
                            draw.point((xx, yy))
                            # print(xx, yy)
                            xx += 1
                        yy += 1
                        # draw.point((xy['x'], xy['y']))
                    # draw.text((xy['x'], xy['y']), "o", (255, 255, 0))
                draw = ImageDraw.Draw(im1)
                im1.save("static/image/target_img%d.jpg" % i)
                content['target_img%d' % i] = "/static/image/target_img%d.jpg" % i
            print(content)
            content['original_img'] = "/static/image/original_img.jpg"  #
            return render(request, 'emotion_detect/show_file_multiple_face.html', context=content)
            # or1 = Image.open("./static/image/" + str(request.FILES['myfile']))
            # # or1.save("static/image/original_img.jpg")
            # im1 = Image.open("./static/image/" + str(request.FILES['myfile']))
            # draw = ImageDraw.Draw(im1)
            # # 保存图片比例为100：1左右
            # width = im1.size[0]
            # height = im1.size[1]
            # siz = 1
            # if min(width, height) > 100:
            #     siz = int(min(width, height) / 100)
            # for index in range(72):
            #     xy = landmark72[index]
            #     yy = xy['y'] - int(siz / 2)
            #     for i in range(siz):
            #         xx = xy['x'] - int(siz / 2)
            #         for j in range(siz):
            #             draw.point((xx, yy))
            #             # print(xx, yy)
            #             xx += 1
            #         yy += 1
            #         # draw.point((xy['x'], xy['y']))
            #     # draw.text((xy['x'], xy['y']), "o", (255, 255, 0))
            # draw = ImageDraw.Draw(im1)
            # im1.save("static/image/target_img.jpg")
            # content['target_img'] = "/static/image/target_img.jpg"
            # content['original_img'] = "/static/image/original_img.jpg"  #

    else:  # 无网络情况下使用本地模型处理
        eeeemmm, face_num = process_img('static/image/original_img.jpg', 'my_model4.h5')
        if face_num == 0:
            content['no_face'] = 1
            return render(request, 'emotion_detect/begin_no_face.html')
        elif face_num == 1:
            content['emotion'] = eeeemmm
            content['emotion_pro'] = '57%'
            content['target_img'] = "/static/image/target_img.jpg"
            content['original_img'] = "/static/image/original_img.jpg"  #
            return render(request, "emotion_detect/show_file.html", context=content)
        else:
            arr = []
            fkk = 0
            for xxx in range(face_num):
                arr.append(str(fkk))
                fkk += 1
            content['img_num'] = arr
            for i in range(face_num):
                content['emotion'+str(i)] = eeeemmm[i]
                content['emotion_pro'+str(i)] = '57%'
            return render(request, "emotion_detect/show_file_multiple_face.html", context=content)
    return render(request, "emotion_detect/show_file.html", context=content)


def showImg(request):
    imgs = Img.objects.all()  # 从数据库中取出所有的图片路径
    context = {
        'imgs': imgs
    }
    return render(request, 'emotion_detect/showImg.html', context)


def test(request):
    return render(request, 'emotion_detect/tasks0.html')
