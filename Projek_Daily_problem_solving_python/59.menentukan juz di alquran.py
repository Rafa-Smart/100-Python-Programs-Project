#ini adalah Program untuk menentukan juz berdasarkan halaman Al-Qur'an
# dibuat pada 26/10/2024
# dibuat oleh rafa khadafi
import os
os.system("cls")
print(30*"\033[92m=")
print("PROGRAM MENENTUKAN JUZ BERDASARKAN HALAMAN")
print(30*"\033[92m=")
print()
def tentukan_juz(halaman):
    if 1 <= halaman <= 20:
        return 1
    elif 21 <= halaman <= 40:
        return 2
    elif 41 <= halaman <= 60:
        return 3
    elif 61 <= halaman <= 80:
        return 4
    elif 81 <= halaman <= 100:
        return 5
    elif 101 <= halaman <= 120:
        return 6
    elif 121 <= halaman <= 140:
        return 7
    elif 141 <= halaman <= 160:
        return 8
    elif 161 <= halaman <= 180:
        return 9
    elif 181 <= halaman <= 200:
        return 10
    elif 201 <= halaman <= 220:
        return 11
    elif 221 <= halaman <= 240:
        return 12
    elif 241 <= halaman <= 260:
        return 13
    elif 261 <= halaman <= 280:
        return 14
    elif 281 <= halaman <= 300:
        return 15
    elif 301 <= halaman <= 320:
        return 16
    elif 321 <= halaman <= 340:
        return 17
    elif 341 <= halaman <= 360:
        return 18
    elif 361 <= halaman <= 380:
        return 19
    elif 381 <= halaman <= 400:
        return 20
    elif 401 <= halaman <= 420:
        return 21
    elif 421 <= halaman <= 440:
        return 22
    elif 441 <= halaman <= 460:
        return 23
    elif 461 <= halaman <= 480:
        return 24
    elif 481 <= halaman <= 500:
        return 25
    elif 501 <= halaman <= 520:
        return 26
    elif 521 <= halaman <= 540:
        return 27
    elif 541 <= halaman <= 560:
        return 28
    elif 561 <= halaman <= 580:
        return 29
    elif 581 <= halaman <= 604:
        return 30
    else:
        return "halaman tidak tersedia"

# Input dari pengguna
while True:
    try:
        halaman_input = int(input("Masukkan nomor halaman (1-604): "))
        juz = tentukan_juz(halaman_input)
        if juz is not "halaman tidak tersedia":
            print(f"Halaman {halaman_input} termasuk dalam Juz {juz}.")
        else:
            print("Nomor halaman tidak tersedia.")
            break
        while True:
            isdone = str(input("apakah sudah beres ? (y/t) = "))
            if isdone == "y":
                break
            elif isdone == "t":
                print("TERIMA KASIH")
                exit()
            else:
                print("masukan y/t saja")
                break
    except ValueError:
        print("Input harus berupa angka.")
