# -*- coding:utf-8 -*-

from http import cookiejar
import os
import json
import random
import time
from typing import AsyncContextManager
import urllib
import http
import re
import io
import js2py
import execjs

import numpy as np
from numpy.core.defchararray import decode, encode, join, replace
from numpy.lib import arrayterator
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




# 解析JS混淆用


def jsHunXiao():

    a0_0xca16 = ['Latin1', 'OFB', '[object Array]', 'Word', 'sigBytes', '_keyPriorReset', 'words', 'mode', 'ZeroPadding', 'HMAC', 'split', '_iv', 'min', 'string', 'hasOwnProperty', 'prototype', '_rBlock', '_createHmacHelper', 'callback', 'finalize', '_keySchedule', 'Encryptor', 'formatter', 'SHA512', 'call', '_des1', 'indexOf', 'blockSize', 'abs', 'decryptBlock', 'StreamCipher', 'floor', '_nRounds', 'object', '_nDataBytes', '&auto_statistic=', 'HmacSHA384', 'enc', 'function', '0123456789ABCDEF', '_doReset', 'traceid', 'Cipher', 'PasswordBasedCipher', 'charCodeAt', 'Base', 'stringify', 'location', 'high', 'HmacMD5', 'fromCharCode', 'mixIn', 'BlockCipherMode', 'OpenSSL', 'cfg', 'version', 'SHA1', 'elapsed', 'parse', 'substr', 'algo', '{eventType:na-moonshad-error}', '_subKeys', 'HmacSHA512', 'max', '_state', 'length', 'moonshad8moonsh6', 'AES', 'byteOffset', 'execute', 'screen', '_invKeySchedule', 'HmacSHA256', 'moonshadV3', '_oKey', '_reverseMap', 'padding', 'sig', 'HmacRIPEMD160', 'low', 'Decryptor', '_lBlock', '_DEC_XFORM_MODE', '_hasher', 'clamp', 'SerializableCipher', 'pad', 'Rabbit', 'SHA3', 'x64', 'keySize', '//nsclick.baidu.com/v.gif?pid=111&type=1023&v=', 'decrypt', 'SHA384', 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/', 'pow', 'CFB', 'ivSize', 'CBC', '&data_source=fe', 'EvpKDF', 'key', '__esModule', 'isArray', '&auto_en=na-monitor', 'alg',
                 'round', 'WordArray', 'moonshad5moonsh2', 'processBlock', 'undefined', 'toX32', 'outputLength', '_hash', '$super', '_mode', 'iterations', '_doCryptBlock', 'time', 'exports', 'width', 'unpad', 'update', '_cipher', 'BufferedBlockAlgorithm', 'default', 'getTime', 'replace', 'BlockCipher', 'encrypt', 'CipherParams', 'Utf16', '_map', 'sin', 'toStringTag', '_createHelper', 'Hex', 'compute', '0123456789abcdef', '&module=wapna', 'apply', 'Module', 'moonshad3moonsh0', 'reset', '__creator', 'hasher', 'height', 'concat', 'MD5', 'protocol', 'TripleDES', 'CTRGladman', 'createEncryptor', 'HmacSHA3', 'RC4', '_append', '_doProcessBlock', '_counter', 'Iso10126', 'toString', 'defineProperty', '&extrajson=', 'lib', '[object Object]', 'encryption', '_ENC_XFORM_MODE', 'ceil', 'charAt', '_xformMode', 'shaOne', 'init', 'HmacSHA1', '_keystream', 'Utf16LE', 'slice', 'kdf', 'encryptBlock', '_invSubKeys', '_key', 'ciphertext', 'create', 'extend', 'null', 'join', 'Utf8', 'moonshad1moonsh9', 'random', 'Pkcs7', 'PBKDF2', '_data', 'SHA256', 'sort', '_des3', 'RIPEMD160', 'Malformed UTF-8 data', '_doFinalize', 'splice', '_minBufferSize', 'clone', 'buffer', 'NoPadding', '&monitorType=moonshadErrors', 'CTR', 'moonshad0moonsh1', 'Iso97971', 'byteLength', '_process', '_parse', 'JSON', 'ECB', 'sqrt', '_iKey', 'push', 'substring', 'salt', 'format', 'createDecryptor', '_prevBlock', 'SHA224', '_des2', 'Hasher']

    file = []

    with open("./baidu/0005.js", 'r') as f:
        file = f.readlines()

    pattern = re.compile(r"\('0x(.*?)'\)")

    def _sub(matched):
        n = matched.group()
        # print(n[2:-2])
        m = int(f"{n[2:-2]}", 16)
        return f"('{a0_0xca16[m]}')"

    tem = []
    for i in range(len(file)):
        # 用sub函数进行替换
        # repl 传入的是一个函数
        tem.append(re.sub(pattern, _sub, file[i]))

    with open('./baidu/0006.js', 'w') as f:
        for i in range(len(tem)):
            f.write(tem[i])
