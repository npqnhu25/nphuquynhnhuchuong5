# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 19:01:15 2024

@author: Nguyễn Phú Quỳnh Như

"""
giai_thua = 1 
n = int(input("nhập số nguyên n:"))
for i in range(1, n + 1): 
    giai_thua = giai_thua * i 
if n >= 0:
    print(f"giai thừa của {n} là {giai_thua}")
    
    