# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 18:13:55 2024

@author: Nguyễn Phú Quỳnh Như
"""

n = int(input("Nhập vào số nguyên dương n: "))
S = 0
while n <= 0:
    n = int(input("Nhập lại n: "))
for i in range(1, n + 1):
    S += pow(i, 2)
print("Tổng là: ", S)
