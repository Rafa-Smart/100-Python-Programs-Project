#ini adalah program menghitung tahun kabisat
# dibuat pada 05/11/2024
# dibuat oleh rafa khadafi
import os
os.system("cls")
print(30*"\033[92m=")
print("PROGRAM MENGHITUNG TAHUN KABISAT".center(30))
print(30*"\033[92m=")

#  membuat Fungsi untuk mengecek apakah tahun kabisat
def is_kabisat(tahun):
    return (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0)
# Input tahun dari user
tahun_input = int(input("Masukkan tahun: "))

# Tahun saat ini 
tahun_sekarang = 2024

jumlah_kabisat = 0
for tahun in range(tahun_input, tahun_sekarang + 1):
    if is_kabisat(tahun):
        jumlah_kabisat += 1

# Menampilkan hasil
print(f"Dari tahun {tahun_input} hingga {tahun_sekarang}, terdapat {jumlah_kabisat} tahun kabisat.")

