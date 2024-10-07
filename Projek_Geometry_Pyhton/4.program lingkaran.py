# ini adalah program menghitung rumus luas dan keliling
# dari lingkaran pada 24/09/2024
# dibuat oleh rafa khadafi

import os
PHI = 22/7
def header():
    os.system("cls")
    '''menampilkan header'''
    print("="*20)
    print("PROGRAM LINGKARAN")
    print("="*20)

def inputan():
    '''inputan dari user'''
    r = float(input("masukan jari jari lingkaran = "))
    return r

def luas(r):
    '''menghitung luas lingkaran'''
    LUAS = (r ** 2) * PHI
    return LUAS

def keliling(r):
    '''mnghitung keliling lingkaran'''
    KELILING = 2 * PHI * r
    return KELILING

def display(pesan,value):
    '''menampilkan output ke layar'''
    print(f"hasil perhitungan {pesan} adalah {value}")

header()
ispilihan = str(input("apakah anda ingin menghitung luas,keliling,keduanya = "))
if ispilihan == "luas":
    r = inputan()
    LUAS = luas(r)
    display(f"luas lingkaran",f"{LUAS:.2f}")
elif ispilihan == "keliling":
    r = inputan()
    KELILING = keliling(r)
    display(f"luas keliling",f"{KELILING:.2f}")
elif ispilihan == "keduanya":
    r = inputan()
    LUAS = luas(r)
    display(f"luas lingkaran",f"{LUAS:.2f}")
    r = inputan()
    KELILING = keliling(r)
    display(f"luas keliling",f"{KELILING:.2f}")
else:
        print("pilihan anda tidak ada")


print("terima kasih")