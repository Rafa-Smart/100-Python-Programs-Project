# contoh aplikasi

while True:
    angka = int(input("masukan angka pembagi = "))
    try:
        hasil = 10/angka
        print(f"hasil = {hasil}")
        isdone = str(input("apakah mau lagi ? (y/t) = "))
        if isdone == "t":
            break
    except:
        print("pembagi tidak bisa 0, masukan angka lain !!!")
print("TERIMA KASIH")