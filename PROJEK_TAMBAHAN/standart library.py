import datetime
data_waktu = datetime.datetime.now()
# untuk menghitung waktu

# now ini adalah method atau fungsi dari class datetime

# coba kamu arahkan kursor ke datetime yang pertama dan kedua
# maka di datetime pertama adalah modulnya
# dan di datetime kedua adalah classnya

# cara liat referensi nya adalah coba kamu
# arahkan kursor ke datetimenya dan klick kanan lalu pilih
# go to reference

# kalo mau buat library sendiri bisa, jdi kamu tinggal copy aja

# klao kamu cari standart library cari aja di google

print(f"data now = {data_waktu}")
print(f"tahun = {data_waktu.year}")
print(f"bulan = {data_waktu.month}")
print(f"hari = {data_waktu.strftime("%A")}")


# =====================================================

from collections import Counter
# untuk menghitung data

# cara menghitung a secara biasa 

data = ['a','b','c','d','a']
# count = 0
# for i in data:
#     if  i == "a":
#         count += 1
# print(count)

# cara menghitung a secara modul
data_count = Counter(data)
print(f"data count = {data_count}")
# ini adalah dictionary
print(f"jumlah a = {data_count["a"]}")
print(f"jumlah a = {data_count["d"]}")

# ==========================================================

import io

# untuk membaca file

file = io.open("surat cinta.txt","r")
# maksud dari "r" ini adalah untuk membaca
# dan ada berbagai fitur lainnya, silahkan cari sendiri
print(file.read())