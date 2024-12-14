import os
from datetime import datetime as dt
os.system("cls")

tahun_lahir = int(input("masukan tahun lahir = "))
bulan_lahir = int(input("masukan bulan lahir (1-12)= "))
tanggal_lahir = int(input("masukan tanggal lahir (1-30)= "))
saat_lahir = dt(year=tahun_lahir,month=bulan_lahir,day=tanggal_lahir)
saat_ini = dt.now()

umur_tahun = saat_ini.year - saat_lahir.year
umur_bulan = saat_ini.month - saat_lahir.month
umur_hari = saat_ini.day - saat_lahir.day

print(f"""umur anda:\ntahun = {umur_tahun}\nbulan = {umur_bulan}\nhari = {umur_hari}""")