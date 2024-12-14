# jadi gini, saat kita memberikan argumen kepada input / ()

# def nama_fungsi(argument):
# bagaimana jika nilai di argument ini tidak kita kasih atau masukan
# berati ada nilai defaultnya dari python

# def nama_fungsi(argumen = nilai defaultnya):

# contoh

# def say_hello(nama):
#     print(f"hallooo {nama}")
# say_hello("rafa")
# say_hello()
# tapi jika kita kosongkan nilai nya maka error

# jadi kita akan membuat default argumennya dengan cara
def say_hello(nama = "cantiik"):
    print(f"hallooo {nama}")
say_hello()

# 2.buat 2 variable di dalam argumen
# ini yang biasa
def sapa_dia(nama,pesan):
    print(f"hay {nama}, {pesan}")
sapa_dia("rafa","apa kabar")

# jadi satunya adalah default argumen, satunya argumen biasa
def sapa_dia(nama,pesan = "apa kabar"):
    print(f"hay {nama}, {pesan}")
sapa_dia("rafa")

# contoh 3
# ini biasa
def hitung_pangkat(angka,pangkat):
    hasil = angka**pangkat
    return hasil
print(hitung_pangkat(2,4))

# ini pake default
def hitung_pangkat(angka = 5,pangkat = 2):
    hasil = angka**pangkat
    return hasil
print(hitung_pangkat())

# bisa juga seperti ini 

def hitung_pangkat(angka,pangkat = 2):
    hasil = angka**pangkat
    return hasil
print(hitung_pangkat(2,4))
hasil = hitung_pangkat(pangkat=3,angka=5)
print(hasil)

# jadi ini berguna misalkan kita punya banyak sekali variable di dalam argumen
# lalu kita ingin mengakses argumen mana yang ingin kita pakai


# contoh 4
def fungsi(input1=1,input2=2,input3=3,input4=4):
    hasil = input1 + input2 +input3 +input4
    return hasil
print(f"ini adalah contoh {fungsi()}")
# nah bagaimana jika kita ingin mengganti nilai di argumen nya
# caranya adalah
print(fungsi())