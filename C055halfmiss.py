# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
import re

N = int(input())
# print(N)
string = input()
# print(string)

for i in range(N):
    abc = input()
    flag = 0
    if string in abc:
        print(abc)
        flag = 1
        
if flag == 0:
    print('None')
    
