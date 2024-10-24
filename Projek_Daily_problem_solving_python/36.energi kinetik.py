# ini merupakan sebuah program energi kinetik
# di buat pada 24/10/2024
# di buat oleh Rafa Khadafi
print(35*"\033[34m=")
print("\033[31mmenghitung energi kinetik")
print(35*"\033[34m=")

m = float(input("masukan massa benda (kg) = "))
v = float(input("masukan kecepatan (m/s) = "))
energi_kinetik = 1/2 * m * (v ** 2)
print(f"jadi energi kinetiknya adalah = {energi_kinetik}")