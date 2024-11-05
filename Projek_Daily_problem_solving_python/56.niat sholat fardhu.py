# ini adalah program niat sholat fardhu
# dibuat pada 26/10/2024
# dibuat oleh rafa khadafi
import os
os.system("cls")
print(30*"\033[92m=")
print("PROGRAM NIAT SHOLAT FARDHU")
print(30*"\033[92m=")
print()

nama_sholat = ["shubuh","dzuhur","ashar","magrib","isya"]

def sholat():
    for i,sholat in enumerate(nama_sholat):
        print(f"{i+1}. {sholat}")
while True:
    try:
        sholat()
        input_sholat = str(input("masukan nama sholat fardhu = "))
        if input_sholat == "shubuh":
            print("niat sholat shubuh :\n نويت أن أصلي فرض الصبح ركعتين، متوجهًا إلى القبلة، لله تعالى")
        elif input_sholat == "dzuhur":
            print("niat sholat dzuhur :\n نويت أن أصلي فرض الظهر أربع ركعات، متوجهًا إلى القبلة، لله تعالى")
        elif input_sholat == "ashar":
            print("niat sholat ashar : \n نويت أن أصلي فرض العصر أربع ركعات، متوجهًا إلى القبلة، لله تعالى")
        elif input_sholat == "magrib":
            print("niat sholat magrib : \n نويت أن أصلي فرض المغرب ثلاث ركعات، متوجهًا إلى القبلة، لله تعالى")
        elif input_sholat == "isya":
            print("niat sholat isya : \n نويت أن أصلي فرض العشاء أربع ركعات، متوجهًا إلى القبلة، لله تعالى")
        else:
            print("nama sholat anda belum tersedia")
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
        print("inputan anda tidak valid")
        print("silahkan masukan inputan bertipe string")