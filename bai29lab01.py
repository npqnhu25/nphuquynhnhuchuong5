# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 17:42:54 2024

@author: Nguyễn Phú Quỳnh Như
"""
N = int(input("Nhập số nguyên dương N: "))
tong_cac_chu_so = 0
while N < 0:
    N = int(input("Nhập lại số nguyên dương N: "))
for chu_so in str(N):
    tong_cac_chu_so += int(chu_so)
print("Tổng các chữ số của N là: ", tong_cac_chu_so)
