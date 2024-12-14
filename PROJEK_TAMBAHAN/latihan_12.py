total = int(input("masukan total harga = "))
if total >= 100:
    total_setelah = total * 5 / 100
    harga_sekarang = total - total_setelah
    print("diskon = ", total_setelah)
    print(f"total harga = {harga_sekarang}")
else:
    print(f"total harga = {total}")