import os
os.system("cls")
buah_buahan = ["apel","jeruk","melon","pisang","anggur"]
print(buah_buahan[1])

buah_buahan[2] = "aden"
print(buah_buahan)

buah_buahan.append("lemon")

# for i in buah_buahan:
#     print((i),"mempunyai id = ",id(i)) 
#     '''Janganlah kau tinggal kan diriku '''
#     print ('rafaa syg putrii')

# no = 1
# for i in range(100):
#     print(i,"aku cinta putri")
#     no += 1

bulan = ["januari","februari","maret","april","mei","juni","july","agustus","september","oktober","november","desember"]
print(bulan[2],[9])
bulan[7] = "august"
print(bulan)
bulan[0] = "january"
bulan.append("muharram")
print(bulan[12])


no = 1
for i in bulan:
    print(no,i)
    no += 1