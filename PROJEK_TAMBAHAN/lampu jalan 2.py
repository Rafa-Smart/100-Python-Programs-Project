input_user= str(input("masukan lampu anda = ")).lower()
# ini pake lower agar sesuai dengan ifnya yang menggunakan 
# huruf kecil semua 
# agar tidak error

if input_user == "hijau":
    print("silahkan anda maju")
elif input_user == "kuning":
    print("siapkan diri anda")
elif input_user == "merah":
    print("anda dilarang maju")

# anda bisa pake while true agar kode bisa berjalan terus menerus
# ini tidak pake konstanta karena variable nya tidak seperti 
# password yang tidak bisa diubah ubah