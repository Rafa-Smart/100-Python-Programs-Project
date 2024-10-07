# ini adalah program menghitung luas dan keliling lingkaran
# dibuat pada 25/08/2024
# dibuat oleh Rafa Khadafi
import os
PHI = 22/7

def header():
    # menampilkan header
    os.system("cls")
    print("="*25)
    print("PROGRAM LINGKARAN")
    print("="*25)

def inputan_user():
    # mengambil inputan dari user
    r = float(input("masukan jari jari lingkaran = "))
    return r

def luas(r):
    # menghitung luas lingkaran
    LUAS = r ** 2 * PHI
    return LUAS

def keliling(r):
    # menghtung keliling lingkaran
    KELILING = 2 * r * PHI
    return KELILING

def display(pesan,value):
    # menampilkan output
    print(f"hasil perhitungan {pesan} adalah {value}")

header()
ispilihan = str(input("apakah anda ingin menghitung luas,keliling,keduanya ? = "))
if ispilihan == "luas":
    r = inputan_user()
    LUAS = luas(r)
    display(f"luas",f"{LUAS:.2f}")
elif ispilihan == "keliling":
    r = inputan_user()
    KELILING = keliling(r)
    display(f"keliling",f"{KELILING:.2f}")
elif ispilihan == "keduanya":
    r = inputan_user()
    LUAS = luas(r)
    display(f"luas",f"{LUAS:.2f}")
    KELILING = keliling(r)
    display(f"keliling",f"{KELILING:.2f}")
else:
    print("pilihan anda tidak tersedia")
print("TERIMA KASIH")