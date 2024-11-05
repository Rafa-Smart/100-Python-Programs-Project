# ini adalah program menentukan telat atau tidak
# dibuat pada 25/10/2024
# dibuat oleh rafa khadafi
import os
os.system("cls")
print(30*"\033[92m=")
print("PROGRAM MENENTUKAN TELAT SEKOLAH")
print(30*"\033[92m=")
print()

jam_masuk = 7.0
while True:
    try:
        waktu_berangkat = float(input("masukan waktu berangkat anda = "))
        jarak = float(input("masukan jarak ke sekolah (m) = "))
        kecepatan = float(input("masukan kecepatan anda (detik) = "))
        waktu_kendaraan = jarak / kecepatan
        waktu_nyampe = waktu_berangkat + waktu_kendaraan
        if waktu_nyampe < jam_masuk:
            sisa = jam_masuk - waktu_nyampe
            print("anda tidak telat")
            print(f"sisa waktu kamu {sisa:.2f} detik")
            print("buku kuning kamu aman")
        elif waktu_nyampe == jam_masuk:
            print("kamu hoki bangettt")
        elif waktu_nyampe > jam_masuk:
            waktu_terlambat = waktu_nyampe - jam_masuk
            print("yahh kamu terlambatt")
            print(f"kamu telat {waktu_terlambat:.2f} menit")
        else:
            print("inputan anda ngacooo")
            break
        while True:
            isdone = str(input("apakah masih mau lagi (y/t) ? = "))
            if isdone == "y":
                break
            elif isdone == "t":
                print("TERIMA KASIH")
                exit()
            else:
                print("silahkan masukan y/t saja")
                break

    except ValueError:
        print("inputan anda tidak valid")
        print("silahkan masukan bilangan bulat / float")

print("TERIMA KASIH")