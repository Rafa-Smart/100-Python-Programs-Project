#ini adalah ujian
# dibuat pada 05/11/2024
# dibuat oleh rafa khadafi
import os
os.system("cls")
print(30*"\033[92m=")
print("PROGRAM MENENTUKAN ZAT".center(30))
print(30*"\033[92m=")
print()
data_nilai = []
input = int(input("masukan jumlah data = "))
for i in range(input):
    data = int(input(f"masukan nilai -{i+1} = "))
    data_nilai.append(data)
nilai_terbesar = data_nilai[0]
nilai_terkecil = data_nilai[0]

for i in data_nilai:
    if i > nilai_terbesar:
        nilai_terbesar = i
    elif i < nilai_terkecil:
        nilai_terkecil = i
print(f"nilai terbesar = {nilai_terbesar}")
print(f"nilai terkecil = {nilai_terkecil}")
    