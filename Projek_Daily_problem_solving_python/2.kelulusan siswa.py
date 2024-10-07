# ini merupakan sebuah program kelulusan siswa
# di buat pada 07/10/2024
# di buat oleh Rafa Khadafi
print(20*"=")
print("PROGRAM KELULUSAN".center(20))
print(20*"=")
input_nilai = float(input("silahkan masukan nilai anda = "))
if input_nilai >= 94:
    print("anda lulus dengan predikat A")
elif 80 < input_nilai < 90:
    print("anda lulus dengan predikat B")
elif 75 < input_nilai < 80:
    print("anda lulus dengan predikat C")
else:
    print("maaf anda dinyatakan tidak lulus\nsilahkan coba di tahun depan :)")