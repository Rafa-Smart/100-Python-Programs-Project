# ini adalah program menghitung luas dan keliling segitiga dangan lambda
# dibuat pada 08/10/2024
# dibuat oleh Rafa Khadafi
import os
os.system("cls")
print(30*"\033[92m=")
print("PROGRAM SEGITIGA LAMBDA")
print(30*"\033[92m=")


'''mengambil input user'''
def input_user():
    alas = float(input("masukan nilai alas segitiga = "))
    tinggi = float(input("masukan nilai tinggi segitiga = "))
    a = float(input("masukan nilai a = "))
    b = float(input("masukan nilai b = "))
    c = float(input("masukan nilai a = "))
    return alas,tinggi,a,b,c

'''rumus luas segitiga'''
luas_segitiga = lambda alas,tinggi : 1/2 * alas * tinggi

'''rumus keliling segitiga'''
keliling_segitiga = lambda a,b,c : a + b + c
alas, tinggi, a, b, c = input_user()
print(f"hasil perhitungan luas = {luas_segitiga(alas,tinggi):.2f}")
print(f"hasil perhitungan keliling = {keliling_segitiga(a,b,c):.2f}")