import os
def header():
    print(20*"=")
    print("PROGRAM MENGHITUNG SEGITIGA")
    print(20*"=")


def input_user_luas():
     alas = float(input("masukan nilai alas = "))
     tinggi = float(input("masukan nilai tinggi = "))
     return alas,tinggi

def input_user_keliling():
     a = float(input("masukan nilai a = "))
     b = float(input("masukan nilai b = "))
     c = float(input("masukan nilai c = "))
     return a,b,c

def luas(alas,tinggi):
     hasil_luas = alas * tinggi  / 2
     return hasil_luas

def keliling(a,b,c):
     hasil_keliling = a + b + c
     return hasil_keliling

def display(pesan,value):
    print(f"hasil perhitungan {pesan} = {value} ")


while True:
     header()
     pilihan = str(input("apakah anda ingin (luas,keliling,keduanya) ? = "))
     if pilihan == "luas":
        lebar,panjang = input_user_luas()
        LUAS = luas(lebar,panjang)
        display(f"luas",LUAS)
     elif pilihan == "keliling":
        a,b,c = input_user_keliling()
        KELILING = keliling(a,b,c)
        display(f"keliling",KELILING)
     elif pilihan == "keduanya":
        # luas
        lebar,panjang = input_user_luas()
        LUAS = luas(lebar,panjang)
        display(f"luas",LUAS)
        # keliling
        a,b,c = input_user_keliling()
        KELILING = keliling(a,b,c)
        display(f"keliling",KELILING)

        iscontinue = input("apakah sudah beres (y/n) ? = ")
        if iscontinue == "n":
            break
print("terima kasih")