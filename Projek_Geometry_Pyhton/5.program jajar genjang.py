import os

def header():
    '''Menampilkan header'''
    os.system("cls")
    print("="*20)
    print("PROGRAM JAJAR GENJANG")
    print("="*20)

def inputan_user():
    '''Mengambil input user'''
    panjang_alas = int(input("Masukan panjang alas = "))
    tinggi = int(input("Masukan nilai tinggi = "))
    sisi_miring = int(input("Masukan panjang sisi miring = "))
    return panjang_alas, tinggi, sisi_miring

def luas(panjang_alas, tinggi):
    '''Menghitung luas'''
    LUAS = panjang_alas * tinggi
    return LUAS

def keliling(panjang_alas, sisi_miring):
    '''Menghitung keliling'''
    KELILING = 2 * (panjang_alas + sisi_miring)
    return KELILING

def display(pesan, value):
    '''Menampilkan output ke monitor'''
    print(f"Hasil perhitungan {pesan} adalah {value:.2f}")

header()
ispilihan = input("Apakah anda ingin menghitung luas, keliling, keduanya? = ").strip().lower()

if ispilihan == "luas":
    panjang_alas, tinggi, _ = inputan_user()  # fungsi _ buat Mengabaikan sisi miring
    LUAS = luas(panjang_alas, tinggi)
    display("luas", LUAS)

elif ispilihan == "keliling":
    panjang_alas, _, sisi_miring = inputan_user()  # fungsi _ buat Mengabaikan tinggi
    KELILING = keliling(panjang_alas, sisi_miring)
    display("keliling", KELILING)

elif ispilihan == "keduanya":
    panjang_alas, tinggi, sisi_miring = inputan_user()
    LUAS = luas(panjang_alas, tinggi)
    KELILING = keliling(panjang_alas, sisi_miring)
    display("luas", LUAS)
    display("keliling", KELILING)

else:
    print("Pilihan anda tidak tersedia")

print("TERIMA KASIH")
