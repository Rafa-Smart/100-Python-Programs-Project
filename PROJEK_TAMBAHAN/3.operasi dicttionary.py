# operator dictionary

data_dict = {
    "cup":"ucup surucup",
    "tong":"otong surotong",
    "dung":"dudung surudung"
}

# 1.panjang dictionary
# len itu biasanya adalah konstanta
LENDICT = len(data_dict)
print(f"ini panjang dictionary = {LENDICT}")


# 2.mengecek key ada atau tidak

KEY = "cup"
CHECKKEY = KEY in data_dict
print(f"apakah {KEY} ada dalam data_dict = {CHECKKEY}")

# 3.mengakses value (read) dengan get
print(data_dict["cup"])
# membedakan apakah ini list atau dictionary
print(data_dict.get("cup"))
# jadi ita bisa mengetahui apakah cup ini dictionary apa bukan
print(data_dict.get("kis")) # ini biasa akan none
print(20*"=")
print(data_dict.get("kis","key tidak ditemukan"))

# 4.mengubah data hanya dari keynya saja
print(f"ini data sebelum diubah {data_dict}")
data_dict["cup"] = "ucup siganteng"
print(f"ini data sesudah diubah {data_dict}")

# 5.menambah data 
data_dict["sep"] = "asep sikasep"
print(f"ini data sesudah ditambah {data_dict}")

# bagaimana jika si sep ini ternyata sudah ada didalam
# dictionarynya maka pake
# 6.mengupdate data
data_dict.update({"cup":"ucup siganteng"})
# jadi kalo kita mengupdate data yang keynya sudah ada
# maka kita tidak akan memnambah data baru lagi namun
# hanya mengganti value dari keynya saja
print(f"ini data sesudah diupdate (yang sudah ada) {data_dict}")


data_dict.update({"faqih":"faqihza keren"})
# tetapi jika kita mengupdate data yang keynya tidak ada
# maka kita akan otomatis menambah data bari ke dalam
# dictionarynya
print(f"ini data sesudah diupdate (yang belum ada) {data_dict}")


# delete data didalam dictionary
del data_dict["faqih"]
print(f"ini data sesudah di delete {data_dict}")