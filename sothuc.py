# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 19:07:57 2024

@author: Nguyễn Phú Quỳnh Như
"""
import random
so_luong = random.randint(20, 30)
so_thuc = [random.uniform(18, 99) for _ in range (so_luong)]
binh_phuong = [x ** 2 for x in so_thuc]
print(f"số lượng phần tử: {so_luong}")
print(f"các số thực ngẫu nhiên: {so_thuc}")
print(f"các giá trị bình phương: {binh_phuong}")

