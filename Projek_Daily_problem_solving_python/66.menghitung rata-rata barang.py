#ini adalah program menghitung rata rata barang
# dibuat pada 05/11/2024
# dibuat oleh rafa khadafi
import os
os.system("cls")
print(30*"\033[92m=")
print("PROGRAM MENGHITUNG RATA RATA BARANG".center(30))
print(30*"\033[92m=")
barang_1 = float(input("masukan harga barang 1 = "))
barang_2 = float(input("masukan harga barang 2 = "))
barang_3 = float(input("masukan harga barang 3 = "))
jumlah = barang_1 + barang_2 + barang_3
hasil_akhir = jumlah / 20.000
print(f"anda berhasil mendapatkan point = {hasil_akhir}")