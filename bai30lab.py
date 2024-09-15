# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 17:54:17 2024

@author: Nguyễn Phú Quỳnh Nhu
"""

thoi_gian = input("Nhập ngày tháng năm (dd/mm/yyyy): ")
ngay, thang, nam = thoi_gian.split("/")
ngay = int(ngay)
thang = int(thang)
nam = int(nam)
nam_nhuan = nam % 400 == 0 or (nam % 4 == 0 and nam % 100 != 0)
if thang in [1, 3, 5, 7, 8, 10, 12]:
    print(f"Tháng {thang} có 31 ngày")
elif thang in [4, 6, 9, 11]:
    print(f"Tháng {thang} có 30 ngày")
elif thang == 2:
    if nam_nhuan:
        print("Tháng", thang, "có 29 ngày")
    else:
        print("Tháng", thang, "có 28 ngày")