import datetime
#kita ingin menambahkan tanggal lahir


# 1.multi keys
mahasiswa_1 = {
    "nama":"ucup surucup", # string
    "nim":"087657", #string
    "sks_lulus":238, #integer
    "beasiswa":False, # boolean
    "lahir":datetime.datetime(2009,5,12)
}
print(f"data mahasiswa 1 = {mahasiswa_1}")
print(20*"=")

# 2.nesting
mahasiswa_2 = {
    "nama":"otong surotong", # string
    "nim":"078653", #string
    "sks_lulus":300, #integer
    "beasiswa":True, # boolean
    "lahir":datetime.datetime(2002,10,18)
}

mahasiswa_3 = {
    "nama":"asep sikasep", # string
    "nim":"088475", #string
    "sks_lulus":150, #integer
    "beasiswa":False, # boolean
    "lahir":datetime.datetime(2000,4,29)
}

# membuat dictionary didalam dictionary
data_mahasiswa = {
    "mah001":mahasiswa_1,
    "mah002":mahasiswa_2,
    "mah003":mahasiswa_3
}
print(f"{"KEY":<6} {"nama":<17} {'nim':<10} {"sks":<3} {"beasiswa":<9} {"lahir":<10}")
print(50*"=")

# maksudnya adalah kita akan membuat outputnya 
# menjadi rata kiri
# nah maksud dari "key":<6 itu karena si keynya
# memakai kurang lebih 6 huruf saat ditulis di 
# atau juga karena kita ingin pake spasi sesuai dengan misal :<7 
# jadi akan ada spasi 7
# dan seterusnya

for mahasiswa in data_mahasiswa:
    KEY = mahasiswa
    NAMA = data_mahasiswa[KEY]["nama"]
    # maksud dari ini adalah
    # kita memasukan data mahasiswa yang mempunyai key
    # sebuah "nama" kedalam variable NAMA
    NIM = data_mahasiswa[KEY]["nim"]
    SKS = data_mahasiswa[KEY]["sks_lulus"]
    BEASISWA = data_mahasiswa[KEY]["beasiswa"]
    LAHIR = data_mahasiswa[KEY]["lahir"].strftime("%x")
    print(f"{KEY:<6} {NAMA:<17} {NIM:<10} {SKS:<3} {BEASISWA:^9} {LAHIR:<10}")

    # < untuk rata kiri
    # > untuk rata kanan
    # ^ intuk rata tengah