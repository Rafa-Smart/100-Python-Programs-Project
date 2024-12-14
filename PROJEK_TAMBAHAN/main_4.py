#ini adalah ujian
# dibuat pada 05/11/2024
# dibuat oleh rafa khadafi
import os
os.system("cls")
print(30*"\033[92m=")
print("PROGRAM MENGHITUNG POINT".center(30))
print(30*"\033[92m=")

# tahun_sekarang = 2024
# tahun = int(input("masukan tahun lahir = "))

# if tahun % 4 == 0 and tahun % 100 != 0 or tahun % 400 == 0:
#     # karena and ga bisa 3 kali maka pake or
#     print(f"tahun = {tahun} adalah tahun kabisat")
# print()
# def iskabisat(tahun:int) -> bool:
#     if tahun % 4 == 0 and tahun % 100 != 0 or tahun % 400 == 0 :
#         return print(f"{tahun} = kabisat")
#     else:
#         return print(f"{tahun} = bukan kabisat")
# iskabisat(2000)


tahun_sekarang = 2024
tahun = int(input("masukan tahun lahir = "))
jumlah_kabisat = 0

for i in range(tahun,tahun_sekarang + 1):
    if i % 4 == 0 and i % 100 != 0 or i % 400 == 0:
        jumlah_kabisat += 1
            
        print(f"jumlah tahun kabisat dari 2009 ke - {jumlah_kabisat} = {i}\n")