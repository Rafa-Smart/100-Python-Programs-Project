input_air = str(input("masukan kondisi air = "))
if input_air == "mendidih":
    print("matikan air")
else:
    print("input yang anda masukan salah")

input_suhu = int(input("masukan suhu ruangan anda = "))
if input_suhu > 50:
    print("bunyikan alarm tanda bahaya")
else:
    print("input yang anda masukan salah")

input_kondisi_mobil = str(input("masukan kondisi mobil anda = "))
if input_kondisi_mobil == "rusak":
    print("silahkan anda naik angkot")
else:
    print("input yang anda masukan salah")

input_angka = int(input("masukan angka = "))
if input_angka % 2 == 0:
    print(f"{input_angka} ini adalah angka genap")
else:
    print(f"{input_angka} ini adalah angka ganjil")