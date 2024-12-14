import os
os.system("cls")
nilai_siswa = int(input("masukan nilai siswa = "))
if 1 < nilai_siswa < 100 :
    if 90 < nilai_siswa < 100:
        print("nilai anda a")
    elif 80 < nilai_siswa < 90:
        print("nilai anda b")
    elif 60 < nilai_siswa < 70:
        print("nilai anda c")
    elif 50 < nilai_siswa < 60:
        print("nilai anda d")
    else:
        print("nilai anda sangat kecil")
else:
    print("nilai anda melebihi batas")

























