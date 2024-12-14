# anonymous function
# namanya currying --> haskell curry (pembuatnya)

# misal pake fungsi biasa
def pangkat(angka,n):
    hasil = angka ** n
    print(f"ini adalah hasilnya {hasil}")
    return hasil
data_hasil = pangkat(5,2)

# jadi si currying ini membuat si fungsi ini dia gk fix dan kita bisa
# mengasignment dia menjadi variable yang bersifat sebagai fungsi

# dengan curriying
def pangkat_asli(n:int) -> int:
    return lambda angka : angka ** n
pangkat2 = pangkat(2) # ini adalah argumen dari fungsinya yaitu si n
print(f"pangkat 2 = {pangkat2(5)}")
pangkat3 = pangkat(3) # ini adalah argumen dari si lambda yaitu si angka
print(f"pangkat 3 = {pangkat3(5)}")


# oh ohhhh paham paham
# jadi kenapa kita pake def sama lambda secara bersamaan
# karena kita ingin membuat fungsi yang banyak tanpa perlu membuat fungsi lagi
# tapi bisa menggunakan lambda saja 
# karena fungsi dari penulisan lambda ini adalah kita membuat variable
# kemudian kita kasih lambda maka otomatis variable yang kita masukan lambda ini
# akan menjadi sebuah fungsi yang otomatis sudah di return

print(f"pangkat bebas = {pangkat_asli(4)(5)}")


# jadi sebenarnya pangkat2 dan pangkat3 adalah fungsi namun
# fungsi ini berbasis dari fungsi pangkat_asli tapi kita bisa merubah
# parameter di dalam pangkat_asli


# penjelasan

# 1. def pangkat_asli(n):
# Ini adalah definisi sebuah fungsi bernama pangkat_asli yang menerima satu argumen, yaitu n. Fungsi ini akan digunakan untuk membuat pangkat berdasarkan nilai n.
# 2. return lambda angka : angka ** n
# Di dalam fungsi pangkat_asli, kita mengembalikan (return) sebuah fungsi anonim (dikenal sebagai lambda) yang menerima satu argumen yaitu angka. Fungsi ini akan mengembalikan hasil dari angka dipangkatkan dengan n (misalnya, jika n adalah 2, maka fungsi ini akan mengembalikan angka ** 2).
# 3. pangkat2 = pangkat_asli(2)
# Di sini, kita memanggil fungsi pangkat_asli dengan argumen 2, dan hasilnya kita simpan dalam variabel pangkat2. Dengan kata lain, pangkat2 sekarang adalah fungsi yang akan memangkatkan angka dengan 2.
# 4. print(f"pangkat 2 = {pangkat2(5)}")
# Di baris ini, kita mencetak hasil dari memanggil pangkat2 dengan argumen 5. Ini berarti kita menghitung 
# 5
# 2
# 5 
# 2
#   (5 dipangkatkan 2). Hasilnya adalah 25, jadi output yang akan dicetak adalah "pangkat 2 = 25".
# 5. pangkat3 = pangkat_asli(3)
# Sama seperti sebelumnya, kita memanggil pangkat_asli dengan argumen 3, dan hasilnya kita simpan dalam variabel pangkat3. Sekarang, pangkat3 adalah fungsi yang memangkatkan angka dengan 3.
# 6. print(f"pangkat 3 = {pangkat3(5)}")
# Di sini, kita mencetak hasil dari pangkat3 dengan argumen 5, yang berarti kita menghitung 
# 5
# 3
# 5 
# 3
#   (5 dipangkatkan 3). Hasilnya adalah 125, jadi output yang akan dicetak adalah "pangkat 3 = 125".
# 7. print(f"pangkat bebas = {pangkat_asli(4)(5)}")
# Di baris terakhir ini, kita memanggil fungsi pangkat_asli langsung dengan argumen 4 dan kemudian langsung memanggil hasilnya dengan argumen 5. Ini berarti kita menghitung 
# 5
# 4
# 5 
# 4
#   (5 dipangkatkan 4). Hasilnya adalah 625, jadi output yang akan dicetak adalah "pangkat bebas = 625".