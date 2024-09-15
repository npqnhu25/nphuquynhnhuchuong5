# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 18:57:31 2024

@author: Nguyễn Phú Quỳnh Như
"""

import random
lua_chon = ["kéo", "búa", "bao"]
so_nguoi_choi = random.randrange(8, 21)
ketqua_nguoi_choi = []
for i in range(so_nguoi_choi):
    ketqua = random.choice(lua_chon)
    ketqua_nguoi_choi += [ketqua]
    print(f"Kết quả của người chơi {i+1} là: {ketqua}")
print("\nSo sánh kết quả giữa các người chơi:")
for i in range(so_nguoi_choi - 1):
    ketqua_1 = ketqua_nguoi_choi[i]
    ketqua_2 = ketqua_nguoi_choi[i + 1]
    print(f"Người chơi {i+1} ({ketqua_1}) vs Người chơi {i+2} ({ketqua_2})")
    if ketqua_1 == ketqua_2:
        print("Kết quả: Hòa")
    elif (ketqua_1 == "kéo" and ketqua_2 == "bao") or \
         (ketqua_1 == "bao" and ketqua_2 == "búa") or \
         (ketqua_1 == "búa" and ketqua_2 == "kéo"):
        print(f"Kết quả: Người chơi {i+1} thắng!")
    else:
        print(f"Kết quả: Người chơi {i+2} thắng!")
    print("-" * 20)
    