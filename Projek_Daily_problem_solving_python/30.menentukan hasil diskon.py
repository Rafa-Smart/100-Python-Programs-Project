# ini merupakan sebuah program menentukan hasil diskon belanja
# di buat pada 21/10/2024
# di buat oleh Rafa Khadafi
import os

while True:
    os.system("cls")
    print(30 * "\033[94m=")
    print("\033[94mPROGRAM MENENTUKAN HASIL DISKON\033[0m")
    print(30 * "\033[94m=")

    try:

        input_belanja = float(input("masukan total belanja anda = "))
        input_diskon = float(input("berapa diskon yang anda dapatkan = "))
        diskon = input_belanja * input_diskon / 100
        harga_akhir = input_belanja - diskon
        print()
        print(f"diskon yang anda dapat = {diskon:,}\n")
        print(f"harga akhir yang harus anda bayar = rp.{harga_akhir:,} ")
        isdone = str(input("apakah masih mau lagi ? (y/t) = "))
        if isdone == "t":
            break
    
    except:
        print("anda memasukan inputan yang salah")
        print("masukan lah angka bulat / float")
        break


print("TERIMA KASIH")