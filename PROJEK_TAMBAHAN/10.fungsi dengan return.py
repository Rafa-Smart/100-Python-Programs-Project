# return = kembalian
# fungsi dengan return

# misal 
# y = f(x) 
# y = adalah output dari fungsi
# f = adalah fungsinya
# (x) = adalah inputanya
# jadi nanti si (x) ini akan masuk ke output y
# input / (x) --> masuk ke badan fungsi lalu dieksekusi --> output

# contoh lagi

# def kuadrat (x):
#     hasil = x**2
#     return
# y = kuadrat(4)
# y = 16


# template fungsi dengan return

# def nama_fungsi(argumen)
    # badan fungsi
    # return output

# fungsi kuadrat

# ini yang biasa
# y = 3**2
# print(y)

# ini yang benar
def kuadrat(input_angka):
    # ini adalah fungsi kuadrat
    output_kuadrat = input_angka**2
    return output_kuadrat
y = kuadrat(3)
print(y)
# bisa juga gini
print(kuadrat(7))


# jadi cara kerjanya adalah y = kuadrat 3 maka 3 akan masuk ke def kuadrat input_angka
# lalu sekarang input angka adalah 3 kemudian memasukan input_kuadrat ke variable
# output_kuadrat, lalu output kuadratnya di return berati apapun yang kita kasih dari variable y ke variable
# input_angka maka akan kembali lagi ke variable y nya



# kita bikin yang lebih rumit lagi
z = 10 + kuadrat(7)
print(f"ini adalah = {z}")
# nah dengan seperti ini jadi kita tidak perlu membuat lagi program
# kuadratnya setiap kali ingin dipake

# fungsi tambah
def tambah(angka_1,angka_2):
    hasil = angka_1 + angka_2
    print(hasil)
    return
a = tambah(2,6)

# kita juga bisa tanpa menggunakan variable baru

def kali(angka_1,angka_2):
    # fungsi return dengan multi input
    return angka_1 * angka_2
a = kali(5,6)
print(a)


# fungsi return banyak
def operasi_matematika(angka_1,angka_2):
    kali = angka_1 * angka_2
    bagi = angka_1 / angka_2
    tambah = angka_1 + angka_2
    kurang = angka_1 - angka_2
    return kali,bagi,tambah,kurang
k,b,t,m = operasi_matematika(9,5)
print(f"hasil kali = {k}")
print(f"hasil bagi = {b}")
print(f"hasil tambah = {t}")
print(f"hasil kurang = {m}")