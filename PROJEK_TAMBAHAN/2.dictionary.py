# array adalah sebuah kumpulan data 
# list adalah contoh dari array , dimana
# kita mengakses data dengan menggunakan index 
 
list = ['rafa',"putri"]
print(f"mengakses data dari list menggunakan index = {list[1]}")

print(20*"=")
# dictionary (dict) adalah asosiative array
# maksudnya jadi kalo misal di list kita mengakses data menggunakan 
# index tapi kalo di asosiative array kita mengakses data menggunakan
# identifier identitasnya apa? yaitu key
print(20*"=")
# contoh
# data_dict = {
#     'key1':'value1',
#     'key2':'value2',
# }

data_dict = {
    "rk":"rafa",
    "md":"putri"
}
print(data_dict["rk"])
# bedanya dengan list adalah saat kita ingin mengakses data
# maka kita bisa menggunakan key nya saja

# kegunaan dictionary ini adalah ketika kita membutuhkan
# sebuah data yang punya struktur yang bisa kita buat
# strukturnya menggunakan dictionary ini

# bahkankita bisa mengambil nomor ataupun list didalam 
# dictionary ini misal

list = ['rafa',"putri"]
data_dict = {
    "rk":"rafa",
    "md":"putri",
    "list":list
}
print(data_dict)
print(data_dict["rk"])
