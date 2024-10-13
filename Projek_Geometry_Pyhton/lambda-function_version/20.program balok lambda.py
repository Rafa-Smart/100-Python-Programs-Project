# ini adalah program menghitung rumus luas dan volume dengan lambda
# dari balok pada 13/10/2024
# dibuat oleh rafa khadafi

import os
os.system("cls")
print(30*"\033[92m=")
print("PROGRAM BALOK LAMBDA")
print(30*"\033[92m=")

def input_user():
    P = float(input("masukan nilai panjang balok = "))
    L = float(input("masukan nilai lebar balok = "))
    T = float(input("masukan nilai tinggi balok = "))
    return P,L,T

volume_balok = lambda P,L,T : P * L * T
luas_balok = lambda  P,L,T : 2 * (P * L + P * T + L * T)

P,L,T = input_user()

print(f"hasil perhitungan volume balok = {volume_balok(P,L,T):.2f}")
print(f"hasil perhitungan luas balok = {luas_balok(P,L,T):.2f}")