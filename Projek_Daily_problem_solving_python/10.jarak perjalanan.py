# ini merupakan sebuah program jarak perjalanan
# di buat pada 07/10/2024
# di buat oleh Rafa Khadafi
print(30*"\033[92m=")
print("PROGRAM MENGHITUNG JARAK PERJALANAN")
print(30*"\033[92m=")

input_cm = int(input("masukan jarak menggunakan cm = "))
KM = 100 * 10 * 100
M = 10 * 10
CM = 1


input_km = int(input_cm / KM)
input_cm = input_cm % KM
input_m = int(input_cm / M)
input_cm= input_cm % M
input_cm_1 = (input_cm / CM)
input_cm = input_cm % CM

print(f"jarak tempuh anda adalah\nkilo meter = {input_km:.2f}\nmeter = {input_m:.2f}\ncm = {input_cm_1:.2f}")