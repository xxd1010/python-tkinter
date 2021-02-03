# -*- coding:utf-8 -*-
from http import cookiejar
import os
import json
import random
import time
from typing import AsyncContextManager
import urllib.parse
import http
import re
import io

import numpy as np
from numpy.core.defchararray import decode, encode, replace
import pretty_errors
import requests
from PIL import Image
from pylab import *
from requests.api import post

# PIL参考文档 https://pillow.readthedocs.io/en/stable/reference/index.html


def push():
    user_dictionary = {}
    with open("USER_DICTIONARY.json", mode='r', encoding='utf-8') as f:
        user_dictionary = json.load(f)

    i = len(user_dictionary)
    user = user_dictionary[str(1)]['user']
    step_ls = user_dictionary[str(1)]['step_ls']

    user.replace(user[3:7], '****')

    ms = time.time()
    # 年月日
    today = time.strftime("%F")

    Year = int(time.strftime('%Y'))
    Month = int(time.strftime('%m'))
    Day = int(time.strftime('%d'))

    # 时分秒
    Hour = int(time.strftime('%H'))
    Minute = int(time.strftime('%M'))
    Second = int(time.strftime('%S'))

    now = f'[{Year}-{Month}-{Day} {Hour}:{Minute}:{Second}]'

    # 默认stage为 len(step_ls)
    stage = len(step_ls)

    for j in range(len(step_ls)):
        hour_array = step_ls[j]['hour_range'].split('-')
        if Hour > int(hour_array[0]) and Hour < int(hour_array[1]):
            stage = step_ls[j]['stage']
    for j in range(len(step_ls)):
        if stage == step_ls[j]['stage']:
            step_array = step_ls[j]['step_range'].split('-')
            if len(step_array) == 2:
                step = str(randint(int(step_array[0]), int(step_array[1])))
            elif str(step) == '0':
                step = ''

    # 使用Server酱推送消息
    sckey = user_dictionary[str(i)]['sckey']
    uri = f"https://sc.ftqq.com/{sckey}.send"
    desp = "http://www.bing.com"
    params = {
        'text': "通知",
        'desp': desp,
    }
    # responce = requests.get(uri, params=params)

    dict1 = user_dictionary["1"]
    dict2 = user_dictionary["2"]

# 图像处理


def imgMission():

    # 读取图像到数组
    Img = Image.open("20200129153307_dvlnw.jpg").convert('L')
    ImgArray = np.asarray(Img)

    # 新建一个图像
    # figure1 = figure()
    # 不使用颜色信息
    # gray()
    # contour(Img, origin = 'image')
    figure2 = figure()

    hist(ImgArray.flatten(), int(ImgArray.max()))
    # show()

    Height, Width = ImgArray.shape

    Img2 = 255 - ImgArray
    Img3 = (100.0/255)*ImgArray + 100
    Img4 = 255.0 * (ImgArray / 255.0)**2

    new_width = 96
    new_height = int(Height * new_width / Width)

    # np.savetxt('output1.txt', ImgArray, fmt='%d')
    # print(int(Img.min()), int(Img.max()))
    # print(int(Img2.min()), int(Img2.max()))
    # print(int(Img3.min()), int(Img3.max()))
    # print(int(Img4.min()), int(Img4.max()))

# 自定义生成火绒自定义拦截规则


def function():

    path_list = ["D:\\Program Files\\", "D:\\Program Files (x86)\\"]

    bad_file = ['BaiduNetdisk', 'LeiGod_Acc', 'MiPhoneAssistant',
                'MyTablet', 'Netease', 'Tencent', 'TTKN', 'WeGame', 'WPS Office']

    for item in range(len(bad_file)):

        exception = bad_file[item]

        dic = {
            "ver": "5.0",
            "tag": "hipsuser",
            "data": [
                {
                    "id": 9,
                    "power": 1,
                    "name": exception,
                    "procname": f"*\\{exception}\\*",
                    "treatment": 3,
                    "policies": [
                    ]
                }
            ]
        }
        custtom_policies = [
            {
                "montype": 1,
                "action_type": 2,
                "res_path": "*\\User\\*"
            },
            {
                "montype": 1,
                "action_type": 2,
                "res_path": "*\\User Data\\Default\\*"
            }
        ]

        for i in range(len(path_list)):
            list = os.listdir(path_list[i])
            for j in range(len(list)):
                if exception != list[j]:
                    dic_policies = {
                        "montype": 1,
                        "action_type": 2,
                        "res_path": ""
                    }
                    dic_policies['res_path'] = f"*\\{list[j]}\\*"
                    dic['data'][0]['policies'].append(dic_policies)

        for i in range(len(custtom_policies)):
            dic['data'][0]['policies'].append(custtom_policies[i])

        with open(f"{exception}.json", mode='w', encoding='utf-8') as f:
            json.dump(dic, f)

        print(f"{exception}.json     已完成")
        time.sleep(0.5)

# 从网络获取时间戳


def getTime():
    responce = requests.get("https://www.tsa.cn/time.jspx")
    return responce.json()

# 网络请求
# 看能不能实现登录百度


def urlRequest():

    tt = getTime()  # 服务器时间
    header = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Mobile Safari/537.36 Edg/88.0.705.56",
        "Accept": "atext/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Host": "wappass.baidu.com",
    }
    name = "想"
    passwd = "123456789"
    data = {
        "name": name,
        "password": passwd,
        "time": f"{tt/1000}",
        "tt": f"{tt}"
    }
    data = urllib.parse.urlencode(data)
    antireplaytoken = f"https://wappass.baidu.com/wp/api/security/antireplaytoken?baiduId=6759F3479F7CAE7EEE0ED6F1FC10A7C9%3AFG%3D1&tpl=undefined&tt={tt}"
    login = "https://wappass.baidu.com/wp/api/login"
    check = "https://wappass.baidu.com/v3/login/api/check"

    url_get_publickey = "https://passport.baidu.com/v2/getpublickey"

    session = requests.session()
    params = {"tt": f"{tt}", "time": f"{tt/1000}"}
    responce = session.request('get', url_get_publickey, cookies=requests.cookies.RequestsCookieJar(
    ), data=urllib.parse.urlencode(params))

    fp = "./temp.json"

    res = responce.content.decode('utf-8')

    # res = eval("{}".format(res))

    # dic = json.dumps(res)
    # ----->
    # dic = json.dumps(eval(res))
    # dic = json,loads(dic)

    # -------------json模块处理字符串时，字符串内不能使用'单引号 将单引号替换成双引号
    # new_res = res.replace("'", '"')
    # -------------eval()   太智能了,这里将 str--->---dict
    dic_pubkey = eval(res)

    # 正则匹配还行
    # pattern = r"-----BEGIN PUBLIC KEY-----\n(.*?)\n-----END PUBLIC KEY-----"

    # pattern = re.compile("{(.*?)}")
    # r = pattern.match(res)

    # with open(fp, 'r') as f:
    #     tmp = f.read()
    #     print(tmp)
    #     dic = json.load(f)
    # dic = json.loads(dic)

    print(dic_pubkey['pubkey'])

    # for name, value in responce.cookies.items():
    #     header['Cookie'] + f"{name}={value};"
    #     print(header)
    res = session.request('post', login, headers=header,
                          data=data, cookies=responce.cookies)
    json_res = res.json()


urlRequest()
