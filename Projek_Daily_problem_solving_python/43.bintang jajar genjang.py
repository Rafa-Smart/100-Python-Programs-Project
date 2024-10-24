# ini merupakan sebuah program segitiga terbalik
# di buat pada 22/10/2024
# di buat oleh Rafa Khadafi
user = int(input("masukan nilai segtiga = "))
print("ini adalah segitiga biasa")
for i in range(1,user + 1):
    # maksudnya adalah kita mulai dari 1 dan
    # user akan ditambah 1 karena index nya dari 0 
    # jadi kalo misal user input 7 maka kalo tidak ditambah maka akan 6
    # tapi jika ditambah maka akan tetap 7
    print(i*"*")
print()
print("ini adalah segitiga biasa terbalk")

for i in range(1,user + 1):
    print((user - i + 1) * "*")
print()
print("ini adalah bintang sempurna")

for i in range(1,user + 1):
    print((user - i) * " " + (2 * i - 1) * "*")
for i in range(user, 0, -1):
    print((user - i) * " " + (2 * i - 1) * "*")


print()
print("ini adalah bintang ultramen")
for i in range(user):
    print("*"*i)
    i += 1
no = 1
for no in range(user):
    print("*"*user)
    user -= 1