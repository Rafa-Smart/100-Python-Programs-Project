# ini merupakan sebuah program diskon belanja biasa
# di buat pada 07/10/2024
# di buat oleh Rafa Khadafi
print(30*"\033[92m=")
print("PROGRAM MENENTUKAN DISKON BELANJA")
print(30*"\033[92m=")

total_harga = float(input("masukan total harga = "))
if total_harga >= 100:
    total_harga * 5 / 100
    print("selamat anda mendapat diskon sebesar 5%")
elif total_harga < 100:
    print("maaf anda tidak mendapatkan diskon")
diskon = total_harga * 5 / 100
print(f"ini adalah diskon anda = {diskon}")
total_harga_diskon = total_harga - diskon
print(f"ini adalah harga yang harus anda bayar = {total_harga_diskon}") 