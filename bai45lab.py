# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 18:34:47 2024

@author: Nguyễn Phú Quỳnh Như
"""
x = float(input("Nhập giá trị cho biến x: "))
n = int(input("Nhập vào số nguyên dương n: "))
S = 0
s = 0
while n <= 0:
    n = int(input("Nhập lại n: "))
for i in range(1, n + 1):
    s = sum(range(1, i + 1))
    S += pow(x, i) / s
    S = float(S)
print("Tổng là: ", S)
