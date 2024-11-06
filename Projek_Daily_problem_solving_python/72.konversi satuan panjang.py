#ini adalah program menghitung konversi
# dibuat pada 05/11/2024
# dibuat oleh rafa khadafi

import os
os.system("cls")
print(30*"\033[92m=")
print("PROGRAM MENGHITUNG KONVERSI".center(30))
print(30*"\033[92m=")


while True:
    try:
        inputan = int(input("masukan satuan meter = "))
        mllimeter = inputan * 1000
        sentimeter = inputan * 100
        dekameter = inputan % 10
        hektometer = inputan % 100
        kilometer = inputan % 1000
        print(f"""hasil konversi meter {inputan}\nmilimeter = {mllimeter}\nsentimeter = {sentimeter}\ndekameter = {dekameter}\nhektometer = {hektometer}\nkilometer = {kilometer}""")
        while True:
            isdone = str(input("apakah sudah beres ? (y/t) = "))
            if isdone == "t":
                break
            elif isdone == "y":
                print("TERIMA KASIH")
                exit()
            else:
                print("masukan y/t saja")
                break
    except ValueError:
        print("inputan anda tidak valid")
        print("masukan inputan bertipe integer saja")