# ini merupakan sebuah program segitiga biasa
# di buat pada 24/10/2024
# di buat oleh Rafa Khadafi
print(30*"\033[92m=")
print("PROGRAM BINTANG BIASA")
print(30*"\033[92m=")
input = int(input("masukan nilai bintang = "))
no = 1
print("biasa")
while no < input:
    print("*"*no)
    no += 1

print("="*20)

print("terbalik")
no_2 = 1
while no_2 < input:
    print("*"*input)
    input -= 1
