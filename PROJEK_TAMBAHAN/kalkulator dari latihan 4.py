# grid() adalah menempatkan widget dalam 2 tabel dimensi.
# widget master dibagi menjadi beberapa baris dan kolom ,
# dan setiap "sel" di tabel yang dihasilkan dapat menampung widget

# grid() adalah yang paling fleksibel dari manejer geometri di tkinter

# option = stiky, column, row, columnspan, rowspan, padx, pady, ipadx, ipady, anchor
from tkinter import *
window = Tk()

window.resizable(False,False)
window.title("KALKULATOR SEDERHANA")

lebar = 500
tinggi = 400
layar_lebar = window.winfo_screenwidth()
layar_tinggi = window.winfo_screenheight()
new_x = (int(layar_lebar//2) - (lebar//2))
new_y = (int(layar_tinggi//2) - (tinggi//2))

# mengatur tempat window
# x adalah jarak dari kiri ke kanan
# y adalah jarak dari atas ke bawah
window.geometry(f"{lebar}x{tinggi}+{new_x}+{new_y}")


# option = column, row, columnspan, rowspan, padx, pady, ipadx, ipady, anchor
# stiky = atas : n, bawah : s, kiri : w, kanan : e

# columnspan digunakan untuk mengatur berapa kolom yang bisa digunakan oleh objek

# stiky = untuk sampe batasnya jadi misal e maka nanti langsung penuh sampe batasnya

# membuat konfigurasi column dulu
# indeks di konfigurasi column itu adalah indeks dari column di grid
window.columnconfigure(index=0,weight=1)
window.columnconfigure(index=1,weight=1)
window.columnconfigure(index=2,weight=1)
window.columnconfigure(index=3,weight=1)



# membuat konfigurasi row dulu
# indeks di konfigurasi row itu adalah indeks dari row di grid
window.rowconfigure(index=0,weight=1)
window.rowconfigure(index=1,weight=1)
window.rowconfigure(index=2,weight=1)
window.rowconfigure(index=3,weight=1)


hasil_jawaban = Button(text="jawaban")
button_1 = Button(text="1")
button_2 = Button(text="2")
button_3 = Button(text="3")
button_4 = Button(text="4")
button_5 = Button(text="5")
button_6 = Button(text="6")
button_7 = Button(text="7")
button_8 = Button(text="8")
button_9 = Button(text="9")
button_tambah = Button(text="+")
button_kurang = Button(text="-")
button_hasil = Button(text="hasil")


# column = dari kiri ke kanan
# row = dari atas ke bawah

# bisa kamu atur sendiri
hasil_jawaban.grid(column=0,row=0,sticky="we",padx=8,columnspan=4)
button_1.grid(column=0,row=1,sticky="wesn",padx=5,pady=5)
button_2.grid(column=1,row=1,sticky="wesn",padx=5,pady=5)
button_3.grid(column=2,row=1,sticky="wesn",padx=5,pady=5)
button_4.grid(column=0,row=2,sticky="wesn",padx=5,pady=5)
button_5.grid(column=1,row=2,sticky="wesn",padx=5,pady=5)
button_6.grid(column=2,row=2,sticky="wesn",padx=5,pady=5)
button_7.grid(column=0,row=3,sticky="wesn",padx=5,pady=5)
button_8.grid(column=1,row=3,sticky="wesn",padx=5,pady=5)
button_9.grid(column=2,row=3,sticky="wesn",padx=5,pady=5)
button_tambah.grid(column=3,row=1,sticky="wesn",padx=5,pady=5)
button_kurang.grid(column=3,row=2,sticky="wesn",padx=5,pady=5)
button_hasil.grid(column=3,row=3,sticky="wesn",padx=5,pady=5)



window.mainloop()