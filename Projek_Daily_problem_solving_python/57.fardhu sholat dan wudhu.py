# ini adalah program menampilkan fardhu sholat dan wudhu
# dibuat pada 26/10/2024
# dibuat oleh rafa khadafi
import os
os.system("cls")
print(30*"\033[92m=")
print("PROGRAM FARDHU SHOLAT DAN WUDHU")
print(30*"\033[92m=")
print()

fardhu = ["sholat","wudhu"]
def pilihan_1():
    for i , jenis in enumerate(fardhu):
        print(f"{i+1}.{jenis}")
while True:
    try:
        pilihan_1()
        print()
        pilihan = str(input("silahkan pilih = "))
        if pilihan == "sholat":
            print("""fardhu sholat adalah :
                  1.niat.
                  2.berdiri bagi yang mampu.
                  3.takbiratul ikhram.
                  4.membaca al-fatihah.
                  5.rukuk dengan tuma'ninah.
                  6.i'tidal dengan tuma'ninah.
                  7.sujud dengan tuma'ninah.
                  8.duduk diantara 2 sujud dengan tuma'ninah.
                  9.duduk tahiyyat akhir.
                  10.membaca doa tahiyya akhir.
                  11.membaca sholawat kepada nabi muhammad saw.
                  12.salam.
                  13.tertib.""")
        elif pilihan == "wudhu":
            print('''fardhu wudhu adalah :
                  1.niat.
                  2.membasuh seluruh wajah.
                  3.membasuh kedua tangan sampai siku siku.
                  4.mengusap sebagian kepala.
                  5.membasuh kaki sampai mata kaki.
                  6.tertib.''')
        else:
            print("pilihan anda belum tersedia")
            break
        while True:
            isdone = str(input("apakah sudah beres ? (y/t) = "))
            if isdone == "y":
                break
            elif isdone == "t":
                print("TERIMA KASIH")
                exit()
            else:
                print("masukan y/t saja")
                break
    except ValueError:
        print("inputan anda tidak valid")
        print("silahkan masukan inputan bertipe string")