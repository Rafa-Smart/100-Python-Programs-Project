#ini adalah ujian
# dibuat pada 05/11/2024
# dibuat oleh rafa khadafi
import os
os.system("cls")
print(30*"\033[92m=")
print("PROGRAM MENGHITUNG POINT".center(30))
print(30*"\033[92m=")

print("siapakah tuhan mu ? ")
# print("""a.monyet
#          b.fagian
#          c.allah""")

list = {"a":"monyet","b":"fagian","c":"allah"}
for i,nilai in list.items():
    print(f"{i}.{nilai}")
jawaban = str(input("masukan jawaban anda = "))
if jawaban == "c":
    print("jawaban anda benar")
elif jawaban == 'b':
    print("jawaban anda salah")
else:
    print("jawaban anda salah")