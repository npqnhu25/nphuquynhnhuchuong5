# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 18:08:28 2024

@author: Nguyễn Phú Quỳnh Như
"""
import math
n = int(input("Nhập vào số nguyên dương n: "))
while n <= 0:
    n = int(input("Nhập lại số n: "))
so_chinh_phuong = math.sqrt(n)
so = int(so_chinh_phuong)
kiem_tra = so * so
if n == kiem_tra:
    print("Số", n, "là số chính phương")
else:
    print("Số", n, "không là số chính phương")
    
