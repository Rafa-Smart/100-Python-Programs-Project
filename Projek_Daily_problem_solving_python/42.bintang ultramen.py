# ini merupakan sebuah program segitiga biasa
# di buat pada 24/10/2024
# di buat oleh Rafa Khadafi
user = int(input("masukan nilai bintang = "))
print("segitiga biasa")
for i in range(user):
    print("*"*i)
    i += 1
no = 1
for no in range(user):
    print("*"*user)
    user -= 1