# ini adalah program membuat latihan dengan oop
# dibuat pada 26/10/2024
# dibuat oleh rafa khadafi
import os
os.system("cls")
print(30*"\033[92m=")
print("PROGRAM MEMBUAT LATIHAN OOP")
print(30*"\033[92m=")
print()
# oop = objek oriented program
# inherite = anakan / warisan dari class induknya
# encapsulation = membuat atribut yang hanya bisa diakses di class tersebut saja
# polymorph = membuat sub class yang merubah atribut dari induk classnya

# jadi oop itu punya class dan objek
# 1. class = template berisi data atau fungsi/method yang masih kosong / nanti
# bisa juga diubah setelah atau saat membuat objeknya
# 2. objek = adalah data / sesuatu yang sudah jadi berdasarkan dari temlpate si class


# 3. konstruktor biasanya didefinisikan menggunakan metode khusus yang disebut __init__.
#  Metode ini dipanggil secara otomatis saat kita membuat objek dari sebuah kelas. 
#  Berikut adalah contoh sederhana:


class Mobil:
    def __init__(self, merk, tahun):

        # jadi fungsi init ini adalah 
        # untuk memanggil fungsi parameternya
        # contoh kita panggi
        # mobil("toyota",2020)
        # nahh kita sudah memanggil class mobil menggunakan init 
        # secara otomatis
        self.merk = merk
        self.tahun = tahun

    def info(self):
        return f"Mobil {self.merk} tahun {self.tahun}"

# Membuat objek dari kelas Mobil
mobil1 = Mobil("Toyota", 2020)
mobil2 = Mobil("Honda", 2018)

# Menampilkan informasi mobil
print(mobil1.info())  # Output: Mobil Toyota tahun 2020
print(mobil2.info())  # Output: Mobil Honda tahun 2018
# Dalam contoh di atas:

# Kelas Mobil memiliki konstruktor __init__ yang menerima parameter merk dan tahun.
# Ketika kita membuat objek mobil1 dan mobil2, konstruktor akan 
# menyimpan nilai-nilai tersebut dalam atribut objek.
# Metode info digunakan untuk menampilkan informasi tentang mobil





# 4. Destruktor adalah metode khusus di Python yang dipanggil saat objek dihancurkan.
#  Metode ini didefinisikan dengan nama __del__. Meskipun Python memiliki pengelolaan memori
#  otomatis melalui pengumpulan sampah, destruktor dapat berguna untuk menjalankan kode pembersihan
#  sebelum objek dihapus, seperti menutup file atau melepaskan sumber daya lainnya.

# Berikut adalah contoh penggunaan destruktor dalam Python:

class Buku:
    def __init__(self, judul):
        self.judul = judul
        print(f"Buku '{self.judul}' telah dibuat.")

    def __del__(self):
        print(f"Buku '{self.judul}' telah dihapus.")

# Membuat objek dari kelas Buku
buku1 = Buku("Python Dasar")
buku2 = Buku("Belajar AI")

# Menghapus objek secara eksplisit
del buku1

# Menghapus objek secara otomatis saat tidak ada referensi lagi
# buku2 = None  # Ini akan memicu destruktor saat garbage collector berjalan
# Output dari contoh di atas mungkin terlihat seperti ini:

# arduino
# Copy code
# Buku 'Python Dasar' telah dibuat.
# Buku 'Belajar AI' telah dibuat.
# Buku 'Python Dasar' telah dihapus.
# Buku 'Belajar AI' telah dihapus.
# Di sini:

# Ketika objek Buku dibuat, konstruktor __init__ dipanggil dan mencetak pesan bahwa buku telah dibuat.
# Saat kita menggunakan del untuk menghapus objek atau saat objek tidak lagi memiliki referensi, destruktor __del__ dipanggil
#  dan mencetak pesan bahwa buku telah dihapus.
# Meskipun destruktor bisa bermanfaat, penting untuk menggunakannya dengan hati-hati karena perilaku pemanggilan bisa 




# pentingggggg
# jadi gini fungsi __main__ adalah
# untuk membuat blok kode yang kita pake if __name__ == "__main__":
# maka blok kode yang kita run maka yang terjadi adalah
# kit hanya bisa mengrun kode dari file awalnya
# jadi blok kode yang diselipkan if __name__ == "__main__":
# tidak akan bisa di import
# karena jika kita mengimport file yang ada if __name__ == "__main__":
# maka yang di import hanya kode yang selain blok kode yang ada if __name__ == "__main__":

# ====================================================
# __name__ pada file program utama
print(f"nilai __name__ pada oop.py = '{__name__}'")

# __name__ pada file program external


# contoh penggunaan

# deklarasi
# def fungsi_tambah(a:int,b:int)->int:
#     return a+b
# if __name__ == "__main__":
#     angka_1 = 5
#     angka_2 = 10
#     hasil = fungsi_tambah(angka_1,angka_2)
#     print(f"hasil tambah = {hasil}")