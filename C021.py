# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
xc, yc, r_1, r_2= [int(x) for x in input().split()]
n = int(input())
# print(xc, yc, r_1, r_2, n)
# print("XXXXXX")

def hantei(x, y):
    if r_1**2 <= (x - xc)**2 + (y - yc)**2 <= r_2**2:
        print('yes')
    else:
        print('no')

point = [] * n

for i in range(n):
    # point = input()
    # point_list = list(point)
    # # point = (' ').join(point_list)
    # # point = (' ').join(point)
    # point = map(str, point_list)
    # point = "".join(point)
    # print(point_list)
    # print(point)
    # point = list(point)
    # print(int(point[0][0]), int(point[0][1]) )
    x, y = [int(j) for j in input().split()]
    hantei(x, y)
    
    
    # print(point)
point_list = list(point)
    # print(point_list)
    
# print(point)