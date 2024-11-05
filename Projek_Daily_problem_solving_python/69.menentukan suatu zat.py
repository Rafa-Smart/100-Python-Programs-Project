#ini adalah program menentukan suatu zat
# dibuat pada 05/11/2024
# dibuat oleh rafa khadafi
import os
os.system("cls")
print(30*"\033[92m=")
print("PROGRAM MENENTUKAN ZAT".center(30))
print(30*"\033[92m=")

inputan_suhu = int(input("masukan suhu = "))
if inputan_suhu <= 0:
    print("ini adalah zat padat")
elif 0 <= inputan_suhu < 100:
    print("ini adalah zat cair")
elif inputan_suhu > 100:
    print("ini adalah zat uap")