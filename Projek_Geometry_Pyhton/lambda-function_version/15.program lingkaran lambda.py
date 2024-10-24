# ini merupakan sebuah program luas dan keliling lingkaran dengan lambda
# di buat pada 08/10/2024
# di buat oleh Rafa Khadafi
import os
os.system("cls")
print(30*"\033[92m=")
print("PROGRAM LINGKARAN LAMBDA")
print(30*"\033[92m=")

PHI = 22/7

def input_user():
    '''mengambil input dari user'''
    r = float(input("masukan jari jari lingkaran = "))
    return r

'''rumus menghitung luas lingkaran'''
luas_lingkaran = lambda r : r ** 2 * PHI

'''rumus menghitung keliling lingkaran'''
keliling_lingkaran = lambda r : 2 * PHI * r

r = input_user()
print(f"hasil perhitungan luas lingkaran = {luas_lingkaran(r):.2f}")
print(f"hasil perhitungan keliling lingkaran = {keliling_lingkaran(r):.2f}")