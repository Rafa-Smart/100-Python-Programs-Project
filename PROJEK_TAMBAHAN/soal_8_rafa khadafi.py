print("soal 8")


input_user = int(input("masukan angka = "))
if  10 < input_user < 1000:
    print("ini adalah angka ratusan")
elif 100 < input_user < 1000000:
    print("ini adalah angka ribuan")
elif input_user > 1000000:
    print("ini adalah angka jutaan")