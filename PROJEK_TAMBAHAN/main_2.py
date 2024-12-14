#ini adalah ujian
# dibuat pada 05/11/2024
# dibuat oleh rafa khadafi
import os
os.system("cls")
print(30*"\033[92m=")
print("PROGRAM MENGHITUNG TABUNG".center(30))
print(30*"\033[92m=")

angka = int(input("masukan angka = "))
jumlah_hasil = 0
for i in range(angka + 1):
    if i % 2 != 0:
        jumlah_hasil += i
print(jumlah_hasil)