from tkinter import *  # Mengimpor semua komponen dari modul tkinter
from tkinter import messagebox  # Mengimpor messagebox untuk menampilkan pesan kesalahan
import base64  # Mengimpor modul base64 untuk melakukan enkripsi dan dekripsi

def enkripsi():  # Mendefinisikan fungsi untuk enkripsi
    kata_sandi = kode.get()  # Mengambil nilai dari entry kata sandi
    if kata_sandi == "1234":  # Memeriksa apakah kata sandi yang dimasukkan benar
         layar_enkripsi = Toplevel(layar)  # Membuat window baru untuk enkripsi
         layar_enkripsi.title("Enkripsi")  # Menetapkan judul window
         layar_enkripsi.geometry("400x200")  # Menetapkan ukuran window
         layar_enkripsi.configure(bg="#ed3833")  # Mengatur warna latar belakang window

         pesan = teks_input.get(1.0, END)  # Mengambil teks dari area input
         pesan_terkode = pesan.encode("ascii")  # Mengubah teks menjadi bytes menggunakan ASCII
         bytes_enkripsi = base64.b64encode(pesan_terkode)  # Melakukan enkripsi dengan base64
         enkripsi = bytes_enkripsi.decode("ascii")  # Mengubah hasil enkripsi kembali menjadi string
         Label(layar_enkripsi, text="ENKRIPSI", font="arial", fg="white", bg="#ed3833").place(x=10, y=0)  # Menampilkan label "ENKRIPSI"
         teks_output = Text(layar_enkripsi, font="Rpbote 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)  # Membuat area teks untuk output
         teks_output.place(x=10, y=40, width=380, height=150)  # Menempatkan area teks di window
         teks_output.insert(END, enkripsi)  # Menampilkan hasil enkripsi di area teks
    elif kata_sandi == "":  # Jika kata sandi kosong
         messagebox.showerror("Enkripsi", "Masukkan kata sandi")  # Menampilkan pesan kesalahan
    elif kata_sandi != "1234":  # Jika kata sandi salah
         messagebox.showerror("Enkripsi", "Kata sandi tidak valid")  # Menampilkan pesan kesalahan

def dekripsi():  # Mendefinisikan fungsi untuk dekripsi
    kata_sandi = kode.get()  # Mengambil nilai dari entry kata sandi
    if kata_sandi == "1234":  # Memeriksa apakah kata sandi yang dimasukkan benar
         layar_dekripsi = Toplevel(layar)  # Membuat window baru untuk dekripsi
         layar_dekripsi.title("Dekripsi")  # Menetapkan judul window
         layar_dekripsi.geometry("400x200")  # Menetapkan ukuran window
         layar_dekripsi.configure(bg="#00bd56")  # Mengatur warna latar belakang window

         pesan = teks_input.get(1.0, END)  # Mengambil teks dari area input
         pesan_terkode = pesan.encode("ascii")  # Mengubah teks menjadi bytes menggunakan ASCII
         bytes_dekripsi = base64.b64decode(pesan_terkode)  # Melakukan dekripsi dengan base64
         dekripsi = bytes_dekripsi.decode("ascii")  # Mengubah hasil dekripsi kembali menjadi string
         Label(layar_dekripsi, text="DEKRIPSI", font="arial", fg="white", bg="#00bd56").place(x=10, y=0)  # Menampilkan label "DEKRIPSI"
         teks_output = Text(layar_dekripsi, font="Rpbote 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)  # Membuat area teks untuk output
         teks_output.place(x=10, y=40, width=380, height=150)  # Menempatkan area teks di window
         teks_output.insert(END, dekripsi)  # Menampilkan hasil dekripsi di area teks
    elif kata_sandi == "":  # Jika kata sandi kosong
         messagebox.showerror("Dekripsi", "Masukkan kata sandi")  # Menampilkan pesan kesalahan
    elif kata_sandi != "1234":  # Jika kata sandi salah
         messagebox.showerror("Dekripsi", "Kata sandi tidak valid")  # Menampilkan pesan kesalahan

def layar_utama():
    global layar
    global kode
    global teks_input
    layar = Tk()
    layar.geometry("375x398")

    def reset():
        kode.set("")
        teks_input.delete(1.0, END)

    layar.title("PROGRAM SAYA")
    Label(text="Masukkan teks untuk enkripsi dan dekripsi", fg="black", font=("calibri", 13)).place(x=10, y=10)
    teks_input = Text(font="robote 13", bg="white", relief=GROOVE, wrap=WORD, bd=0)
    teks_input.place(x=10, y=50, width=355, height=100)

    Label(text="Masukkan kunci untuk enkripsi dan dekripsi", fg="black", font=("calibri", 13)).place(x=15, y=170)
    kode = StringVar()
    Entry(textvariable=kode, width=19, bd=0, font=("arial", 25), show="*").place(x=15, y=200)

    Button(text="ENKRIPSI", height="2", width=23, bg="#ed3833", fg="black", bd=0, command=enkripsi).place(x=10, y=250)
    Button(text="DEKRIPSI", height="2", width=23, bg="#00bd56", fg="black", bd=0, command=dekripsi).place(x=200, y=250)
    Button(text="RESET PROGRAM", height="2", width=50, bg="#1089ff", fg="black", bd=0, command=reset).place(x=10, y=300)

    layar.mainloop()

layar_utama()