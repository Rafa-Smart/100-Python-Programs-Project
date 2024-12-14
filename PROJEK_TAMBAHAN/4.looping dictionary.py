# looping dictionary

teman_teman = {
    "rafa":"pecinta",
    "putri":"sicantik",
    "nazwa":"silucu",
    "aden":"sikocak",
    "ghina":"sisholehah"
}
# 1.looping for biasa
# yang keluar adalah si keynya saja
for i in teman_teman:
    print(i)

# operator untuk mengambil item / itereble
# 2.mengambil keynya saja
key = teman_teman.keys()
print(key)
for key in teman_teman.keys():
    print(key)
    # yang diatas hanya untuk mengetahui apakah
    # apakah ini key atau bukan
print(20*"=")
for key in teman_teman.keys():
    print(teman_teman.get(key))
    # fungsi get adalah untuk membaca apakah value yang mempunyai key  ini
    # dictionary atau bukan
    # karena jika kita ingin mengakses sebuah value yang tidak memiliki key yang kita masukan
    # didalam dictionary tanpa get maka ini akan error
    # namun jika ingin mengecek apakah value yang memiliki key yang kita masukan tidak ada didalam
    # dictionary maka hasilnya tidak akan error

print(20*"=")
# 3.jika kita ingin mengambil valuenya saja 
value = teman_teman.values()
print(value)
print(20*"=")

for value in teman_teman.values():
    print(value)

# 4.mengambil key dan value nya secara berpasangan
print(20*"=")

item = teman_teman.items()
print(item)

print(20*"=")

for item in teman_teman.items():
    print(item)

print(20*"=")

for key,value in teman_teman.items():
    print(f"key = {key}, value = {value}")

print(20*"=")

for key,value in enumerate(teman_teman):
    print(f"key = {key}, value = {value}")
    # ini tidak akan bisa karena enumerate hanya
    # bisa digunakan di list biasa saja