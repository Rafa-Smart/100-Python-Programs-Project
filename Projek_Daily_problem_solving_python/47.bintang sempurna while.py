# ini merupakan sebuah program segitiga sempurna
# di buat pada 24/10/2024
# di buat oleh Rafa Khadafi
print(30*"\033[92m=")
print("PROGRAM BINTANG SEMPURNA")
print(30*"\033[92m=")
user = int(input("masukan nilai bintang = "))
bintang = 1
print("segitiga sempurna biasa")
spasi_user = user
while bintang < user:
        print(" "*spasi_user,"*"*bintang)
        spasi_user -= 1
        bintang += 2
print()
print(35*"=")
print()
print("segitiga sempurna terbalik")
bintang = 1
spasi_2 = user 
while bintang < user:
        print(" "*spasi_2,"*"*user)
        spasi_2 += 1
        user -= 2
        