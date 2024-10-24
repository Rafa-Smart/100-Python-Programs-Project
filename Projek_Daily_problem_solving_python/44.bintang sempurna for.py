# ini merupakan sebuah program segitiga sempurna
# di buat pada 24/10/2024
# di buat oleh Rafa Khadafi
user = int(input("masukan nilai bintang = "))
spasi = user
spasi1 = 1
user_2 = user

print("ini adalah seegitiga sempurna")
for i in range(user):
    print(f" "*spasi,"*"*i*2)
    i += 2
    spasi -= 1
    # user += 2
print()

for i in range(user):
    print(f" "*spasi1,"*"*user)
    user -= 2
    spasi += 1