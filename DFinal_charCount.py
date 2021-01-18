# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
char = input()
str = input()
len = len(str)
# print(char, str, len)

str_list = list(str)
# print(str_list)

count = 0

for i in range(len):
    if str_list[i]==char:
        count += 1

print(count)