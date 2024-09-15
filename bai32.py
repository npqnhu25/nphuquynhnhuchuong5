# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 18:05:44 2024

@author: Nguyễn Phú Quỳnh Như
"""

d = float(input("Nhập quãng đường xe đi(km): "))
while d <= 0:
    d = float("Nhập lại: ")
tien = 0
if d < 1:
    tien += d * 150000
if 2 <= d < 6:
    tien += 15000 + ((d - 1) * 13500)
if 6 <= d:
    tien += 15000 + 67500 + ((d - 6) * 11000)
if d > 120:
    tien *= 0.9
print("Số tiền của bạn là: ", tien)
