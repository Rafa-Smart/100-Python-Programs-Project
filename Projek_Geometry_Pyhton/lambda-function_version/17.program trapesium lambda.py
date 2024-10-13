# ini merupakan sebuah program luas dan keliling trapesium dengan lambda
# di buat pada 10/10/2024
# di buat oleh Rafa Khadafi
import os
os.system("cls")
print(30*"\033[92m=")
print("PROGRAM TRAPESIUM LAMBDA")
print(30*"\033[92m=")

def input_user():
    '''mengambil inputan user'''
    sisi_sejajar_1 = float(input("masukan sisi sejajar 1 = "))
    sisi_sejajar_2 = float(input("masukan sisi sejajar 2 = "))
    sisi_miring_1 = float(input("masukan sisi miring 1 = "))
    sisi_miring_2 = float(input("masukan sisi miring 2 = "))
    tinggi = float(input("masukan nilai tinggi trapesium = "))
    return sisi_sejajar_1,sisi_sejajar_2,sisi_miring_1,sisi_miring_2,tinggi

'''menghitung luas trapesiuum'''
luas_trapesium = lambda sisi_sejajar_1,sisi_sejajar_2,tinggi:(sisi_sejajar_1 + sisi_sejajar_2) * tinggi / 2

'''luas keliling trapesium'''
keliling_trapesium = lambda sisi_sejajar_1,sisi_sejajar_2,sisi_miring_1,sisi_miring_2:sisi_sejajar_1 + sisi_sejajar_2 + sisi_miring_1 + sisi_miring_2

sisi_sejajar_1,sisi_sejajar_2,sisi_miring_1,sisi_sejajar_2,tinggi = input_user()


print(f"hasil perhitungan luas = {luas_trapesium(sisi_sejajar_1,sisi_sejajar_2,tinggi):.2f}")
print(f"hasil perhitungan keliling = {keliling_trapesium(sisi_sejajar_1,sisi_sejajar_2,sisi_miring_1,sisi_sejajar_2):.2f}")
