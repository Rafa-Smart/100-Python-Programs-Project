# ini merupakan sebuah program menentukan nilai siswa
# di buat pada 07/10/2024
# di buat oleh Rafa Khadafi
print(20*"=")
print("PROGRAM MENENTUKAN NILAI UJIAN")
print(20*"=")
nilai = float(input("masukan nilai anda = "))
if nilai >= 90 and nilai <= 100 :
    # kalo pengen 2 situasi dalam 1 if yaitu pake
    # and
    print("nilai anda = A")
elif nilai >= 80 and nilai <= 90:
    print("nilai anda = B")
elif nilai >= 70 and nilai <= 80:
    print("nilai anda = C")
elif nilai <= 60:
    print("nilai anda = E")

print("belajar lah lebih giat lagi !")