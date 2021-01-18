# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
import math
N, Dist = input().split()
N = int(N)
Dist = int(Dist)
# print(N, Dist)
Taxi_pay = []
Price = 0
Lowest_price = 1000000000000000000
Highest_price = 0
for i in range(N):
    Taxi_pay = input().split()
    Taxi_1st_dist   = int(Taxi_pay[0])
    Taxi_1st_pay    = int(Taxi_pay[1])
    Taxi_next_dist  = int(Taxi_pay[2])
    Taxi_next_pay   = int(Taxi_pay[3])
    # print(Taxi_1st_dist,Taxi_1st_pay,Taxi_next_dist,Taxi_next_pay)
    
    if Dist < Taxi_1st_dist:
        price = Taxi_1st_pay
        # print("1st", price)
        
    else:
        price = Taxi_1st_pay + math.ceil((Dist - Taxi_1st_dist)/Taxi_next_dist) * Taxi_next_pay
        # print("next", price)
    # print("price",price)
    if price >= Highest_price:
        Highest_price = price
    if price <= Lowest_price:
        Lowest_price = price
    # print("L", Lowest_price, "H", Highest_price)

print(int(Lowest_price), int(Highest_price))
        
        
        
        