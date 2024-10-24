# ini merupakan sebuah progam segitiga terbalik
# di buat pada 24/10/2024
# di buat oleh Rafa Khadafi
print(30*"\033[92m=")
print("PROGRAM BINTANG BISA")
print(30*"\033[92m=")
user = int(input("masukan nilai bintang = "))
print("segitiga biasa")
for i in range(user):
    print("*"*i)
    i += 1
    
print(35*"=")

print("segitiga biasa terbalik")
no = 1
for no in range(user):
    print("*"*user)
    user -= 1