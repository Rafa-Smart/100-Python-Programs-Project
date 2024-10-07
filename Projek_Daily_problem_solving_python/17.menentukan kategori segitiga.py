# ini merupakan sebuah program menentukan kategori segitiga
# di buat pada 07/10/2024
# di buat oleh Rafa Khadafi
print(30*"\033[92m=")
print("PROGRAM MENENTUKAN KATEGORI SEGITIGA")
print(30*"\033[92m=")

print("dengan syarat berikut\n1. a+b>c\n2.a+c>b\n3.b+c>a\njika tidak sesuai maka ini bukan segitiga !!!")
print()
a = float(input("masukan sisi a = "))
b = float(input("masukan sisi b = "))
c = float(input("masukan sisi terpanjang c = "))

# c merupakan sisi terpanjang

if a**2 + b**2 == c**2:
    print("ini adalah segitiga siku siku")
elif a**2 + b**2 > c**2:
    print("ini adalah segitiga lancip")
elif a**2 + b**2 < c**2:
    print("ini adalah segitiga tumpul")