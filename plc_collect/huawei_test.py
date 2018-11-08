# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 11:13:05 2018

@author: SCUTYJ
"""
#import sys
#print("linux 系统按CTRL＋D结束输入，windows按CTRL+Z结束输入")
#text=sys.stdin.read()
#print(text)

#time_list = [0 for _ in range(8)]
#a,b = 12,20
#for i in range((a-12),(b-12)):
#    time_list[i] += 1
#left_list = list(range(12,20))
#right_list = list(range(13,21))
#for i in range(8):
#    print(r'[{},{}):{}'.format(
#            left_list[i],
#            right_list[i],
#            time_list[i]))

list1 = []
list2 = []
def isint(str_):
    try:
        x = int(str_)
        return True
    except:
        return False
str_ = input()
for letter in str_:
    if letter in ('*', '^', '+'):
        list1.append(letter)
    elif isint(letter):
        list2.append(int(letter))
    elif letter == ')':
        if list1[-1] == '*':
            list2 = [list2[-1] * list2[-2]]
            list1 = list[:-1]
        elif list1[-1] == '^':
            list2 = [list2[-1] + 1]
            list1 = list[:-1]
        elif list1[-1] == '+':
            list2 = [list2[-1] + list2[-2]]
            list1 = list[:-1]
        