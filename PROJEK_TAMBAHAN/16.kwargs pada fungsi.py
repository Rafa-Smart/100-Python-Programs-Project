# kwargs pada fungsi
# kwargs = keyword args

# 1.fungsi biasa
def fungsi(nama,tinggi,berat):
    print(f"{nama} punya tinggi = {tinggi} dan berat = {berat}")
fungsi("rafa",185,75)

# 2.fungsi dengan args
def fungsi(*args):
    print(f"{args[0]} punya tinggi = {args[1]} dan berat = {args[2]}")
fungsi("ucup",167,65)

# 3.fungsi dengan kwargs
def fungsi(**kwargs):
    print(kwargs)
fungsi(nama="ucup",tinggi=167,berat=65)
# maka ini akan menjadi dictionary yang mempunyai sebuah key dan valuenya

# kita juga bisa mengambil value dari keynya saja

print("liat yg bawah")
def fungsi(**kwargs):
    print(kwargs["nama"])
fungsi(nama="ucup",tinggi=167,berat=65)


# 4.nah dengan kwargs kita bisa membuat ini
def fungsi(**kwargs):
    nama = kwargs["nama"]
    tinggi = kwargs["tinggi"]
    berat = kwargs["berat"]
    print(f"{nama} punya tinggi = {tinggi} dan berat = {berat}")
fungsi(nama="ucup",tinggi=167,berat=65)


# # study kasus
# def math(*args,**kwargs):
#     if kwargs["option"] == "tambah":
#         print(args)
#     elif kwargs["option"] == "kali":
#         print("operasi perkalian")
#     return 0
# hasil = math(1,2,3,4,5,6,7,option="tambah")
# hasil = math(1,2,3,4,5,6,7,option="kali")

# # study kasus
# def math(*args,**kwargs):
#     output = 0
#     if kwargs["option"] == "tambah":
#         for angka in args:
#             output += angka
#     elif kwargs["option"] == "kali":
#         for angka in args:
#             output *= angka
            # yang ini hasilnya akan 0 karena dia mengkalikan ke outpunya yang nilai dari vaariable
            # output adalah 0 maka apapun yang di kali 0 maka hasilnya akan 0
#     else:
#         print("tidak ada operasi")
#     return output
# hasil = math(1,2,3,4,5,6,7,option="tambah")
# print(f"ini hasil penjumlahan {hasil}")
# hasil = math(1,2,3,4,5,6,7,option="kali")
# print(f"ini adalah hasil perkalian {hasil}")

# study kasus
def math(*args,**kwargs):
    output = 0
    if kwargs["option"] == "tambah":
        for angka in args:
            output += angka
    elif kwargs["option"] == "kali":
        output = 1
        for angka in args:
            output *= angka
    else:
        print("tidak ada operasi")
    return output
hasil = math(1,2,3,4,5,6,7,option="tambah")
print(f"ini hasil penjumlahan {hasil}")
hasil = math(1,2,3,4,5,6,7,option="kali")
print(f"ini adalah hasil perkalian {hasil}")

# fungsi kwargs
# jadi fungsi dari kwargs adalah kita mengambil data dari dictionary dari user
# yaitu keynya adalah option dan valuenya adalah "kali" 
# cara penulisannya adalah option="kali"

# fungsi args
# jadi fungi args adalah kita membuat seperti tuple yaitu data list yang bisa diambil saja\