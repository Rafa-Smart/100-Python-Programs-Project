# ini adalah program membuat fungsi tambah dengan oop
# dibuat pada 26/10/2024
# dibuat oleh rafa khadafi
import os
os.system("cls")
print(30*"\033[92m=")
print("PROGRAM MEMBUAT PROGRAM FUNGSI TAMBAH")
print(30*"\033[92m=")
print()
print(f"nilai __name__ pada fungsi.py = '{__name__}'")
def fungsi_tambah(a:int,b:int)->int:
    return a+b
if __name__ == "__main__":
    angka_1 = int(input("masukan nilai 1 = "))
    angka_2 = int(input("masukan nilai 2 = "))
    hasil = fungsi_tambah(angka_1,angka_2)
    print(f"hasil tambah = {hasil}")