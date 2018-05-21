#!python3
#coding=utf-8

import shelve
import findStates
import random
import os

#定义四个答案的方法
def fourAnswers(random_states):
    #shelve方法读取本地保存的数据
    shelfFile = shelve.open('mydata')
    rightAnswer = []
    rightAnswer.append(shelfFile[random_states])
    shelfFile.close()
    #capital_list除去正确选项
    capital_list_1 = capital_list * 1
    capital_list_1.remove(rightAnswer[0])
    wrongAnswer = random.sample(capital_list_1,3)
    return rightAnswer + wrongAnswer

if os.path.exists('E:\\learnpython\\RandomQuizGenerator\\Gengraphy'):
    print('请稍等......')
else:
        #创建Generator文件夹
        os.makedirs('E:\\learnpython\\RandomQuizGenerator\\Gengraphy')
        print('请稍等......')

if os.path.exists('E:\\learnpython\\RandomQuizGenerator\\Gengraphy_Answer'):
    print('\n')
else:
        #创建Generator_Answer文件夹
        os.makedirs('E:\\learnpython\\RandomQuizGenerator\\Gengraphy_Answer')

#循环35次,35张试卷,35张答案
for i in range(35):

    #define numbers,title and information.
    Numbers = i
    Title =       '*****************Geography Test*****************\n\n'
    Title_2 =     '****************Geography_Answer****************\n\n'
    Information = 'Name:___________       School number____________\n\n'
    #print(Title)
    #print(Information)

    #open file with add.(GeographyFile)
    GeographyFile = open('E:\\learnpython\\RandomQuizGenerator\\Gengraphy\\Gengraphy_'+str(Numbers)+'.txt','a')
    GeographyFile.write(Title)
    GeographyFile.write(Information)
    #open file with add.(GeographyFile_Answer)
    GeographyFile_Answer = open('E:\\learnpython\\RandomQuizGenerator\\Gengraphy_Answer\\Gengraphy_Answer_'+str(Numbers)+'.txt','a')
    GeographyFile.write(Title_2)

    #复制state和capital的列表
    states_list = findStates.states_list * 1
    capital_list = findStates.capitals_list * 1
    #设置选项
    option = ('A. ','B. ','C. ','D. ')
    #设置正确答案的列表，用于写入答案的文件
    RightAnswerList = []
    
    #The quiz data. Keys are states and values are their capitals.
    for j in range(1,51):
        #选出一个题目
        random_states = random.sample(states_list,1)
        #print(str(j) + '. What is the capital of ' + random_states[0] + '?\n')
        #写入题目
        GeographyFile.write(str(j) + '. What is the capital of ' + random_states[0] + '?\n')
        states_list.remove(random_states[0]) 
        #设置四个选项的列表
        Answers = fourAnswers(random_states[0])
        
        for o in option:
            Option = str(random.sample(Answers,1)[0])
            #判断是否为正确答案，若是，保存到RightAnswerList中
            if Option == findStates.capitals[random_states[0]]:
                RightAnswerList += o[0]
            #print('    ' + o + Option + '\n')
            #写入选项
            GeographyFile.write('    ' + o + Option + '\n')
            Answers.remove(Option)

    #写入答案
    for ans in range(len(RightAnswerList)): 
        GeographyFile_Answer.write(str(ans+1) + '. ' + RightAnswerList[ans] + '\n')
    
    #close the file        
    GeographyFile.close()
    GeographyFile_Answer.close()

    #print(RightAnswerList)

print('创建完成!')
           




    