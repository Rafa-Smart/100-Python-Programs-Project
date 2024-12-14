print("soal 10")

inputan_user = str(input("masukan kalimat = "))
if "apakah" not in inputan_user:
    print(f"apakah {inputan_user} ?")
elif "?" not in inputan_user:
    print(f"{inputan_user} ?")
else:
    print(inputan_user)