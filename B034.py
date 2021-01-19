# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
# input_line = input()
# print("XXXXXX")
s_x, s_y = [int(x) for x in input().split()]
# print(s_x, s_y)

d_f, d_r, d_b, d_l = [int(x) for x in input().split()]
# print(d_f, d_r, d_b, d_l)

N = int(input())
# print(N)

move_list = []
for i in range(N):
    move_list.append(i)
# print(move_list)
for i in range(N):
    move_input = input()
    # print(i, N)
    move_list[i] = move_input.split()
# print(move_list)

# print(move_list[N-1][1])

def posXY(s_x, s_y, m_l):
    # print(s_x, s_y, m_l)
    x = s_x
    y = s_y
    dir = 0
    for i in range(N):
        
        
        if m_l[i][0] == 't':
            # ターン時の処理
            # print('turn')
            if m_l[i][1] == 'F':
                dir += 0
            if m_l[i][1] == 'R':
                dir += 1
            if m_l[i][1] == 'B':
                dir += 2
            if m_l[i][1] == 'L':
                dir += 3
            if dir >= 4:
                dir -= 4
            # print(x, y, dir)
        if m_l[i][0] == 'm':
            # 直進時の処理
            # print('front')
            if dir == 0: # 前向き
                if m_l[i][1] == 'F':
                    y += d_f
                if m_l[i][1] == 'R':
                    x += d_r
                if m_l[i][1] == 'B':
                    y -= d_b
                if m_l[i][1] == 'L':
                    x -= d_l
                # print(x, y, dir)
                # print( d_f, d_r, d_b, d_l)
            if dir == 1: # 右向き
                if m_l[i][1] == 'F':
                    x += d_f
                if m_l[i][1] == 'R':
                    y -= d_r
                if m_l[i][1] == 'B':
                    x -= d_b
                if m_l[i][1] == 'L':
                    y += d_l
                
            if dir == 2: # 後ろ向き
                if m_l[i][1] == 'F':
                    y -= d_f
                if m_l[i][1] == 'R':
                    x -= d_r
                if m_l[i][1] == 'B':
                    y += d_b
                if m_l[i][1] == 'L':
                    x += d_l
            
            if dir == 3: # 左向き
                if m_l[i][1] == 'F':
                    x -= d_f
                if m_l[i][1] == 'R':
                    y += d_r
                if m_l[i][1] == 'B':
                    x += d_b
                if m_l[i][1] == 'L':
                    y -= d_l
                
        # print(x, y, dir)
    
    return (x, y)
    
n_x, n_y = posXY(s_x, s_y,  move_list)
print(n_x, n_y)

# for i in range(N):
#     if move_list[i] == 'm':
#       print('m') 

# for y in range(2):
#     for x in range(N):
#         print(move_list[x][y])
        
        