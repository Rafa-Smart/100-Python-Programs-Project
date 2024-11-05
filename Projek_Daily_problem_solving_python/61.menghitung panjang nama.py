#ini adalah Program menghitung panjang nama 
# dibuat pada 27/10/2024
# dibuat oleh rafa khadafi
import os
os.system("cls")
print(30*"\033[92m=")
print("PROGRAM MENGHITUNG PANJANG NAMA")
print(30*"\033[92m=")
print()

while True:
    try:
        input_nama = str(input("masukan nama anda = "))
        panjang_nama = len(input_nama)
        print(f"panjang nama anda adalah = {panjang_nama}")
        while True:
            isdone = str(input("apakah sudah beres ? (y/t) = "))
            if isdone == "y":
                break
            elif isdone == "t":
                print("TERIMA KASIH")
                exit()
            else:
                print("masukan y/t saja")
                break
    except ValueError:
        print("inputan anda tidak valid")
        print("masukan inputan bertipe string saja")