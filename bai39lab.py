# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 18:18:07 2024

@author: Dell
"""

n = int(input("Nhập vào số nguyên dương n: "))
S = 0
while n <= 0:
    n = int(input("Nhập lại n: "))
for i in range(1, n + 1):
    S += (1 / i)
    S = float(S)
print("Tổng là: ", S)
