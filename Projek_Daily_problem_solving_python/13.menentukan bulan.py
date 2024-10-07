# ini merupakan sebuah program menentukan bulan
# di buat pada 07/10/2024
# di buat oleh Rafa Khadafi
print(30*"\033[92m=")
print("PROGRAM MENENTUKAN BULAN")
print(30*"\033[92m=")

menu_bulan = {
    "januari"  : 1,
    "februari" : 2,
    "maret"    : 3,
    "april"    : 4,
    "mei"      : 5,
    "juni"     : 6,
    "juli"     : 7,
    "agustus"  : 8,
    "september": 9,
    "oktober"  : 10,
    "november" : 11,
    "desember" : 12
}
for bulan,angka in menu_bulan.items():
    print(f"bulan = {bulan}, angka = {angka}")

input_user = int(input("masukan angka sesuai bulan = "))

print(f"angka yang anda pilih adalah bulan = {bulan}")
# if input_user == 1:
#     print(f"")

