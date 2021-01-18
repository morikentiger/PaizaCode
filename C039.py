# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
line = input()
# print(line)
line_list = list(line)
# print(line_list)

cnt_k=0
cnt_l=0

for i in range(len(line)):
    # print(i)
    if line_list[i]=="<":
        cnt_k += 1
    # print(cnt_k)
    if line_list[i]=="/":
        cnt_l += 1
    
print(cnt_k*10 + cnt_l)