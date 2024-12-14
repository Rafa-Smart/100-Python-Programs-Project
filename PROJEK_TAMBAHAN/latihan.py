# input = int(input("masukan jumlah bintang = "))


# # segitiga biasa
# for i in range(1,input + 1,+1):
#     # jadi maksudnya adalah (1,input,+1) +1 = berati setiap perulangan kita tambahkan 1
#     print("*"*i)
#     # i += 1
# print()
# print("="*20)
# print()
# # segitiga terbalik
# for i in range(input,0,-1):
#     # jadi maksudnya adalah (input,0,-1) -1 = berati setiap perulangan kita kurangkan 1
#     print("*"*i)
# print()
# print("="*20)
# print()


# # Jumlah baris segitiga
# n = 5

# # Loop untuk setiap baris
# for i in range(n): # untuk mengulang baris
#     # Mencetak spasi untuk membuat segitiga sama kaki
#     for j in range(n - i - 1):
#         # baris pertama
#         # jadi gini inikan buat spasi, jadi
#         # di baris pertama, n itukan 5 terus si n ini dikurang sama i, 
#         # nah i nyakan baru iterasi/perulangan pertama jadi masih 0
#         # jadi 5 - 0 sama dnegan 5,
#         # terus hasilnya dikurang 1 setiap iterasi / perulangan
#         # terus di print pake spasi
#         # jadi spasi di baris pertama dari perulanga adalah 4 spasi
#         # begitu seterusnya

#         # ini kan pake end berati di perulangan * bakal disamping kanan si spasi

#         print(" ", end="")
    
#     # Mencetak bintang
#     for k in range(2 * i + 1):
#         # baris pertama
#         # jadi si i / perulangan untuk baris masih 0 maka, 2 dikali dengan 0 = 0
#         # terus di tambah 1 = 1, 
#         # jadi dibaris pertama disamping kanansi spasi itu
#         # di perulangan pertamanya ada 1 bintang
#         # begitu seterusnya
#         print("*", end="")
#     # Pindah ke baris berikutnya
#     print()
#     # print ini sangat berguna karena agar setiap baris yang sudah teriterasi
#     # akan di print ke baris baru, jadi tidak akan terus print di baris pertama
    
# print()
# print("="*20)
# print()
# n = int(input("masukan panjang segitiga = "))
# for i in range(n):
#     for spasi in range(n - i - 1):
#         print(" ", end="")
#     for bintang in range(2 * i + 1):
#         print("*", end="")
#     print()
# # print()
# print("="*20)
# print()

# segitiga terbalik
n = int(input("masukan panjang segitiga = "))
for i in range(n):
    for spasi in range(i):
        print(" ", end="")
    for bintang in range(2 * (n - i) - 1):
        print("*", end="")
    print()