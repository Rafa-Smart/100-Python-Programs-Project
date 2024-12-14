# rumus biasa

sisi = int(input("masukan sisi = "))
luas = sisi * sisi
print(f"luas = {luas}")

# pake lambda
luas2 = lambda sisi : sisi * sisi
print(luas2(12))
print(luas2(76))
print(luas2(43))

# jadi bisa dipanggil berkali kali
# dan membuat program menjadi lebih efisien

input = int(input("masukan sisi = "))
luas  = lambda input : x * x