import os
# jaid import CRUD adalah jika memiliki beberapa modul di dalam package CRUD,
# Anda bisa mengimpor modul-modul tersebut di dalam __init__.py,
# sehingga saat Anda mengimpor package, Anda dapat mengakses
# modul-modul tersebut langsung.
import CRUD as CRUD
os.system("cls")
def menu():
    print(f"1.baca data perpustakaan")
    print(f"2.buat data perpustakaan")
    print(f"3.menambah data perpustakaan")
    print(f"4.menghapus data perpustakaan")

# membuat agar program ini hanya bisa dijalankan
# hanya di file ini saja
if __name__ == "__main__":

    sistem_operasi = os.name
    CRUD.init_console()
    while True:

        match sistem_operasi:
            # agar bisa digunakan di berbagai sistem operasi
            case "posix": os.system("clear")
            case "nt": os.system("cls")

        print(f"SELAMAT DATANG".center(20))
        print(f"DATABASE PERPUSTAKAAN".center(20))
        print("="*22)

        jumlah_pilihan = [1,2,3,4]

        '''menampilkan menu'''
        menu()

        print()
        try:
            user_option = int(input("masukan pilihan anda = "))
            print("="*22)
            if user_option in jumlah_pilihan:
                match user_option:
                    #  disini case nya pake 1 karena di variable jumlah_pilihan
                    # pakenya int / 1,2,3,4 bukan "1"
                     case 1:
                          CRUD.read_console()
                     case 2:
                          print("membuat data")
                     case 3:
                          print("menambah data")
                     case 4:
                          print("menghapus data")
                print("="*22)
                isdone = input("apakah sudah selesai (y/t) ? = ")
                if isdone.lower() == "y":
                    break
            else:
                print("pilihan tidak valid,coba lagi")
                break
        except:
                print("input yang anda masukan salah, coba lagi")
                break
                