# ini adalah program menghitung rumus luas dan volume dengan lambda
# dari limas segitiga pada 13/10/2024
# dibuat oleh rafa khadafi

import os
os.system("cls")
print(30*"\033[92m=")
print("PROGRAM LIMAS SEGITIGA LAMBDA")
print(30*"\033[92m=")

def input_user():
    '''mengambil input dari user'''
    global a 
    global t 
    global T
    a = int(input("masukan nilai alas segitiga = "))
    t = int(input("masukan nilai tinggi segitiga = "))
    T = int(input("masukan nilai tinggi limas = "))
    return a, t, T

a,t,T = input_user()
'''beberapa variable'''
Luas_alas = 0.5 * a * t  # luas alas segitiga
sisi_1 = ((a/2)**2 + T**2)**0.5 # tinggi sisi pertama
sisi_2 = ((a/2)**2 + T**2)**0.5 # tinggi sisi kedua
Luas_sisi = (0.5 * a * sisi_1) + (0.5 * a * sisi_2) + (0.5 * a * sisi_1)  # 3 sisi segitiga


volume_limas_segitiga = lambda T : (1/3) * Luas_alas * T
luas_limas_segitiga = lambda Luas_alas,Luas_sisi : Luas_alas + Luas_sisi


print(f"hasil perhitungan volume limas segitiga = {volume_limas_segitiga(T):.2f}")
print(f"hasil perhitungan luas limas segitiga = {luas_limas_segitiga(Luas_alas,Luas_sisi):.2f} ")