import os

def header():
    '''header'''
    os.system("cls")
    print("="*20)
    print("PROGRAM PERSEGI")
    print("="*20)

def inputan():
    '''inputan user'''
    s = int(input("silahkan masukan nilai sisi persegi = "))
    return s

def luas(s):
    '''menghitung luas'''
    LUAS = s ** 2
    return LUAS

def keliling(s):
    '''menghitung keliling'''
    KELILING = s * 4
    return KELILING



header()
ispilihan = str(input("pilih apakah anda ingin menghitung (luas,keliling,keduanya) = "))
if ispilihan == "luas":
    s = inputan()
    LUAS = luas(s)
    print(f"hasil perhitungan dari luas segitiga adalah = {LUAS}")
elif ispilihan == "keliling":
    s = inputan()
    KELILING = keliling(s)
    print(f"hasil perhitungan dari keliling segitiga adalah = {KELILING}")
elif ispilihan == "keduanya":
    s = inputan()
    LUAS = luas(s)
    print(f"hasil perhitungan dari luas segitiga adalah = {LUAS}")
    s = inputan()
    KELILING = keliling(s)
    print(f"hasil perhitungan dari keliling segitiga adalah = {KELILING}")
else:
    print("pilihan yang anda tidak tersedia")
   
print("TERIMA KASIH")
 
        