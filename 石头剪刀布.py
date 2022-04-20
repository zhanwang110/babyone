#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件 :test.py
@说明 :python
@时间 :2022/04/14 16:31:26
@作者 :张大婶
@版本 :3.9
'''
import random
a = random.randint(0,2)
b = int(input("请输入:石头(0),剪刀(1),布(2)"))
if  b >= 2 or b <= 0:
    print("输入错误")
else:
    print("输入正确,开始游戏")
    if b == 0 and a ==1:
        print("电脑出剪刀")
        print("玩家出石头")
        print("玩家胜利")
    elif b == 1 and a ==2:
        print("电脑出布")
        print("玩家出剪刀")
        print("玩家胜利")
    elif b == 2 and a ==0:
        print("电脑出石头")
        print("玩家出布")
        print("玩家胜利")
    elif b==1 and a==1 or b==2 and a==2 or b==0 and a==0:
        print("平局")

    else:
        print("玩家输了")
