# ini adalah program menghitung luas dan keliling persegi panjang
# dibuat pada 08/10/2024
# dibuat oleh Rafa Khadafi
print(30*"\033[92m=")
print("PROGRAM PERSEGI PANJANG LAMBDA")
print(30*"\033[92m=")
sisi = int(input("masukan nilai sisi = "))
lebar = int(input("masukan nilai lebar = "))
luas = lambda s,l : s * l
keliling = lambda s,l : 2 * (s + l)

print(f"hasil luasnya adalah = {luas(sisi,lebar)}")
print(f"hasil kelilingnya adalah = {keliling(sisi)}")


# kalo cuma satu perintah 