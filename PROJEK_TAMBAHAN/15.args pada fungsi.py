# args

# jadi args itu adalah cara simple untuk menympan banyak inputan dari user
# tanpa harus membuat banyak parameternya cukup dengan *nama_parameternya saja


# memasukan banyak args kedalam fungsi
# cara biasa
# contoh 1
def fungsi(nama,tinggi,berat):
    print(f"{nama} tinggi = {tinggi} = {berat}")
fungsi("rafa",170,67)


# ini fungsi list biasa
# contoh 2
def fungsi_list(*args):
    # args = fungsi_list.copy()
    nama = args[0]
    tinggi = args[1]
    berat = args[2]
    print(f"{nama} tinggi = {tinggi} berat = {berat}")

# jadi kalo kita ingin menaruh list kedalam fungsi maka kita haru copy dulu
# agar tidak berubah ubah args listnya

# ini maksudnya adalah membuat list
fungsi_list("putri",167,54)


# nah ini adalah args
# args sebenarnya adalah argument
def fungsi(*args):
    # jadi ini adalah akan sama dengan yang list
    # tapi inputnya atau argumennya sama dengan contoh pertama
    nama = args[0]
    tinggi = args[1]
    berat = args[2]
    print(f"{nama} tinggi = {tinggi} berat = {berat}")

fungsi('khadafi',178,72)
# keebihan 1
# jadi ini akan lebih simple dari pada harus
#  pake ini (["rafa",159,45])
# kelebihan 2 
# misal
# study kasus
# def tambah(angka1,angka2,angka3,angka4,angka5):
    # nah jika begini akan cape karena banyak

# penyelesaian
def tambah(*data):
    # data ini typenya adalah tuple 
    # dan bisa di iterasi
    output = 0
    for angka in data:
        output += angka
        return output

hasil = tambah(1,2,3,4,5,6,7,8,9)
print(f"hasil 1 = {hasil}")


hasil = tambah(10,5,15)
print(f"hasil 2 = {hasil}")
# nah jadinya kita bisa menambah apapun angkanya dan berapapun agka nya
# tanpa harus membuat banyak variable atau parameter di fungsi
# tetapi cukup hanya memakai *nama_parameternya saja


