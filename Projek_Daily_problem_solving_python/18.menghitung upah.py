# ini merupakan sebuah program menghitung upah
# di buat pada 07/10/2024
# di buat oleh Rafa Khadafi
print(30*"\033[92m=")
print("PROGRAM MENGHITUNG UPAH KERJA BERDASARKAN JAM")
print(30*"\033[92m=")

golongan_kerja = {
    "asisten"   : 4000,
    "spesialis" : 5000,
    "manager"   : 6000,
    "ceo"       : 7000
}
for golongan,upah in golongan_kerja.items():
    print(f"golongan = {golongan}, upah = {upah}")

input_golongan = str(input("pilih golongan pekerjaan anda = "))
jam_kerja = int(input("masukan durasi bekerja anda = "))

upah_user = golongan_kerja[input_golongan] * jam_kerja
print(f"upah anda adalah = {upah_user}")


