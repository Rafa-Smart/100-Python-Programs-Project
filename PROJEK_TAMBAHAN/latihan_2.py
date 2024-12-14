# data = {
#     "kelompok":"",
#     "asal_daerah":"",
#     "jumlah":0
# }

# kelompok = data["kelompok"] = str(input("masukan kelompok = "))
# asal = data["asal_daerah"] = str(input("masukan asal daerah = "))
# jumlah = data["jumlah"] = int(input("masukan jumlah = "))
# print(kelompok)
# for key,data in data.items():
#     print(f"{key} : {data}")


















data = {
    "kelompok":"",
    "asal":"",
    "no":""
}

data["kelompok"] = str(input("masukan kelompok = "))
data["asal"] = str(input("masukan asal = "))
data["no"] = str(input("masukan no = "))

for key,value in data.items():
    print(f"{key} : {value}")