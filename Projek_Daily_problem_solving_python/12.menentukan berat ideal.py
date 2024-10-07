# ini merupakan sebuah program menentukan berat ideal
# di buat pada 07/10/2024
# di buat oleh Rafa Khadafi
print(30*"\033[92m=")
print("PROGRAM MENGHITUNG BERAT BADAN")
print(30*"\033[92m=")

tinggi = int(input("masukan tinggi badan anda = "))

persen = tinggi * 10 / 100
berat_ideal = tinggi - 100 - persen

print(f"ini adalah berat badan ideal untuk anda = {berat_ideal}")