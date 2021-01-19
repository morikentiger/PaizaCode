# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
# input_line = input()
# print("XXXXXX")

num_h, num_w, num_k = [int(x) for x in input().split()]
# print(num_h, num_w, num_k)
magic_circle = []
for i in range(num_h):
    magic_circle.append(input())
    
# print(magic_circle)

# print(magic_circle[2][2])
max_num = 0

for i in range(num_h):
    for j in range(num_w - num_k + 1):
        # print(magic_circle[j][i])
        # if max_num <= 
        num = 0
        for k in range(num_k):
            # print(k)
            num += int(magic_circle[j + k][i])*10**(num_k - k -1) 
            # print(num)
            # print(int(magic_circle[j + k][i]))
            # print(10**(num_k - k -1) )
        # + int(magic_circle[j+1][i])*10 
        # + int(magic_circle[j+2][i]) )
        # print(num)
        if max_num < num:
            max_num = num

for i in range(num_h - num_k + 1):
    for j in range(num_w):
        # print(magic_circle[j][i])
        # if max_num <= 
        num = 0
        for k in range(num_k):
            # print(k)
            num += int(magic_circle[j][i + k])*10**(num_k - k -1) 
            # print(num)
            # print(int(magic_circle[j + k][i]))
            # print(10**(num_k - k -1) )
        # + int(magic_circle[j+1][i])*10 
        # + int(magic_circle[j+2][i]) )
        # print(num)     
        if max_num < num:
            max_num = num

print(max_num)
        