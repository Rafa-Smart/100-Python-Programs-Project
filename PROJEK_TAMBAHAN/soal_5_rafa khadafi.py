print("soal 5")
list_buah = []
input_jumlah = int(input("berapa jumlah buah (harus lebih dari 4) = "))
for i in range(1,input_jumlah +1):
    buah = str(input(f"masukan buah ke-{i} = "))
    list_buah.append(buah)
print(f"hasil 1 mencetak mencari buah berdasarkan indeks, ini indeks ke 1 berati buah ke 2= {list_buah[1]}")
print(f"hasil 1 mencetak mencari buah berdasarkan indeks, ini indeks ke 3 berati buah ke 4 = {list_buah[3]}")
print()
print(f"hasil 2 mencetak buah berdasarkan soal yaitu 2 dan 4 = {list_buah[2]}")
print(f"hasil 2 mencetak buah berdasarkan soal yaitu 2 dan 4 = {list_buah[4]}")


