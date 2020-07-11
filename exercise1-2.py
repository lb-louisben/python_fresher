#-*- codeing = utf-8 -*-
#@Time : 2020/7/10 0010 16:48
#@Author : 李博_1910120228
#@File : exercise1-2.py
#@Software : PyCharm

user = input("你输入的：")
import random
x = random.randint(0,2) 
if (user==0):
    if(x==0):
        print("平局")
    elif(x==1):
        print("哈哈，你输了")
    else:
        print("你赢了")
elif (user==1):
    if(x==0):
        print("你赢了")
    elif(x==1):
        print("平局")
    else:
        print("哈哈，你输了")
elif (user==2):
    if(x==0):
        print("哈哈，你输了")
    elif(x==1):
        print("平局")
    else:
        print("你赢了")