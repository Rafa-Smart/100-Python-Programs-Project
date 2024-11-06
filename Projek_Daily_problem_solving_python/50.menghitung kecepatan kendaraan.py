# ini adalah program menghitung kecepatan berkendara 
# dibuat pada 24/10/2024
# dibuat oleh rafa khadafi
import os
os.system("cls")
print(30*"\033[92m=")
print("PROGRAM MENGHITUNG KECEPATAN KENDARAAN")
print(30*"\033[92m=")

while True:
    try:
        jarak = int(input("masukan jarak berkendara (m) = "))
        waktu = int(input("masukan waktu berkendara (s) = "))
        kecepatan = jarak / waktu
        print(f"kecepatan kendaraan anda adalah = {kecepatan:.2f} m/s")
        while True:
            isdone = str(input("apakah mau lagi (y/t) ? = "))
            if isdone == "y":
                break
            elif isdone == "t":
                print("TERIMA KASIH")
                exit()
            else:
                print("silahkan masukan y/t saja ")
                break 
    except ValueError:
        print("inputan anda tidak valid")
        print("silahka masukan y/t saja")
print("TERIMA KASIH")