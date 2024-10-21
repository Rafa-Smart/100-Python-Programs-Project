# ini merupakan sebuah program menghitung hasil ujian siswa
# di buat pada 19/10/2024
# di buat oleh Rafa Khadafi
import os
os.system("cls")
print(30 * "\033[94m=")  
print("\033[94mPROGRAM MENGHITUNG HASIL UJIAN SISWA\033[0m") 
print(30 * "\033[94m=")

nilai_siswa = []
mata_ujian = [
    "b.indonesia",
    "b.sunda",
    "b.inggris",
    "ipas",
    "pancasila",
    "sejarah",
    "pai",
    "seni budaya"
]

# Loop untuk input nilai
for mata in mata_ujian:
    nilai_siswa.append(float(input(f"Masukkan nilai_siswa {mata} = ")))

# Menghitung total, nilai terbesar, dan terkecil
total = 0
nilai_terbesar = nilai_siswa[0]
nilai_terkecil = nilai_siswa[0]

for i in nilai_siswa:
    total += i
    if i > nilai_terbesar:
        nilai_terbesar = i
    if i < nilai_terkecil:
        nilai_terkecil = i

# Menampilkan hasil
print(f"Total nilai anda = {total}")
print(f"Rata-rata nilai anda = {total / len(mata_ujian)}")  # Menggunakan jumlah mata ujian untuk rata-rata
print(f"Nilai terbesar anda = {nilai_terbesar}")
print(f"Nilai terkecil anda = {nilai_terkecil}")
