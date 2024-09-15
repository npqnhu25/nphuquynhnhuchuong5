# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 18:39:31 2024

@author: Nguyễn Phú Quỳnh Như
"""
print("Cho phương trình:", "\n", "2x + 7y + 9z = 979 với (x,y,z > 0)")
bo_nghiem = []
print("Bộ nghiệm nguyên của phương trình là: ")
for x in range(1, (int(979 // 2) + 1)):
    for y in range(1, (int((979 - (2 * x)) // 7)) + 1):
        for z in range(1, (int((979 - (2 * x) - (7 * y)) // 9)) + 1):
            if (2 * x) + (7 * y) + (9 * z) == 979:
                bo_nghiem += [[x, y, z]]
                print(f"(x={x}, y={y}, z={z})")
min_nghiem = bo_nghiem[0]
min_tong = sum(min_nghiem)
for nghiem in bo_nghiem:
    tong = sum(nghiem)
    if tong < min_tong:
        min_tong = tong
        min_nghiem = nghiem
print("Bộ nghiệm có tổng bé nhất là:", min_nghiem, "với tổng:", min_tong)
