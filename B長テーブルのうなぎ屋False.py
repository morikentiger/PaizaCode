# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
# import numpy as np

num_seat, m = [int(x) for x in input().split()]
print(num_seat, m)

consumer = []
for i in range(m):
    consumer.append(0)
    
for i in range(m):
    consumer[i] = [int(x) for x in input().split()]

print(consumer)

seats = [False] * num_seat
print(seats)
    
for i in range(m):
    # 座席の空席判定
    index_start = int(consumer[i][1]) 
    index_end = int(consumer[i][1])+int(consumer[i][0])
    
    print(index_start, index_end)
    # print( seats[index_start:index_end])
    print( seats[index_start:num_seat])
    print( seats[index_end - num_seat: index_end - num_seat + index_start])
    if(index_end > num_seat):
        print('座席渡り')
    
    elif seats[int(consumer[i][1]):int(consumer[i][1])+int(consumer[i][0])] == [False] * consumer[i][]:
        print('空席')
    # 座席の在席状態への遷移
    
    # 着席数のカウント（計上）
# print(consumer[0:m-1][1])
# print(consumer[1][0:m-1])

# print(consumer[0:2][1])
# print(consumer[1][0:2])

# print(consumer[0:m][1])
# print(consumer[1][0:m])

# print(consumer[:2, 1:])
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
# import numpy as np

num_seat, m = [int(x) for x in input().split()]
print(num_seat, m)

consumer = []
for i in range(m):
    consumer.append(0)
    
for i in range(m):
    consumer[i] = [int(x) for x in input().split()]

print(consumer)

seats = [False] * num_seat
print(seats)
    
for i in range(m):
    # 座席の空席判定
    index_start = int(consumer[i][1]) 
    index_end = int(consumer[i][1])+int(consumer[i][0])
    
    print(index_start, index_end)
    # print( seats[index_start:index_end])
    print( seats[index_start:num_seat])
    print( seats[index_end - num_seat: index_end - num_seat + index_start])
    if(index_end > num_seat):
        print('座席渡り')
    
    elif seats[int(consumer[i][1]):int(consumer[i][1])+int(consumer[i][0])] == [False] * consumer[i][]:
        print('空席')
    # 座席の在席状態への遷移
    
    # 着席数のカウント（計上）
# print(consumer[0:m-1][1])
# print(consumer[1][0:m-1])

# print(consumer[0:2][1])
# print(consumer[1][0:2])

# print(consumer[0:m][1])
# print(consumer[1][0:m])

# print(consumer[:2, 1:])
