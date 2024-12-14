# lambda function 
# jadi lambda itu adalah sebuah fungsi tetapi belum memiliki nama
# merupakan sesuatu yang bisa membuat program kita menjadi lebih simple
# misal

def f_kuadrat(angka):
    return angka**2
print(f"ini adalah hasil fungsi biasa = {f_kuadrat(3)}")

print(20*"=")

# kita coba dengan lambda
# output = lambda argumen/input: expression
kuadrat = lambda angka:angka**2
print(f"ini adalah hasil fungsi pake lambda = {kuadrat(5)}")
# jadi gini saat di panggil maka jadi kita panggil fungsi yang adala di lambda yaitu kuadrat
# lalu inputnya/3 masuk ke angka: , lalu expression nya atau reaksinya 
# adalah yang angka**2
# dan yang ini otomatie mereturn


# contoh lain 

pangkat = lambda angka,pangkat: angka**pangkat
print(f"ini adalah hasil fungsi pake lambda yang 2 argumennya ={pangkat(5,3)}")
# nah jika seperti ini maka si variable pangkat ini 
# otomatis akan menjadi sebuah fungsi yang dapat dipanggil

# kegunaan ketika menggunaan lambda
# 1. kita ingin membuat sorting untk list
# nah kalo ita sorting pake list maka akan gampang saja
data_list = ["putri","cantik"]
data_list.sort()
print(f"ini adalah data list yang sudah di sort berdasarkan urutan abjadnya {data_list}")
# jadi ini sortnya berdasarkan posisi abjad abcd


# nah bagaimana caranya jika kita ingin mensorted datanya bersasarkan
# panjangnya 

# data_list.sort()
# nah sebenarnya di argumen si sort itu kita bisa menambahkan keynya
# atau menambahkan syaratnya untuk mengurutkanya

data_list.sort(key=len)
print(f"ini adalah data list yang sudah di sort berdasarkan panjangnya {data_list}")

# jika kita ingin memakai fungsi maka akan begini
def panjang_nama(nama):
    return len(nama)
data_list.sort(key=panjang_nama)
print(f"ini adalah data list yang sudah di sort berdasarkan panjangnya pake fungsi biasa {data_list}")


# jika kita ingin pake lambda 
data_list = ["rafa","putri","cantik"]
data_list.sort(key=lambda nama:len(nama))
print(f"ini adalah data list yang sudah di sort berdasarkan panjangnya pake lambda {data_list}")



# 2. kita bisa untuk memfilter
# contoh kalo pake fungsi
data_angka = [1,2,3,4,5,6,7,8,9,10]
def kurang_dari_lima(angka):
    return angka < 5
data_angka_baru = list(filter(kurang_dari_lima,data_angka))
print(data_angka_baru)

# contoh kalo pake lambda
data_angka_baru = list(filter(lambda x:x<5,data_angka))
# jadi ini maksudnya adalah kita memfilter sebuah list yang di x pertama adlah
# argumen atau inputnya dan :x<5 adalah expressionnya lalu dimasukan dengan ,data_angka

# 3.kita ingin memfilter yang genapnya saja

# contoh pake fungsi biasa
def angka_genap(angka):
    return angka % 2 == 0
data_genap_baru = list(filter(angka_genap,data_angka))
print(f"data genap pake fungsi biasa = {data_genap_baru}")

# contoh pake lambda
data_genap_baru = list(filter(lambda x:x % 2 == 0,data_angka))
print(f"data genap pake lambda = {data_genap_baru}")


# 4.membuat kelipatan 3 yang datanya diambil dari list

# pake fungsi biasa
def kelipatan(angka):
    return angka % 3 == 0 
data_kelipatan = list(filter(kelipatan,data_angka))
print(f"data kelipatan 3 pake fungsi = {data_kelipatan}")

# pake lambda 
data_kelipatan = list(filter(lambda x : x % 3 == 0,data_angka))
print(f"data kelipatan 3 pake fungsi = {data_genap_baru}")

data_lagi = [4,5,6,7,8,3,4,5]
def kelipatan(angka):
    return angka % 5 == 0
print(list(filter(kelipatan,data_lagi)))


print(list(filter(lambda x:x % 5 == 0,data_lagi)))




# lambda bisa pake 2 parameter caranya
sisi = int(input("masukan nilai sisi = "))
lebar = int(input("masukan nilai lebar = "))
luas = lambda s,l : s * l
keliling = lambda s : 4 * s

print(f"hasil luasnya adalah = {luas(sisi,lebar)}")
print(f"hasil kelilingnya adalah = {keliling(sisi)}")