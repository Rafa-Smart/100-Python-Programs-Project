# ini adalah program menentukan jam tidur ideal
# dibuat pada 26/10/2024
# dibuat oleh rafa khadafi
import os
os.system("cls")
print(30*"\033[92m=")
print("PROGRAM MENENTUKAN JAM TIDUR IDEAL")
print(30*"\033[92m=")
print()

while True:
    try:
        jam_tidur = int(input("masukan jam tidur anda = "))
        if 1 <= jam_tidur and 3 >= jam_tidur:
            print("jaga pola tidurnya yaa sayangg")
            print("jam tidur mu berdampak buruk : \n1.kelelahan extrem.\n2.gangguan kognitif.\n3.resiko kesehatan mental.\n4.penyakit fisik.\n5.potensi kecelakaan.")
        elif jam_tidur == 4:
            print("jaga pola tidurnya yaa sayangg")
            print("jam tidur mu berdampak buruk : \n1.kelelahan.\n2.penurunan kinerja.\n3.mood buruk.\n4.kesulitan beradaptasi.\n5.gangguan fisiologis")
        elif jam_tidur == 5 or jam_tidur == 6:
            print("jaga pola tidurnya yaa sayangg")
            print("jam tidur mu berdampak buruk : \n1.kelelahan ringan.\n2.resiko penyakit jantung.\n3.konsentrasi menurun.\n4.peforma menurun.\n5.stress meningkat.")
        elif jam_tidur == 7 or jam_tidur == 8:
            print("pola tidur kamu sudah baguss sayangg")
            print("jam tidur mu berdampak baik : \n1.pemulihan yang baik.\n2.kesehatan mental stabil.\n3.peningkatan kinerja kognitif.\n4.kesehatan jantung baik.\n5.regulasi hormon.")
        elif jam_tidur == 9 or jam_tidur == 10:
            print("pola tidur kamu lumayan baguss")
            print("jam tidur mu lumayan baik : \n\nmanfaat : \n1.pemulihan extra.\n2.peningkatan kreativitas.\n3.fokus yang tajam.\n\ndampak buruk : \n1.kepala sakit.\n2.kesulitan bangun.\n3.resiko penyakit tertentu.")
        else:
            print("kamu tidur nya berlebihan sayangg")
            break
        while True:
            isdone = str(input("apakah masih mau lagi (y/t) ? ="))
            if isdone == "y":
                    break
            elif isdone == "t":
                    print("TERIMA KASIH SAYANGG")
            else:
                    print("masukan y/t saja")
            break
    except ValueError:
        print("inputan anda tidak valid")
        print("silahkan masukan bilangan bulat")
        break