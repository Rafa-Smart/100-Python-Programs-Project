import os

# Bersihkan layar terminal
os.system("cls" if os.name == "nt" else "clear")

# Inisialisasi list untuk menyimpan nilai
nilai = []
inputan = int(input("Masukkan jumlah data yang ingin di input = "))

# Input nilai
for i in range(inputan):
    nilai.append(float(input(f"Masukkan nilai ke - {i + 1} = ")))

# Perhitungan data di dalam list
total = 0
max_value = nilai[0]
min_value = nilai[0]

for i in nilai:
    total += i
    if i > max_value:
        max_value = i
    if i < min_value:
        min_value = i

# Menampilkan hasil
print(f"Total nilai = {total}")
print(f"Nilai rata-rata = {total / inputan}")
print(f"Nilai terbesar = {max_value}")
print(f"Nilai terkecil = {min_value}")
