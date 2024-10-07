# ini adalah program menghitung rumus luas dan volume
# dari balok pada 05/10/2024
# dibuat oleh rafa khadafi

import os
def header():
    '''header'''
    os.system("cls")
    os.system("cls")
    print("="*20)
    print("PROGRAM BALOK")
    print("="*20)

def input_user():
    '''mengambil input dari user'''
    P = int(input("masukan nilai panjang balok = "))
    L = int(input("masukan nilai lebar balok = "))
    T = int(input("masukan nilai tinggi balok = "))
    return P,L,T

def volume(P,L,T):
    # menghitung volume balok
    global VOLUME
    VOLUME = P * L * T
    return VOLUME

def luas(P,L,T):
    # menghitung luas balok
    global LUAS
    LUAS = 2 * (P * L + P * T + L * T)
    return VOLUME

def display(value,pesan):
    # menampilkan output
    print(f"hasil perhitungan {value} adalah {pesan}")

ispilihan = str(input("anda ingin menghitung volume,luas,keduanya ? = "))
if ispilihan == "volume":
    P,L,T = input_user()
    VOLUME = volume(P,L,T)
    display(f"volume balok",f"{VOLUME:.2f}")
elif ispilihan == luas:
    P,L,T = input_user()
    LUAS = luas(P,L,T)
    display(f"luas balok",f"{LUAS:.2f}")
elif ispilihan == "keduanya":
    P,L,T = input_user()
    VOLUME = volume(P,L,T)
    display(f"volume balok",f"{VOLUME:.2f}")
    LUAS = luas(P,L,T)
    display(f"luas balok",f"{LUAS:.2f}")
else : 
    print("pilihan anda tidak tersedia")
print("TERIMA KASIH")
