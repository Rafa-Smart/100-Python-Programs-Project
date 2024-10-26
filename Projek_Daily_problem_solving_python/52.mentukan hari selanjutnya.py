# ini adalah program menentukan hari selanjutnya
# dibuat pada 26/10/2024
# dibuat oleh rafa khadafi
import os
os.system("cls")
print(30*"\033[92m=")
print("PROGRAM MENENTUKAN HARI SELANJUTNYA")
print(30*"\033[92m=")
print()

daftar_hari = ["senin","selasa","rabu","kamis","jumat","sabtu","minggu"]

def display_hari():
    for no,hari in enumerate(daftar_hari,start=1):
        print(f"{no}. hari = {hari}")
    
while True:
    try:
        print(f"SILAHKAN PILIH HARI")
        display_hari()
        hari_pertama = str(input("masukan hari pertama = "))
        jumlah = int(input("berapa hari setelahnya ? = "))
        hasil = jumlah % 7
        if hari_pertama not in daftar_hari:
            print("inputan anda tidak valid")
            continue
        # menghitung index hari pertama
        index_hari_pertama = daftar_hari.index(hari_pertama)
        # jadi ini itu maksudnya adalah kita mencari dulu index dari hari pertama itu
        # masuk di list daftar hari sebagai index ke berapa.
        index_hari_setelah = (index_hari_pertama + (jumlah % 7))%7
        # setelah itu kita cari index setalah hari pertama di tambah dengan jumlah 
        # misal hari pertama adalah selasa dan index selasa adalah 1, lalu
        # 1 ditambah dengan jumlah yang sudah dimodulus 7 contoh 100 = 100 % 7 = 3
        # kemudian 1 ditambah 3 lalu dimoduus 7 = 4 
        # nah berdasarkan list daftar hari index ke 4 adalah jumat  
        hari_setelah = daftar_hari[index_hari_setelah]
        print(f"{jumlah} hari setelah hari {hari_pertama} adalah = {hari_setelah}")
        
        while True:
            isdone = str(input("apakah masih mau lagi (y/t) ? = "))
            if isdone == "y":
                break
            elif isdone == "t":
                print("TERIMA KASIH")
                exit()
            else:
                print("silahkan masukan (y/t) saja")
                break
    except ValueError:
        print("inputan anda tidak valid")
        break