from tkinter import *

window = Tk()
lebar = 500
tinggi = 400
x = 400
y = 100


# membuat ukuran window fiks
window.resizable(False,False)
# atau bisa juga
# window.minsize(lebar,tinggi)
# window.maxsize(lebar,tinggi)

# mengganti title
window.title("belajar Tkinter")


# membuat window otomatis ditengah
screnwidth = window.winfo_screenwidth() # lebar
screnheight = window.winfo_screenheight() # tinggi

new_x = (int(screnwidth//2) - (lebar//2))
new_y = (int(screnheight//2) - (tinggi//2))

# mengatur tempat window
# x adalah jarak dari kiri ke kanan
# y adalah jara dari atas ke bawah
window.geometry(f"{lebar}x{tinggi}+{new_x}+{new_y}")

# membuat program terus berjalan sampai di hentikan
window.mainloop()