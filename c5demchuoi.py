# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 18:56:10 2024

@author: Nguyễn Phú Quỳnh Như
"""

chuoi = (input("Nhập vào chuỗi: "))
print("Độ dài của chuỗi là: ", len(chuoi))
ktdb = ['!', '@', '#', '$', '%', '^', '&', '*', '( )', '-', '=', '+', '.', '/']
dem_ktdb = 0
for i in chuoi:
    if i in ktdb:
        print("Kí tự đặc biệt là: ", i, "\t")
        dem_ktdb += 1
print("Số kí tự đặc biệt là: ", dem_ktdb)
dem_ki_tu_thuong = 0
for e in chuoi:
    if e.islower():
        print("Kí tự thường là: ", e, "\t")
        dem_ki_tu_thuong += 1
print("Số kí tự thường là: ", dem_ki_tu_thuong)
dem_ki_tu_so = 0
so = ["1", '2', '3', '4', '5', '6', '7', '8', '9']
for m in chuoi:
    if m in so:
        dem_ki_tu_so += 1
print("Số kí tự số là: ", dem_ki_tu_so)
dem_ki_tu_hoa = 0
for n in chuoi:
    if n.isupper():
        dem_ki_tu_hoa += 1
print("Số kí tự in hoa là: ", dem_ki_tu_hoa)