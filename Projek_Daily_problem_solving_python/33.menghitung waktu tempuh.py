# ini merupakan sebuah program waktu tempuh perjalanan
# di buat pada 22/10/2024
# di buat oleh Rafa Khadafi
import os
os.system("cls")

while True:
    print(30 * "\033[94m=")  
    print("\033[94mPROGRAM MENGHITUNG WAKTU TEMPUH\033[0m") 
    print(30 * "\033[94m=")
    print()
    try:
        jarak = int(input("masukan jarak perjalanan (m) = "))
        kecepatan = int(input("masukan kecepatan kendaraan (m/s) = "))
        waktu = jarak / kecepatan
        print(f"waktu yang anda perlukan untuk sampai ke tujuan = {waktu:.2f} menit")
        while True:
            isdone = input("Apakah masih mau lagi? (y/t) = ").strip().lower()
            if isdone == "y":
                 break  # Kembali ke awal loop
            elif isdone == "t":
                print("Terima kasih! Program selesai.")
                exit()  # Keluar dari program
            else:
                print("Input tidak valid. Silakan masukkan 'y' untuk ya atau 't' untuk tidak.")
    except ValueError:
        print("inputan anda tidak valid")
        print("silahkan masukan bilangan bulat")
        break
print("TERIMA KASIH")