# ini merupakan sebuah program luas dan volume kerucut dengan lambda
# di buat pada 13/10/2024
# di buat oleh Rafa Khadafi
import math
import os
os.system("cls")
print(30*"\033[92m=")
print("PROGRAM KERUCUT LAMBDA")
print(30*"\033[92m=")

PHI = 22/7
sisi_miring = math.sqrt(r**2 + tinggi**2)
LUAS_ALAS = r ** 2 * PHI
LUAS_SELIMUT = r * PHI * sisi_miring

def input_user():
    '''mengambil input user'''
    global r
    global tinggi
    r = float(input("masukan nilai jari jari = "))
    tinggi = float(input("masukan nilai tinggi kerucut = "))
    return r,tinggi
r,tinggi = input_user()

volume_kerucut = lambda r,tinggi : r ** 2 * PHI * 1/3 * tinggi
luas_kerucut = lambda LUAS_ALAS,LUAS_SELIMUT : LUAS_ALAS + LUAS_SELIMUT


print(f"hasil perhitungan volume kerucut adalah = {volume_kerucut(r,tinggi):.2f}")
print(f"hasil perhitungan luas kerucut adalah = {luas_kerucut(LUAS_ALAS,LUAS_SELIMUT):.2f}")