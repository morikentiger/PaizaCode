# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
import random

num_plus, num_minus = [int(x) for x in input().split()]
# print(num_plus, num_minus)
# print("XXXXXX")

N = num_plus + num_minus

def random_calc(num_for, plusT_or_minusF):
    for i in range(num_for):
        random_int1 = random.randint(0, 99)
        random_int2 = random.randint(0, 99)
        while random_int1==random_int2:
            random_int2 = random.randint(0, 99)
            
        if plusT_or_minusF == True:
            print(str(random_int1) + ' + ' + str(random_int2) + ' =')
        else:
            print(str(random_int1) + ' - ' + str(random_int2) + ' =')
            
random_calc(num_plus,True)
random_calc(num_minus, False)