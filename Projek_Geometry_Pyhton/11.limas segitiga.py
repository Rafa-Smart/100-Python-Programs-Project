# ini adalah program menghitung rumus luas dan volume
# dari limas segitiga pada 05/10/2024
# dibuat oleh rafa khadafi

import os

def header():
    '''header'''
    os.system("cls")
    print("="*20)
    print("PROGRAM LIMAS SEGITIGA")
    print("="*20)

def input_user():
    '''mengambil input dari user'''
    a = int(input("masukan nilai alas segitiga = "))
    t = int(input("masukan nilai tinggi segitiga = "))
    T = int(input("masukan nilai tinggi limas = "))
    return a, t, T

def volume(a, t, T):
    # menghitung volume limas segitiga
    global VOLUME
    Luas_alas = 0.5 * a * t  # luas alas segitiga
    VOLUME = (1/3) * Luas_alas * T
    return VOLUME

def luas(a, t, T):
    # menghitung luas permukaan limas segitiga
    global LUAS
    # luas alas segitiga
    Luas_alas = 0.5 * a * t 
    # Menghitung luas sisi menggunakan Pythagoras untuk tinggi sisi
    # tinggi sisi pertama
    sisi_1 = ((a/2)**2 + T**2)**0.5 
    # tinggi sisi kedua
    sisi_2 = ((a/2)**2 + T**2)**0.5 
    Luas_sisi = (0.5 * a * sisi_1) + (0.5 * a * sisi_2) + (0.5 * a * sisi_1)  # 3 sisi segitiga
    LUAS = Luas_alas + Luas_sisi
    return LUAS

def display(value, pesan):
    # menampilkan output
    print(f"hasil perhitungan {value} adalah {pesan}")

header()
ispilihan = str(input("anda ingin menghitung volume, luas, keduanya ? = "))
if ispilihan == "volume":
    a, t, T = input_user()
    VOLUME = volume(a, t, T)
    display("volume limas segitiga", f"{VOLUME:.2f}")
elif ispilihan == "luas":
    a, t, T = input_user()
    LUAS = luas(a, t, T)
    display("luas limas segitiga", f"{LUAS:.2f}")
elif ispilihan == "keduanya":
    a, t, T = input_user()
    VOLUME = volume(a, t, T)
    display("volume limas segitiga", f"{VOLUME:.2f}")
    LUAS = luas(a, t, T)
    display("luas limas segitiga", f"{LUAS:.2f}")
else: 
    print("pilihan anda tidak tersedia")
print("TERIMA KASIH")
