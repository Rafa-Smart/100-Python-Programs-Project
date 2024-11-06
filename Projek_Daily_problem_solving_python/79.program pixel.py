#ini adalah program menghitung pixel
# dibuat pada 06/11/2024
# dibuat oleh rafa khadafi

import os
os.system("cls")
print(35*"\033[34m=")
print("PROGRAM PIXEL".center(35))
print(35*"\033[34m=")
p = float(input("masukan nilai pixel = "))
def n_pixel(p):
    if p > 255:
        return 255
    elif p < 0:
        return 0 
    else:
        return p 
print(f"nilai {p} = {n_pixel(p)} pixel")