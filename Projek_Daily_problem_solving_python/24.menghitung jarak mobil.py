# ini merupakan sebuah program menghitung jarak tempuh mobil
# di buat pada 08/10/2024
# di buat oleh Rafa Khadafi
print(35*"\033[34m=")
print("\033[31mPROGRAM MENGHITUNG JARAK MOBIL".center(40))
print(35*"\033[34m=")

kecepatan = float(input("masukan kecepatan mobil anda km/jam = "))
waktu = float(input("masukan waktu tempuh mobil = "))

jarak = kecepatan * waktu
print(f"jarak tempuh mobil adalah = {jarak}")