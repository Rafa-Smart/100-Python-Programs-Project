import numpy as np
print(np)

# contoh 1
list_a = [1,2,3,4,5]
vector_a = np.array([1,2,3,4,5])

# lihat lah perbedaanya
print(f"list a = {list_a}")
print(list_a)
print(f"vector a = {vector_a}")
print(vector_a)

print(20*"=")

# coba kita kuadratkan
# print(list_a**2) -> akan error
# tapi kalo yang vector
print(vector_a**2) # berhasil
print(vector_a*5)

print(20*"=")
# contoh 2
matriks_b = np.array([(1,2,3),(3,4,5),(6,7,8)])
print(matriks_b)

print(20*"=")
matriks_kosong = np.zeros((2,2))
print(matriks_kosong)

print(20*"=")
matriks_hanya_1 = np.ones((2,2))
print(matriks_hanya_1)

print(20*"=")
jumlah = matriks_b + matriks_b ** 2
print(jumlah)