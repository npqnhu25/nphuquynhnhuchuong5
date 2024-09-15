# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 18:58:07 2024

@author: Nguyễn Phú Quỳnh Như
"""
import random
lua_chon = ["kéo", "búa", "bao"]
ket_qua_nguoi_choi = input("Nhập sự lựa chọn của người chơi: ")
while ket_qua_nguoi_choi not in lua_chon:
    ket_qua_nguoi_choi = input("Nhập lại kết quả người chơi: ")
    if ket_qua_nguoi_choi in lua_chon:
        break
ket_qua_may = random.choice(lua_chon)
print("Kết quả máy chọn là: ", ket_qua_may)
if ket_qua_nguoi_choi == ket_qua_may:
    print("Máy và người hòa")
elif (ket_qua_nguoi_choi == "kéo" and ket_qua_may == "bao") or \
     (ket_qua_nguoi_choi == "bao" and ket_qua_may == "búa") or \
     (ket_qua_nguoi_choi == "búa" and ket_qua_may == "kéo"):
    print("Người chơi thắng")
else:
    print("Máy thắng")
