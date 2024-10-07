# ini adalah program menghitung luas,keliling, dan vomume tabung
# dibuat pada 26/08/2024
# dibuat oleh Rafa Khadafi
import os
PHI = 22/7
def header():
    # menampilkan header
    os.system("cls")
    print("="*20)
    print("PROGRAM TABUNG")
    print("="*20)

def inputan_user():
    # mengambil input dari user
    r = float(input("masukan nilai jari jari tabung = "))
    tinggi = float(input("masukan nilai tinggi tabung = "))
    return r,tinggi

def luas_alas(r):
    # mengitung luas alas
    LUAS = r ** 2 * PHI
    return LUAS

def keliling_alas(r):
    # mengitung keliling alas
    KELILING = r * 2 * PHI
    return KELILING

def volume(r,tinggi):
    # menghitung volume tabung
    VOLUME = r ** 2 * PHI * tinggi
    return VOLUME
def display(pesan,value):
    # menampilkan output di layar
    print(f"hasil perhitungan {pesan} adalah {value}")
header()
ispilihan = str(input("pilih : luas alas, keliing alas, volume, ketiganya ? = "))
if ispilihan == "luas alas":
    r = inputan_user()
    LUAS = luas_alas(r) 
    display(f"luas alas",f"{LUAS:.2f}")
elif ispilihan == "keliling alas":
    r = inputan_user()
    KELILING = keliling_alas(r)
    display(f"keliling alas",f"{KELILING:.2f}")
elif ispilihan == "volume":
    r,tinggi = inputan_user()
    VOLUME = volume(r,tinggi)
    display(f"volume",f"{VOLUME:.2f}")
elif ispilihan == "ketiganya":
    r,tinggi = inputan_user()
    LUAS = luas_alas(r) 
    display(f"luas alas",f"{LUAS:.2f}")
    KELILING = keliling_alas(r)
    display(f"keliling alas",f"{KELILING:.2f}")
    VOLUME = volume(r,tinggi)
    display(f"volume",f"{VOLUME:.2f}")

else:
    print("pilihan anda tidak tersedia")
print("TERIMA KASIH")