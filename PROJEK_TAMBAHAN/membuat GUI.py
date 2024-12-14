# GUI -> graphical user interface
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# window adalah objeknya
# .configure adalah methodnya 

window = tk.Tk()
window.configure(bg="lavender")
window.geometry("330x200")
# variable komponen
NAMA_DEPAN = tk.StringVar()
NAMA_BELAKANG = tk.StringVar()

window.resizable(False,False)
# maksudnya adalah false pertama untuk sumbu x, false kedua untuk sumbu y
window.title("love letter to my princess")

# frame input
input_frame = ttk.Frame(window)
# maksudnya ttk.frame(window = untuk menaruh framenya di window kita)
# penempatan = grid,pack,place
input_frame.pack(padx=10,pady=10,fill="x",expand=True)
# jadi fill x itu untuk horizontal, dan y untuk vertikal

# komponen - komponen
# 1.label nama depan
nama_depan_label = ttk.Label(input_frame,text="""nama depan : """)
nama_depan_label.pack(padx=10,fill="x",expand=True) 

# 2.entry nama depan
nama_depan_entry = ttk.Entry(input_frame,textvariable=NAMA_DEPAN)
# NAMA_DEPAN akan masuk ke variable NAMA_DEPAN = tk.StringVar()
nama_depan_entry.pack(padx=10,fill="x",expand=True) 
# 3.label nama belakang
nama_belakang_label = ttk.Label(input_frame,text="""nama belakang : """)
nama_belakang_label.pack(padx=10,fill="x",expand=True) 

# 4.entry nama belakang
nama_belakang_entry = ttk.Entry(input_frame,textvariable=NAMA_BELAKANG)
# NAMA_BELAKANG akan masuk ke variable NAMA_BELAKAng = tk.StringVar()
nama_belakang_entry.pack(padx=10,fill="x",expand=True) 

# 5.tombol
# buat fungsi tombol click
def tombol_click():
    print(NAMA_DEPAN.get(),NAMA_BELAKANG.get())
    pesan = f"{NAMA_DEPAN.get()} {NAMA_BELAKANG.get()}, kamu cantikkk"
    showinfo(title="whattzup!",message=pesan)
    
tombol_sapa = ttk.Button(input_frame,text="kirim!",command=tombol_click)
tombol_sapa.pack(fill="x",expand=True,padx=10,pady=10)
window.mainloop()