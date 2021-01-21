# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
import math
N, M = [int(x) for x in input().split()]
# print(N, M)
# print("XXXXXX")
tree_state = input()
# print(tree_state.strip(' '))
# tree_state_list = list(tree_state)
# tree_state_list_strip = tree_state_list.strip()
# print(''.join(tree_state_list))
# print(tree_state_list_strip)
# tree_s = str(0)
# for k in range(N):

def check_trees(t_s,s,e):
    ave_t = sum(int(i) for i in t_s[s:e])/(e - s)
    # print(ave_t)
    if ave_t < M:
        # print('少ない')
        d = M - math.floor(ave_t)
        # print(d)
        for i in range(s-1, e):
            # t_s_d = int(t_s[i]) + d
            # print(t_s_d)
            tree_s[i] = int(t_s[i]) + d
            # print(tree_s)
            
    else:
        pass
        # print('多い')
    
    return tree_s


tree_s = ['0']*N
    
count = 0
for i in range(2*N -1):
    if i % 2 == 0:
        # print(tree_state[i])
        tree_s[count] = tree_state[i]
        
        count += 1
        # print('cnt', count)

# print(tree_s)
# 
Q = input()
# print(Q)

for j in range(int(Q)):
    start, end = [int(x) for x in input().split()]
    # print(start, end)
    tree_state = check_trees(tree_s, start, end)
t = [str(i) for i in tree_state]
print(" ".join(t))
# print(''.join(tree_state))

    