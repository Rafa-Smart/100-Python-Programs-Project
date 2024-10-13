# ini merupakan sebuah program luas dan keliling jajar genjang dengan lambda
# di buat pada 10/10/2024
# di buat oleh Rafa Khadafi
import os
os.system("cls")
print(30*"\033[92m=")
print("PROGRAM JAJAR GENJANG LAMBDA")
print(30*"\033[92m=")

def input_user():
    '''mengambil input user'''
    panjang_alas = float(input('masukan nilai panjang sisi = '))
    sisi_miring = float(input("masukan nilai sisi miring = "))
    tinggi = float(input("masukan nilai tinggi = "))
    return panjang_alas,sisi_miring,tinggi

'''menghitung luas jajar genjang'''
luas_jajar_genjang = lambda panjang_alas,tinggi:panjang_alas * tinggi

'''menghitung keliling jajar genjang'''
keliling_jajar_genjang = lambda panjang_alas,sisi_miring:2 * panjang_alas + sisi_miring

panjang_alas,sisi_miring,tinggi = input_user()

print(f"hasil perhitungan luas = {luas_jajar_genjang(panjang_alas,tinggi):.2f}")
print(f"hasil perhitungan keliling = {keliling_jajar_genjang(panjang_alas,sisi_miring):.2f}")
