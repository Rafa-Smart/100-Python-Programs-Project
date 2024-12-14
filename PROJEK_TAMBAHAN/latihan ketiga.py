# pack() adalah layout manager termudah untuk dirapkan di tkinter
# pack() mengatur widget dalam kotak horizontal dan vertikal yang terbatas pada
# posisi iri, kanan, atas , bawah, offset, dan relatif satu sama lain daam bingkai

# option = side, fill, expand, padx, pady, ipadx, ipady, anchor

from tkinter import *
window = Tk()

# membuat window otomatis ditengah
screnwidth = window.winfo_screenwidth() # lebar
screnheight = window.winfo_screenheight() # tinggi
lebar = 500
tinggi = 400
new_x = (int(screnwidth//2) - (lebar//2))
new_y = (int(screnheight//2) - (tinggi//2))

# setting geometri
window.geometry("400x400+200+200")
# side = TOP (default), BOTTOM, LEFT, or RIGHT ,CENTER
# fill = NONE (default), X (fill horizontaly), y (fill vertically), BOTH
# expand = YES,NO
# padx = horizontal padding(external), pady = vertical padding(external)
# ipadx = internal padding, ipady = internal padding

button_1 = Button(text="BUtton1")
# coba saja ya rafa nanti satu satu dair penjelasan diatas
button_1.pack(side=TOP, fill=X, expand=YES, padx=40, pady=40  )
window.mainloop()

