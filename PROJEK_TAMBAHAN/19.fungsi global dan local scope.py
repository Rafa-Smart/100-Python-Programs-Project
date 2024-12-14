# global dan local scope

# 1.variable global
# ini merupakan contoh dari pengguanaan variable global
nama_global = "putri cantik" # variable global
'''akses variable global dalam fungsi'''
def fungsi1():
    print(f"fungsi menampilkan nama = {nama_global}")
# kita panggil fungsinya
fungsi1()

# jadi variable global adalah variable yang bisa kita akses
# menggunakan yang ada : nya

'''akses variable global dalam looping'''
for i in range(1,6):
    print(f"looping {i} - {nama_global}")

'''akses variable global dalam percabangan'''
if True:
    print(f"menampilkan {nama_global}")


# 2.variable local scope
# ini contoh dari variable local
# def fungsi2():
#     nama_local = "ucup" <- variable local scope
# fungsi2()
# print(nama_local)

# dan jika kita run maka akan error
# karena variable ini hanya hidup di dalam fungsi2 ini saja
# dan tidak bisa di akses di luar dari fungsi ini


# contoh 1 : penggunaan
def say_otong():
    print(f"hello {nama}")
nama = "rafa"
say_otong()
# meskipun variablenya nama ini ada setelah penulisan print(f"hello {nama}")
# maka tidak akan error karena penulisan variablenya sebelum
# pemanggilan fungsi

# contoh 2 : merubah variable global
angka = 0
def ubah(nilai_baru):
    angka = nilai_baru
    # asumsi kita saat kita masukan variable nilai_baru ke
    # variable angka maka akan merubah nilai dari variable angka ini
print(f"sebelum dirubah = {angka}")
ubah(10)
print(f"sesudah dirubah = {angka}")

# jadi ini hasilnya adalah angka ini sudah menjadi local variable
# karena berada di dalam suatu fungsi
# dan tidak akan bisa diakses di luar fungsi

# maka cara merubahnya adalah 
'''cara ini akan salah karana penulisan global angka ini hanya'''
'''untuk bilang bahwa variable ini sudah menjadi global'''
# angka = 0
# def ubah_nilai(nilai_baru):
#      global angka = nilai_baru
print(20*"=")
# caranya adalah
angka = 0
nama = "putri cantikkk"
def ubah(nilai_baru,nama_baru):
     global angka
     global nama
     angka = nilai_baru
     nama = nama_baru
print(f"sebelum ubah data = {angka,nama}")
ubah(10,"mau diubah bagaimana pun kamu tetap cantikkk")
print(f"sesudah ubah data = {angka,nama}")


print(20*"=")
# contoh 3:
angka = 0
for i in range(1,6):
    angka += i
    angka_dummy = 0
print(angka)
print(angka_dummy)

if True:
    angka = 10 
    angka_dummy = 10
print(angka)
print(angka_dummy)

# berati kita bisa mengakses variable global 
# dan kita bisa mengakses local variable dari luar
# jika penggunaan nya di if dan di for loop