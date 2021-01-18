# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
input_line = input()
N = len(input_line)
str_to_leet = {"A":"4", "E":"3", "G":"6", "I":"1", "O":"0", "S":"5", "Z":"2"}

for i in range(N):
    string = input_line[i]
    print(string)
    if input_line[i] == "A":
        input_line[i]="4"
    if input_line[i] == "E":
        input_line[i]="3"
    if input_line[i] == "G":
        input_line[i]="6"
    if input_line[i] == "I":
        input_line[i]="1"
    if input_line[i] == "O":
        input_line[i]="0"
    if input_line[i] == "S":
        input_line[i]="5"
    if input_line[i] == "Z":
        input_line[i]="2"
        
    # print(input_line[i])
print(input_line)