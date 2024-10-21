# ini merupakan sebuah program menghitung hasil tabungan tahunan
# di buat pada 18/10/2024
# di buat oleh Rafa Khadafi
import os
os.system("cls")
print(30*"\033[92m=")
print("PROGRAM MENGHITUNG HASIL TABUNGAN DALAM TAHUNAN")
print(30*"\033[92m=")

'''variable'''
BULAN = 12
MINGGU = 52
HARI = 365

def input_user():
    global input_tahun
    global input_uang
    input_tahun = int(input("masukan jumlah tahun menabung = "))
    input_uang = int(input("masukan nominal uang yang ingin ditabung = "))
    return input_tahun,input_uang

def hasil_menabung():
    global hasil_menabung_user
    hasil_menabung_user = input_tahun * input_uang 
    return hasil_menabung_user


input_masa = str(input("apakah anda ingin menabung per (hari,minggu,bulan) = "))

if input_masa == "hari":
    input_tahun,input_masa = input_user()
    hasil_1 = hasil_menabung_user = hasil_menabung() * HARI
    print(f"dalam {input_tahun} tahun anda menabung uang rp.{input_uang} per hari\nanda mendapakan = rp.{hasil_1:,}")
elif input_masa == "minggu":
    input_tahun,input_masa = input_user()
    hasil_2 = hasil_menabung_user = hasil_menabung() * MINGGU
    print(f"dalam {input_tahun} tahun anda menabung uang rp.{input_uang} per minggu\nanda mendapakan = rp.{hasil_2:,}")
elif input_masa == "bulan":
    input_tahun,input_masa = input_user()
    hasil_3 = hasil_menabung_user = hasil_menabung() * BULAN
    print(f"dalam {input_tahun} tahun anda menabung uang rp.{input_uang} per bulan\nanda mendapakan = rp.{hasil_3:,}")
else:
    print("anda salah memilih pilihan !\npilihannya hanya \nhari,minggu,bulan")
print("terima kasih")