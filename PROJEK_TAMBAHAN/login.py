# biasanya jika sudah mahir maka usernamenya akan 
# diambil dari database

input_user = str(input("masukan akun google anda = "))
input_pass = int(input("masukan password  anda = "))

USERNAME = "rafakhadafi1205@mail.com"
PASSWORD = 12345678

# if input_user == "USERNAME":
#     print(f"selamat datang {input_user}")
# else:
#     print("akun google yang anda masukan salah")

# if input_pass == PASSWORD:
#     print("silahkan masuk ")
# else:
#     print("kata sandi yang anda masukan salah")

# ini adalah contoh yang biasa

# ini yang pak yayat

if input_user != USERNAME:
    print("username tidak tersedia")
elif input_user == USERNAME and input_pass != PASSWORD:
    print("password salah")
else:
    print(f"selamat datang {input_user}")


print("nama dzay")





# jika and maka semua kondisi harus bernilai benar jika
# outputnya ingin True