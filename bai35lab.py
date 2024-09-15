# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 18:12:32 2024

@author: Nguyễn Phú Quỳnh Như
"""
so_nguyen = int(input("Nhập một số nguyên dương n: "))
if so_nguyen > 0:
    S = 0
    for i in range(1, so_nguyen + 1):
        S += i
    print("Kết quả là: ", S)
else:
    print("Vui lòng nhập số nguyên dương")
