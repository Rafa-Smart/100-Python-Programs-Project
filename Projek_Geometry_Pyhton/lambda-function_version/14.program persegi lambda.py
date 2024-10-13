# ini adalah program menghitung luas dan keliling persegi dengan lambda
# dibuat pada 08/10/2024
# dibuat oleh Rafa Khadafi
import os
os.system("cls")
print(30*"\033[92m=")
print("PROGRAM PERSEGI LAMBDA".center(30))
print(30*"\033[92m=")

'''mengambil input user'''
def input_user():
    sisi = float(input("masukan nilai sisi persegi = "))
    return sisi

'''menghitung luas persegi'''
luas_persegi = lambda sisi : sisi ** 2

'''menghitung keliling persegi'''
keliling_persegi = lambda sisi : sisi * 4

sisi = input_user()
print(f"hasil perhitungan luas persegi = {luas_persegi(sisi):.2f}")
print(f"hasil perhitungan keliling persegi = {keliling_persegi(sisi):.2f}")
