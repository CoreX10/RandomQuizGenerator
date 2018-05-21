#!python3
#coding=utf-8

import os
import re
import pprint
import shelve
#定义一个正则表达式找到所有保存在states.txt文件中的state和capital.
statesRegex = re.compile(r'([A-Z][a-z]+\.?)( [A-Z]?[a-z]+)?( [A-Z]?[a-z]+)?')
#读取states文本数据
text = open('E:\\learnpython\\RandomQuizGenerator\\states.txt','r')
Text = text.read()
#查找
states_capitals = statesRegex.findall(Text)
#关闭text
text.close()

#定义一个shelve文件本地保存所有的states和capital >> mydata
shelfFile = shelve.open('mydata')

#定义空字典capitals存放数据
capitals = {}
#定义空列表存放capital，方便设置3个错误选项
capitals_list = []
#定义states列表
states_list = []

for i in range(0,len(states_capitals),2):

    #取出state和cpital组合在一起
    strStates = ''
    strCapitals = ''
    for j in range(3):
        strStates += ' ' + states_capitals[i][j]
        strCapitals += ' ' + states_capitals[i+1][j]

    #strip()方法去除左右空格
    strStates = strStates.strip()
    strCapitals = strCapitals.strip()

    #保存states和capital >> mydata
    shelfFile[strStates] = strCapitals

    #保存states到states_list中
    states_list.append(strStates)
    #保存capital到capitals_lsit中
    capitals_list.append(strCapitals)

    #setdefault方法写入capitals{}
    capitals.setdefault(strStates,strCapitals)

#关闭shelfFile
shelfFile.close()