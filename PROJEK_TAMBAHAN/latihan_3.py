total_harga = int(input("masukan total harga barang (rp) (100),(50),(90)= "))
diskon = total_harga * 5 / 100
if total_harga >= 100:
    hasil = total_harga - diskon
    print(f"total harga yang harus anda bayar = {hasil}")
else:
    print("total barang anda tidak cukup untuk memenuhi diskon")
    print(f"total harga yang harus anda bayar {total_harga}")
