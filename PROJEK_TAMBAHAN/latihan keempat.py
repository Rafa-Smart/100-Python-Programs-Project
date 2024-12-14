# grid() adalah menempatkan widget dalam 2 tabel dimensi.
# widget master dibagi menjadi beberapa baris dan kolom ,
# dan setiap "sel" di tabel yang dihasilkan dapat menampung widget

# grid() adalah yang paling fleksibel dari manejer geometri di tkinter

# option = stiky, column, row, columnspan, rowspan, padx, pady, ipadx, ipady, anchor
from tkinter import *
window = Tk()

window.resizable(False,False)

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


# membuat konfigurasi column dulu
window.columnconfigure(index=0,weight=1)
window.columnconfigure(index=1,weight=1)
window.columnconfigure(index=2,weight=1)
window.columnconfigure(index=3,weight=1)
window.columnconfigure(index=4,weight=1)
window.columnconfigure(index=5,weight=1)

# membuat konfigurasi row dulu
window.rowconfigure(index=0,weight=1)
window.rowconfigure(index=1,weight=1)

button_1 = Button(text="tombol 1")
button_2 = Button(text="tombol 2")
button_3 = Button(text="tombol 3")
button_4 = Button(text="tombol 4")


# column = dari kiri ke kanan
# row = dari atas ke bawah

# bisa kamu atur sendiri
# indeks 0 dan 1 dan 2 sudah dipake oleh button 1
button_1.grid(column=0,row=0,sticky="we",columnspan=2)
# indeks 2 dan 3 dan 4 sudah dipake oleh button 2
button_2.grid(column=2,row=0,sticky="we",columnspan=2)
# indeks 4 dan 5 dan 6 sudah dipake oleh button 3
button_3.grid(column=4,row=0,sticky="we",columnspan=4)
# button mengisi semua columnspan yang ada yaitu 6 
button_4.grid(column=0,row=1,sticky="we",columnspan=6)



window.mainloop()