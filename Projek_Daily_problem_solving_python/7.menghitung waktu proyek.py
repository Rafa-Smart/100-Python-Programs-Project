# ini merupakan sebuah program menghitung waktu proyek
# di buat pada 07/10/2024
# di buat oleh Rafa Khadafi
print(30*"\033[92m=")
print("PROGRAM MENGHITUNG WAKTU PROYEK")
print(30*"\033[92m=")

hari_input = float(input("masukan waktu pengerjaan proyek = "))
TAHUN = 365  
BULAN = 30
HARI = 1 
# yang memakai huruf besar semua adalah konstanta 
# artinya nilai yang berada di konstanta tersebut
# tidak akan dirubah

tahun = int(hari_input / TAHUN)
hari_input = hari_input % TAHUN
bulan = int(hari_input / BULAN )
hari_input = hari_input % BULAN
hari = int(hari_input / HARI)
hari_input = hari_input % HARI

print(f"waktu pengerjaan proyek ini adalah\n tahun = {tahun}\nbulan = {bulan}\nhari = {hari} ")