# ini merupakan sebuah program kalkulator sederhana
# di buat pada 07/10/2024
# di buat oleh Rafa Khadafi
print(30*"\033[92m=")
print("PROGRAM KALKULATOR SEDERHANA")
print(30*"\033[92m=")

input_user = str(input("silahkan pilih operator (+,-,%,/,x,**)"))
angka_1 = float(input("masukan angka 1 = "))
angka_2 = float(input("masukan angka 2 = "))

if input_user == "+":
    hasil = angka_1 + angka_2
    print(f"hasilnya adalah = {hasil}")
elif input_user == "-":
    hasil = angka_1 - angka_2
    print(f"hasilnya adalah = {hasil}")
elif input_user == "%":
    hasil = angka_1 % angka_2
    print(f"hasilnya adalah = {hasil}")
elif input_user == "/":
    hasil = angka_1 / angka_2
    print(f"hasilnya adalah = {hasil}")
elif input_user == "*":
    hasil = angka_1 * angka_2
    print(f"hasilnya adalah = {hasil}")
elif input_user == "**":
    hasil = angka_1 ** angka_2
    print(f"hasilnya adalah = {hasil}")
print("terima kasih")