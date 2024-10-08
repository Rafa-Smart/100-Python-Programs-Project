# ini merupakan sebuah program menentukan berat badan ideal 2
# di buat pada 08/10/2024
# di buat oleh Rafa Khadafi
print(30*"\033[92m=")
print("PROGRAM MENENTUKAN BERAT IDEAL")
print(30*"\033[92m=")

tinggi = int(input("masukan tinggi badan anda = "))
berat = int(input("masukan berat badan anda = "))
persen = tinggi * 10 / 100
berat_ideal = tinggi - 100 - persen
if berat - 2 < berat_ideal and berat + 2 > berat_ideal:
    print("berat badan anda masih ideal")
else:
    print("berat badan anda tidak ideal")
print(f"ini adalah berat badan ideal untuk anda = {berat_ideal}")