# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
input_line = input()
N = len(input_line)
str_to_leet = {"A":"4", "E":"3", "G":"6", "I":"1", "O":"0", "S":"5", "Z":"2"}
input_line = list(input_line)
# print(input_line)
for i in range(N):
    # string = input_line[i]
    # print(string)
    if input_line[i] == "A":
        input_line[i]=""
    if input_line[i] == "E":
        input_line[i]=""
    if input_line[i] == "U":
        input_line[i]=""
    if input_line[i] == "I":
        input_line[i]=""
    if input_line[i] == "O":
        input_line[i]=""
    if input_line[i] == "a":
        input_line[i]=""
    if input_line[i] == "i":
        input_line[i]=""
    if input_line[i] == "u":
        input_line[i]=""
    if input_line[i] == "e":
        input_line[i]=""
    if input_line[i] == "o":
        input_line[i]=""
        
    # print(input_line[i])

input_line="".join(input_line)
print(input_line)

# 参考URL
# https://minus9d.hatenablog.com/entry/20130528/1369745960