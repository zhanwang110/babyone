#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件 :翻译.py
@说明 :python
@时间 :2022/04/21 19:36:15
@作者 :张大婶
@版本 :3.9
'''

import requests
import json
import time
import random
import hashlib
#1.确认网址
r = str(int(time.time()*1000))
l=random.randint(0,9)
i = r +str(l)



url='https://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
#1.2参数提供
def data_new(e):
    str = "fanyideskweb" + e + i + "Ygy_4c=r#e#4EX^NUGUc5"
    md5 = hashlib.md5()
    md5.update(str.encode())
    sign=md5.hexdigest()

    data ={
            'i':e,
        'from':'AUTO',
        'to':'AUTO',
        'smartresult':'dict',
        'client':'fanyideskweb',
        'salt':i,
        'sign':sign,
        'lts':r,
        'bv':'ac3968199d18b7367b2479d1f4938ac2',
        'doctype':'json',
        'version':'2.1',
        'keyfrom':'fanyi.web',
        'action':'FY_BY_REALTlME',
    }
    return data
head ={
    'Host': 'fanyi.youdao.com',
'Origin': 'https://fanyi.youdao.com',
'Referer': 'https://fanyi.youdao.com/',
'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': "Windows",
'Sec-Fetch-Dest': 'empty',
'Sec-Fetch-Mode': 'cors',
'Sec-Fetch-Site': 'same-origin',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ,AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
'X-Requested-With': 'XMLHttpRequest',
}
data = data_new(input('请输入想翻译的词：\n'))
#2.请求
req =requests.post(url,data=data,headers=head).text
print(req)
#3.删选数据
dict_str =json.loads(req)
print(dict_str['translateResult'][0][0]['tgt'])
