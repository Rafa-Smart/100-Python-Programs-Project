# ini merupakan sebuah program menentukan jumlah protein ideal perhari
# di buat pada 18/10/2024
# di buat oleh Rafa Khadafi
import os
os.system("cls")
print(35*"\033[34m=")
print("\033[31mPROGRAM MENENTUKAN JUMLAH PROTEIN  HARIAN".center(40))
print(35*"\033[34m=")

kelamin = str(input("masukan jenis kelamin anda (cowok/cewek) = "))
umur = int(input("masukan umur anda = "))
# 1-3 tahun: 14 gram
# 4-8 tahun: 19 gram
# 9-13 tahun: 34 gram
# Remaja:
# 14-18 tahun:
# Laki-laki: 52 gram
# Perempuan: 46 gram
# Dewasa:
# 19-50 tahun:
# Laki-laki: 56 gram
# Perempuan: 46 gram
# 51 tahun ke atas:
# Laki-laki: 56 gram
# Perempuan: 46 gram     
if kelamin == "cowok":
    if 1 <= umur <= 3:
        print("kamu masih anak anak")
        print("protein yang harus kamu konsumsi perhari\n adalah 14 gram") 
    elif 4 <= umur <= 8:
        print("kamu masih anak anak")
        print("protein yang harus kamu konsumsi perhari\n adalah 19 gram") 
    elif 9 <= umur <= 13:
        print("kamu masih anak anak")
        print("protein yang harus kamu konsumsi perhari\n adalah 34 gram") 
    elif 14 <= umur <= 18:
        print("kamu sudah remaja")
        print("protein yang harus kamu konsumsi perhari\n adalah 52 gram") 
    elif 19 <= umur <= 50:
        print("kamu sudah dewasa")
        print("protein yang harus kamu konsumsi perhari\n adalah 56 gram") 
    elif umur < 51:
        print("kamu sudah manula")
        print("protein yang harus kamu konsumsi perhari\n adalah 56 gram") 
elif kelamin == "cewek":
    if 1 <= umur <= 3:
        print("kamu masih anak anak")
        print("protein yang harus kamu konsumsi perhari\n adalah 14 gram") 
    elif 4 <= umur <= 8:
        print("kamu masih anak anak")
        print("protein yang harus kamu konsumsi perhari\n adalah 19 gram") 
    elif 9 <= umur <= 13:
        print("kamu masih anak anak")
        print("protein yang harus kamu konsumsi perhari\n adalah 34 gram") 
    elif 14 <= umur <= 18:
        print("kamu sudah remaja")
        print("protein yang harus kamu konsumsi perhari\n adalah 46 gram") 
    elif 19 <= umur <= 50:
        print("kamu sudah dewasa")
        print("protein yang harus kamu konsumsi perhari\n adalah 46 gram") 
    elif umur < 51:
        print("kamu sudah manula")
        print("protein yang harus kamu konsumsi perhari\n adalah 46 gram")

print("terima kasih")