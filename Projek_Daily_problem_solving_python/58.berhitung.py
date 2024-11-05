# ini adalah program berhitung
# dibuat pada 26/10/2024
# dibuat oleh rafa khadafi
import os
os.system("cls")
print(30*"\033[92m=")
print("PROGRAM BERHITUNG")
print(30*"\033[92m=")
print()
while True:
    try:
        input_no = int(input("masukan nilai berhitung = "))
        input_pesan = str(input("masukan pesan = "))
        for i in range(input_no):
            print(f"{i+1}.{input_pesan}")
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