#ini adalah program menghitung massa jenis
# dibuat pada 06/11/2024
# dibuat oleh rafa khadafi

import os
os.system("cls")
print(30*"\033[92m=")
print("PROGRAM MENGHITUNG MASSA JENIS".center(30))
print(30*"\033[92m=")

while True:
    try:
        massa = float(input("masukan massa benda (gram) = "))
        volume_benda = float(input("masukan volume benda (cm3) = "))
        massa_jenis = massa / volume_benda
        print(f"massa jenis benda ini adalah = {massa_jenis:.2f} J")
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