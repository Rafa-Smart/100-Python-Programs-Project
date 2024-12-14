# fungsi dengan argumen (input)

# template
# def nama_fungsi(argumen/paremeter/input): # nama fungsi
    # badan fungsi
    # / tempat deklarasi
# nanti si argumen ini akan masuk kedalam badan tempat deklarasi fungsi


def hello_wolrd(nama):
    # fungsi hello wolrd menerima argumen dengan variable nama
    print(f"selamat datang dunia wahai {nama}")

# jadi saat kita panggil hello world maka maka rafa akan masuk ke variable nama
# yang ada didalam fungsi
# di argumen kita bisa apa saja misal list,bool,number,string dll
hello_wolrd("rafa")

# program tambah 
# number pake fungsi
def tambah(angka_1,angka_2):
    # fungsi tambah
    hasil = angka_1 + angka_2
    return print(f"{angka_1} + {angka_2} = {hasil}")

tambah(3,6)

# list pake fungsi
def say_hay(list_peserta):
    data_peserta = list_peserta.copy()
    for peserta in data_peserta:
        print(f"yang terhormat {peserta}")
anggota_boyband = ["ucup","otong","asep"]
# jadi gini, kita punya list anggota boyband diluar fungsi
# lalu kita masukin data list anggota boyband kedalam fungsi say_hay(list_peserta)
# kemudian saat data list kita masukan ke dalam fungsi say_hay
# maka otomatis variable nya berubah yang asalnya adalah anggota_boyband
# menjadi list_peserta 
# terus kenapa kita pake copy, karena kita tidak mau merubah
# data yang ada diluar fungsi
say_hay(anggota_boyband)