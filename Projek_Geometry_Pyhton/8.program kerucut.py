# ini adalah program menghitung luas dan keliling kerucut
# dibuat pada 25/08/2024
# dibuat oleh Rafa Khadafi
import os
import math
PHI = 22/7

def header():
    # menampilkan header
    print(20*"=")
    print("PROGRAM KERUCUT")
    print(20*"=")

def inputan_user():
    # mengambil input dari user
    r = float(input("masukan nilai jari jari alas dari kerucut = "))
    tinggi = float(input("masukan nilai tinggi dari kerucut = "))
    return r,tinggi

def volume(r,tinggi):
    # menghitung volume kerucut
    global VOLUME
    VOLUME = r ** 2 * PHI * 1/3 * tinggi
    return VOLUME

def luas(r,tinggi):
    # menghitung luas kerucut
    sisi_miring = math.sqrt(r**2 + tinggi**2)
    global LUAS_ALAS
    global LUAS_SELIMUT
    global LUAS_TOTAL_PERMUKAAN
    LUAS_ALAS = r ** 2 * PHI
    LUAS_SELIMUT = r * PHI * sisi_miring
    LUAS_TOTAL_PERMUKAAN = LUAS_ALAS + LUAS_SELIMUT
    return LUAS_ALAS,LUAS_SELIMUT,LUAS_TOTAL_PERMUKAAN

def display(pesan,value):
    print(f"hasil perhitungan {pesan} adalah {value}")

header()
ispilihan = str(input("apakah anda ingin menghitung volume,luas,keduanya ? = "))
if ispilihan == "luas":
    r,tinggi = inputan_user()
    LUAS_ALAS,LUAS_SELIMUT,LUAS_TOTAL_PERMUKAAN = luas(r,tinggi)
    display(f"luas alas",f"{LUAS_ALAS:.2f}")
    display(f"luas selimut",f"{LUAS_SELIMUT:.2f}")
    display("luas total permukaan",f"{LUAS_TOTAL_PERMUKAAN:.2f}")
elif ispilihan == "volume":
    r,tinggi = inputan_user()
    VOLUME = volume(r,tinggi)
    display(f"volume",f"{VOLUME:.2f}")
elif ispilihan == "keduanya":
    r,tinggi = inputan_user()
    LUAS_ALAS,LUAS_SELIMUT,LUAS_TOTAL_PERMUKAAN = luas(r,tinggi)
    VOLUME = volume(r,tinggi)
    display(f"volume",f"{VOLUME:.2f}")
    display(f"luas alas",f"{LUAS_ALAS:.2f}")
    display(f"luas selimut",f"{LUAS_SELIMUT:.2f}")
    display(f"luas total permukaan",f"{LUAS_TOTAL_PERMUKAAN:.2f}")
else:
    print("pilihan anda tidak tersedia")
print("TERIMA KASIH")