import datetime
import os
import string
import random
# jadi fungsi dari os ini adalah kita akan membersihkan 
# outputnya 


# template dict mahasiswa

mahasiswa_template = {
    "nama":"nama",
    "nim":"00000000",
    "sks_lulus":0,
    "lahir":datetime.datetime(1111,11,11)
}

# kita bikin dict kosong untuk menyimpan input 
# dari user
data_mahasiswa = {}

# mengambil input dari user

while True:
    os.system("cls")
    # nah dengan ini kita telah membersihkan outputnya


    print(f"{"SELAMAT DATANG SAYANG":^20}")
    print(f"{"DATA MAHASISWA":^20}")
    print(30*"=")
    print()
    # nah jika kita ingin membuat dictionary kosong 
    # berdasarkan mahasiswa_template untuk kita masukan
    # data dari input user ke dict mahasiswa_template
    # caranya adalah

    mahasiswa = dict.fromkeys(mahasiswa_template.keys())
    # jadi ini kita sudah membuat dict kosong yang berdasarkan dict mahasiswa_template
    # nah sekarang kita akan membuat input yang bisa 
    # langsung masuk ke dalam dict kosong berdasarkan dict template tadi

    mahasiswa["nama"] = str(input("masukan nama mahasiswa = "))
    mahasiswa["nim"] = int(input("masukan nim mahasiswa = "))
    mahasiswa["sks_lulus"] = int(input("masukan sks lulus mahasiswa = "))
    TAHUN_LAHIR = int(input("masukan tahun lahir (yyyy) = "))
    BULAN_LAHIR = int(input("masukan bulan lahir (1 - 12) = "))
    TANGGAL_LAHIR = int(input("masukan tanggal lahir (1 - 30) = "))
    # selanjutnya kita masukan input lahir kedalam dict
    # kosong berdasarkan dict template
    mahasiswa["lahir"] = datetime.datetime(TAHUN_LAHIR,BULAN_LAHIR,TANGGAL_LAHIR)


    KEY = "".join((random.choice(string.ascii_uppercase) for i in range(6)))

    # jika keynya tidak kita bedakan maka keynya akan sama
    # di setiap inputanya maka hal ini akan menyebabkan data yang
    # diberikan user akan menimpa data sebelumnya oleh sebab itu
    # kita akan merandom keynya agar disetiap inputan 
    # keynya berbeda dan tidak akan menimpa data sebelumnya


    # jadi kita mempunyai join ini fungsinya untuk menggabungkan 
    # inputan beberapa string dari user dan menggabungkannya tanpa spasi
    # jadi akan membuat KEY menggunakan random kita si choice ini akan memilih
    #  1 string data input dari user
    # yang menggunakan uppercase 
    # terus kita akan membuatnya maksimal 6 kali

    # nah cara pemakainnya seperti ini yaitu
    # 1.kita akan menggunakan KEY untuk memanggil pasangannya
    # dari input user
    # 2.dari input user (user itu kan memberikan data berupa beberapa string 
    # maka string ini akan kita gabungkan dengan cara ) ".join"(maksudnya adalah
    # kita menggabungkan inputan beberapa string dari user lalu mengabungkannya tanpa spasi)
    # 3.kita menggunakan random.choice untuk digabungkan dengan join dan stringnya 
    # menggunakan huruf besar contoh Jadi, jika huruf-huruf acak yang dipilih adalah 
    # "A", "B", "C", "D", "E", "F", maka KEY akan menjadi "ABCDEF".
    # 4.lalu total user dapat menginput adalah 6 kali sesuai kode

    # AGAR LEBIH PAHAM LIHAT OUTPUNYA


    # for nya

    data_mahasiswa.update({KEY:mahasiswa})
    # kegunaan update disini adalah agar saat input user memasukan data
    # maka akan masuk ke dalam dict kosongnya yaitu mahasiswa
    # kemudian dict yang ada di mahasiswa ini akan ditamahkan ke dalam 
    # variable data_mahasiswa yang jika data sudah ada maka hanya akan 
    # diperbarui namun jika data belum ada maka akan ditambah


    print(f"{"key":<10} {"nama":<10} {"nim":<10} {"sks lulus":<10} {"lahir":<10}")
    for mahasiswa in data_mahasiswa:
        KEY = mahasiswa
        NAMA = data_mahasiswa[KEY]["nama"]
        # maksud dari KEY ini adalah kita mengambil data dari mahasiswa untuk keynya
        NIM = data_mahasiswa[KEY]["nim"]
        SKS = data_mahasiswa[KEY]["sks_lulus"]
        LAHIR = data_mahasiswa[KEY]["lahir"].strftime("%x")
        # .strftime("%x") adalah metode untuk mengubah tanggal
        #  ke dalam format yang lebih mudah dibaca oleh manusia,
        #  seperti "09/01/24" untuk 1 September 2024. %x adalah 
        # kode format yang secara otomatis menyesuaikan tampilan tanggal
        #  berdasarkan pengaturan lokal.
        print(50*"-")
        print(f"{KEY:<6} {NAMA:<10} {NIM:<10} {SKS:<10} {LAHIR:^10}")
    
    print("\n")
    is_done = str(input("apakah sudah beres bro? (y/t) = "))
    if is_done == "y":
        break
print("TERIMA KASIH")