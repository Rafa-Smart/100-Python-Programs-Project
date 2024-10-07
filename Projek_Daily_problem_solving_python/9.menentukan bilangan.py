# ini merupakan sebuah program menentukan nilai bilangan
# di buat pada 07/10/2024
# di buat oleh Rafa Khadafi
print(30*"\033[92m=")
print("PROGRAM CARI BILANGAN YANG TERKECIL DAN YANG TERBESAR")
print(30*"\033[92m=")

x = int(input("masukan bilangan bulat 1 = "))
y = int(input("masukan bilangan bulat 2 = "))
z = int(input("masukan bilangan bulat 3 = "))

if x > y and x > z:
    print(f"ini adalah bilangan terbesar {x}")
elif y > x and y > z:
    print(f"ini adalah bilangan terbesar {y}")
elif z > x and z > y:
    print(f"ini adalah bilangan terbesar {z}")
else:
    print()
if x < y and x < z:
    print(f"ini adalah bilangan terkecil {x}")
elif y < x and y < z:
    print(f"ini adalah bilangan terkecil {y}")
elif z < x and z < y:
    print(f"ini adalah bilangan terkecil {z}")