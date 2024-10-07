import os
def header():
    os.system("cls")
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



header()
pilihan = str(input("apakah anda ingin (luas,keliling,keduanya) ? = "))
if pilihan == "luas":
     lebar,panjang = input_user_luas()
     hasil_luas = luas(lebar,panjang)
     display(f"luas",hasil_luas)
elif pilihan == "keliling":
     a,b,c = input_user_keliling()
     hasil_keliling = keliling(a,b,c)
     display(f"keliling",hasil_keliling)
elif pilihan == "keduanya":
        # luas
     lebar,panjang = input_user_luas()
     hasil_luas = luas(lebar,panjang)
     display(f"luas",hasil_luas)
        # keliling
     a,b,c = input_user_keliling()
     hasil_keliling = keliling(a,b,c)
     display(f"keliling",hasil_keliling)
print("terima kasih")