# ini merupakan sebuah program kalor jenis es
# di buat pada 24/10/2024
# di buat oleh Rafa Khadafi
print(35*"\033[34m=")
print("\033[31mKALOR JENIS ES")
print(35*"\033[34m=")

m = float(input("masukan massa es = "))
suhu_awal = float(input("masukan suhu awal = "))
suhu_akhir = float(input("masukan suhu akhir = "))
kalor_jenis_es = 2.1
# menghitung perubahan suhu
t = suhu_awal - suhu_akhir
# menghitung energi yang diperlukan
Q1 = m * kalor_jenis_es * t
print(f"julmah kalor yang diperlukan adalah {Q1}")
input = float(input("masu "))
