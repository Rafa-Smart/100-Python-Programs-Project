# ini adalah program menghitung luas dan keliling trapesium
# dibuat pada 24/08/2024
# dibuat oleh Rafa Khadafi
import os
def header():
    '''menampilkan header'''
    os.system("cls")
    print("="*20)
    print("PROGRAM TRAPESIUM")
    print("="*20)

def inputan_user():
    '''mengambil inputan user'''
    sisi_sejajar_1 = float(input("masukan sisi sejajar 1 = "))
    sisi_sejajar_2 = float(input("masukan sisi sejajar 2 = "))
    sisi_miring_1 = float(input("masukan sisi miring 1 = "))
    sisi_miring_2 = float(input("masukan sisi miring 2 = "))
    tinggi = float(input("masukan nilai tinggi trapesium = "))
    return sisi_sejajar_1,sisi_sejajar_2,sisi_miring_1,sisi_miring_2,tinggi

def luas(sisi_sejajar_1,sisi_sejajar_2,tinggi):
    '''menghitung luas trapesium'''
    LUAS = (sisi_sejajar_1 + sisi_sejajar_2) * tinggi / 2
    return LUAS

def keliling(sisi_sejajar_1,sisi_sejajar_2,sisi_miring_1,sisi_miring_2):
    '''menghitung keliling trapesium'''
    KELILING = sisi_sejajar_1 + sisi_sejajar_2 + sisi_miring_1 + sisi_miring_2
    return KELILING

def display(pesan,value):
    '''menampilkan output ke monitor'''
    print(f"hasil perhitungan {pesan} adalah {value}")

header()
ispilihan = str(input("apakah anda ingin menghitung luas,keliling,keduanya ? = "))
if ispilihan == "luas":
    sisi_sejajar_1,sisi_sejajar_2,tinggi = inputan_user()
    LUAS = luas(sisi_sejajar_1,sisi_sejajar_2,tinggi)
    display(f"luas",f"{LUAS:.2f}")
elif ispilihan == "keliling":
    sisi_sejajar_1,sisi_sejajar_2,sisi_miring_1,sisi_miring_2 = inputan_user()
    KELILING = keliling(sisi_sejajar_1,sisi_sejajar_2,sisi_miring_1,sisi_miring_2)
    display(f"keliling",f"{KELILING}")
elif ispilihan == "keduanya":
    sisi_sejajar_1,sisi_sejajar_2,sisi_miring_1,sisi_miring_2,tinggi = inputan_user()
    LUAS = luas(sisi_sejajar_1,sisi_sejajar_2,tinggi)
    display(f"luas",f"{LUAS:.2f}")
    KELILING = keliling(sisi_sejajar_1,sisi_sejajar_2,sisi_miring_1,sisi_miring_2)
    display(f"keliling",f"{KELILING}")
else:
    print("pilihan anda tidak tersedia")
print("TERIMA KASIH")