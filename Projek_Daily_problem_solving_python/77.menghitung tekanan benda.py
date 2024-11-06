#ini adalah program menghitung tekanan bneda
# dibuat pada 06/11/2024
# dibuat oleh rafa khadafi

import os
os.system("cls")
print(30*"\033[92m=")
print("PROGRAM MENGHITUNG TEKANAN BENDA".center(30))
print(30*"\033[92m=")

while True:
    try:
        gaya = float(input("berapa besaran gaya benda (n) = "))
        luas = float(input("berapa luas permukaan benda tempat gaya diterapkan (m2) = "))
        tekanan = gaya / luas
        print(f"tekanan benda ini adalah = {tekanan:.2f} J")
        while True:
            isdone = str(input("apakah masih mau lagi (y/t) = "))
            if isdone == "y":
                break
            elif isdone == "t":
                exit()
                break
    except ValueError:
        print("inputan anda tidak valid ")
        print("silahkan masukan bilangan bertipe float saja")