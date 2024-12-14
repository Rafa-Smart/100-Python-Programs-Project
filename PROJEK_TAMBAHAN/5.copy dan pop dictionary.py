# copy dictionary

teman_teman = {
    "cup":"ucup surucup",
    "dung":"dudung surudung",
    "din":"udin surudin",
    "mal":"jamaludin",
    "tong":"otongsurotong"
}
# ini yang biasa
# friends = teman_teman
# print(f"friends = {friends}")
# print(f"teman teman = {teman_teman}")
# # coba kita ubah
# print(20*"=")
# teman_teman["cup"] = "kasep"
# print(f"friends = {friends}")
# print(f"teman teman = {teman_teman}")

# hasilnya sama seperti di list jadi 
# dua duanya akan berubah 

print(20*"=")
# beda jika kita mengcopy

friends = teman_teman.copy()
print(f"teman teman = {teman_teman}")
print(f"friends = {friends}")
# coba kita ubah
print(20*"=")
teman_teman["cup"] = "kasep"
print(f"teman teman = {teman_teman}")
print(f"friends = {friends}")

# kita ingin mengambil si data yang ada didalam
# dictionary sekalian data ini keluar dari 
# dictionary teman teman
print(20*"=")

# 1.pop dictionary (berdasarkan key)
data_ucup = friends.pop("cup")
print(f"data ucup = {data_ucup}")
print(f"friends sesudah mengeluarkan key cup = {friends}")
# jadi saat kita mengpop data dari dictionary
# maka kita telah mengambil data sekaligus 
# mengeluarkan key cup dari dictionary
# atau dengan kata lain (mentransfer)

print(20*"=")
# 2.popitem (yang terakhir saja)
# INGAT
# jika kita menggunakan item maka akan mengambil secara berpasangan 
# jika kita menggunakan popitem maka akan dikeluarkan yang terakhir
data_terakhir = friends.popitem()
print(f"data terakhir = {data_terakhir}")
print(f"friends sesudah mengeluarkan data terakhir = {friends}")
