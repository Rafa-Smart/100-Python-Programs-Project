#ini adalah program perulangan kalimat
# dibuat pada 05/11/2024
# dibuat oleh rafa khadafi
import os
os.system("cls")
print(30 * "\033[38;5;13m=")
print("PROGRAM PERULANGAN KALIMAT".center(30))
print(30 * "\033[38;5;13m=")
print()

inputan_jumlah = int(input("masukan jumlah perulangan = "))
inputan_kalimat = str(input("masukan kalimat yang ingin diulang = "))
for i in range(inputan_jumlah):
    print(f"{i + 1}.{inputan_kalimat}.")