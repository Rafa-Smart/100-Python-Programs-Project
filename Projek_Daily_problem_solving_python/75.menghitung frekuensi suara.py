#ini adalah program menghitung frekuensi suara
# dibuat pada 06/11/2024
# dibuat oleh rafa khadafi

import os
os.system("cls")
print(30*"\033[92m=")
print("PROGRAM MENGHITUNG FREKUENSI SUARA".center(30))
print(30*"\033[92m=")

while True:
    try:
        getaran = float(input("berapa jumlah getaran benda = "))
        waktu = float(input("berapa lama waktu getaran (detik) = "))
        frekuensi = getaran / waktu
        print(f"frekuensi benda ini adalah = {frekuensi:.2f} hz")
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