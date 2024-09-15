# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 17:53:13 2024

@author: Nguyễn Phú Quỳnh Như
"""

N = int(input("Nhập vào số nguyên dương N: "))
uoc_so = []
while N < 0:
    N = int(input("Nhập lại sô nguyên dương"))
for i in range(1, N + 1):
    uoc_so += [i]
print(uoc_so)