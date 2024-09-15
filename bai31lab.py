# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 18:02:07 2024

@author: Nguyễn Phú Quỳnh Như
"""
a = int(input("Nhập vào số nguyên dương a: "))
b = int(input("Nhập vào số nguyên dương b: "))
c = int(input("Nhập vào số nguyên dương c: "))
while a < 0 or b < 0 or c < 0:
    if a < 0:
        a = int(input("Nhập lại a:"))
    if b < 0:
        b = int(input("Nhập lại b:"))
    if c < 0:
        c = int(input("Nhập lại c:"))
if a + b > c or a + c > b or b + c > a:
    if a == b == c:
        print("Ba cạnh a,b,c tạo thành tam giác đều")
    elif pow(a, 2) + pow(b, 2) == pow(c, 2) or pow(a, 2) + pow(c, 2) == pow(b, 2) or pow(b, 2) + pow(c, 2) == pow(a, 2):
        print("Ba cạnh a,b,c tạo thành tam giác vuông")
    elif a == b != c or a == c != b or b == c != a:
        print("Ba cạnh a,b,c tạo thành tam giác cân")
    elif (pow(a, 2) + pow(b, 2) == pow(c, 2) and a == b != c) or \
         (pow(a, 2) + pow(c, 2) == pow(b, 2) and a == c != b) or \
         (pow(b, 2) + pow(c, 2) == pow(a, 2) and b == c != a):
        print("Ba cạnh a,b,c tạo thành tam giác vuông cân")
    else:
        print("Ba cạnh a,b,c tạo thành tam giác thường")
else:
    print("Ba cạnh a,b,c không là tam giác")
        
