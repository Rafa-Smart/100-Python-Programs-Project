# ini adalah program menghitung luas,keliling, dan vomume tabung dengan lambda
# dibuat pada 13/10/2024
# dibuat oleh Rafa Khadafi

import os
os.system("cls")
print(30*"\033[92m=")
print("PROGRAM TABUNG LAMBDA")
print(30*"\033[92m=")

PHI = 22/7

def input_user():
    global r
    global tinggi
    r = float(input("masukan jari jari tabung = "))
    tinggi = float(input("masukan nilai tinggi tabung = "))
    return r,tinggi
r,tinggi = input_user()

luas_tabung = lambda r,PHI : r ** 2 * PHI
keliling_tabung = lambda r,PHI : r * 2 * PHI
volume_tabung = lambda r,tinggi,PHI : r ** 2 * PHI * tinggi


print(f"hasil perhitungan luas tabung = {luas_tabung(r,PHI):.2f}")
print(f"hasil perhitungan keliling tabung = {keliling_tabung(r,PHI):.2f}")
print(f"hasil perhitungan volume tabung = {volume_tabung(r,tinggi,PHI):.2f}")