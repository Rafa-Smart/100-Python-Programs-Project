# ini merupakan sebuah program konversi panjang benda
# di buat pada 07/10/2024
# di buat oleh Rafa Khadafi
print(30*"\033[92m=")
print("PROGRAM MENGHITUNG PANJANG BENDA")
print(30*"\033[92m=")



input_m = float(input("masukan panjang benda dengan satuan m = "))


INCHI = 25.4
KAKI = 30.48
YARD = 0.9144

inchi = input_m / INCHI
input_m = input_m % INCHI
kaki = input_m / KAKI
input_m = input_m % KAKI
yard = input_m / YARD
input_m = input_m % YARD

print(f"ini adalah konversi panjang benda\ninchi = {inchi:.2f}\nkaki = {kaki:.2f}\nyard = {yard:.2f}")