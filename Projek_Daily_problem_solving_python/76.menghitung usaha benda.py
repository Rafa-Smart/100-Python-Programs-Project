#ini adalah program menghitung usaha benda
# dibuat pada 06/11/2024
# dibuat oleh rafa khadafi

import os
os.system("cls")
print(30*"\033[92m=")
print("PROGRAM MENGHITUNG USAHA BENDA".center(30))
print(30*"\033[92m=")

while True:
    try:
        gaya = float(input("berapa besaran gaya benda (n) = "))
        perpindahan = float(input("berapa jauh perpindahan benda (m) = "))
        sudut = float(input("berapa besaran sudut benda (derajat) = "))
        usaha = gaya * perpindahan * sudut
        print(f"usaha benda ini adalah = {usaha:.2f} J")
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