# ini adalah program menghitung luas dan keliling persegi panjang dengan lambda
# dibuat pada 08/10/2024
# dibuat oleh Rafa Khadafi
import os
os.system("cls")
print(30*"\033[92m=")
print("PROGRAM PERSEGI PANJANG LAMBDA")
print(30*"\033[92m=")
sisi = int(input("masukan nilai sisi = "))
lebar = int(input("masukan nilai lebar = "))
luas = lambda s,l : s * l
keliling = lambda s,l : 2 * (s + l)

print(f"hasil luasnya adalah = {luas(sisi,lebar):.2f}")
print(f"hasil kelilingnya adalah = {keliling(sisi):.2f}")


# lmmbda itu berada didalam variable
# luas = lambda s : s * s
# nah s ini adalah variable local