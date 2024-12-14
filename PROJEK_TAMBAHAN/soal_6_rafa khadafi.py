# # print("soal 6")
# x = int(input("masukan angka = "))
# xx = x * 10 + x
# print(f"xx = {xx}")
# xxx  = xx * 10 + x
# print(f"xxx = {xxx}")
# xxxx = xxx * 10 + x
# print(f"xxxx = {xxxx}")
# hasil = xxxx - ( xx * x)
# print()
# print(hasil)

# # def hitung_angka():
#     # Input angka dari user
angka = input("Masukkan angka: ")

    # Buat string yang terdiri dari angka yang diulang beberapa kali
str_angka = angka * 4

    # Buat string yang terdiri dari angka yang diulang beberapa kali, kemudian dikali dengan angka
str_angka_kali = (angka * 2) + " * " + angka

    # Lakukan perhitungan
hasil = int(str_angka) - (int(angka * 2) * int(angka))

    # Cetak hasil
print(f"Hasil perhitungan: {str_angka} - ({str_angka_kali}) = {hasil}")

# Jalankan program
# hitung_angka()




y = int(input("masukan angka = "))
y_4 = str(y)*4
y_2 = str(y)*2
hasil = int(y_4) - int((y_2 * y))
print(f"{int(y_4)} - {int((y_2 * y))} = {hasil}")



















