# ini adalah program menghitung luas dan keliling jajar genjang
# dibuat pada 24/08/2024
# dibuat oleh Rafa Khadafi
import os
def header():
    '''menampilkan header'''
    os.system("cls")
    print("="*20)
    print("PROGRAM JAJAR GENJANG")
    print("="*20)

def inputan_user():
    '''mengambil input user'''
    panjang_alas = int(input("masukan panjang alas = "))
    tinggi = int(input("masukan nilai tinggi = "))
    sisi_miring = int(input("masukan panjang sisi miring = "))
    return panjang_alas,tinggi,sisi_miring

def luas(panjang_alas,tinggi):
    '''menghitung luas'''
    LUAS = panjang_alas * tinggi
    return LUAS

def keliling(sisi_miring,panjang_alas):
    '''menghitung keliling'''
    KELILING = 2 * (panjang_alas + sisi_miring)
    return KELILING

def display(pesan,value):
    '''menampilkan output ke monitor'''
    print(f"hasil perhitungan {pesan} adalah {value}")

header()
ispilihan = str(input("apakah anda ingin menghitung luas,keliling,keduanya ? = "))
if ispilihan == "luas":
    panjang_alas,tinggi = inputan_user()
    LUAS = luas(panjang_alas,tinggi)
    display(f"luas",f"{LUAS:.2f}")
elif ispilihan == "keliling":
    panjang_alas,sisi_miring = inputan_user()
    KELILING = keliling(panjang_alas,sisi_miring)
    display(f"keliling",f"{KELILING:.2f}")
elif ispilihan == "keduanya":
    panjang_alas,tinggi,sisi_miring = inputan_user()
    LUAS = luas(panjang_alas,tinggi)
    KELILING = keliling(panjang_alas,sisi_miring)
    display(f"luas",f"{LUAS:.2f}")
    display(f"keliling",f"{KELILING:.2f}")
else:
    print("pilihan anda tidak tersedia")
print("TERIMA KASIH")       