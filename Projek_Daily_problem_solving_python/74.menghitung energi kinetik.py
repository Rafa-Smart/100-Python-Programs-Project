#ini adalah program menghitung energi kinetik
# dibuat pada 06/11/2024
# dibuat oleh rafa khadafi

import os
os.system("cls")
print(30*"\033[92m=")
print("PROGRAM MENGHITUNG ENERGI KINETIK".center(30))
print(30*"\033[92m=")

while True:
    try:
        massa = float(input("masukan massa sebuah benda (kg) = "))
        kecepatan = float(input("masukan kecepatan benda (m/s) = "))
        energi_kinetik = 1/2 * massa * (kecepatan ** 2)
        print(f"energi kinetik benda ini adalah = {energi_kinetik:.2f}")
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