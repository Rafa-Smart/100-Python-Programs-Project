def header():
    '''fungsi header'''
    import os
    os.system("cls")
    print(20*"=")
    print("PROGRAM MENGHIlebar,panjang".center(40))
    print(20*"=")

def input_user():
    '''fungsi input user'''
    lebar = int(input("masukan nilai lebar persegi panjang = "))
    panjang = int(input("masukan nilai panjang persegi panjang = "))
    return lebar,panjang

def hitung_luas(lebar,panjang):
    '''hitung keliling'''
    LUAS = panjang * lebar
    return LUAS

def hitung_keliling(lebar,panjang):
    '''fungsi keliling'''
    KELILING = 2 * (lebar + panjang)
    return KELILING

def display(pesan,value):
    '''fungsi display'''
    print(f"hasil perhitungan {pesan} = {value}")


while True:
    header()
    lebar,panjang = input_user()
    LUAS = hitung_luas(lebar,panjang)
    KELILING = hitung_keliling(lebar,panjang)
    display(f"luas", KELILING)
    display(f"keliling", LUAS)


    iscontinue = input("apakah lanjut ? (y/n) = ")
    if iscontinue == "n":
        break
print("program selesai, terima kasih")

