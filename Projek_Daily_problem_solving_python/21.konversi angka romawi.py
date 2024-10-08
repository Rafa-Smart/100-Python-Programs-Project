# ini merupakan sebuah program konversi angka romawi
# di buat pada 08/10/2024
# di buat oleh Rafa Khadafi
print(30*"\033[92m=")
print("PROGRAM KONVERSI ANGKA KE ROMAWI 1 - 10")
print(30*"\033[92m=")


input = int(input("masukan angka integer = "))
if 1 <= input <= 9:
    print("inputan yang anda masukan benar")

angka_romawi = {
    1:"I",
    2:"II",
    3:"III",
    4:"IV",
    5:"V",
    6:"VI",
    7:"VII",
    8:"VIII",
    9:"IX",
    10:"X"
}
hasil_romawi = angka_romawi[input]
print(f"ini adalah angka romawinya {hasil_romawi}")
