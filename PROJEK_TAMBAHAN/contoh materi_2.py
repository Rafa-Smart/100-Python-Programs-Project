# contoh aplikasi

while True:
    try:
        with open("data_7.txt","r") as file:
            print(file.read())
            break
    except:
        print("file data_7.txt tidak ditemukan, membuat file baru")
        with open("data_7.txt","w",encoding="utf-8") as file:
            file.write("file baru")
            break
print("TERIMA KASIH")

    

# sebelumnya saat kode ini di buat saya belum membuat file data_7.txt
# maka otomatis saat meruning yang pertama program akan langsung
# masuk except dan membuat file baru bernama data_7.txt
# dan melewati si try karena akan erorr disebabkan tidak adanya file

# lalu setelah itu saat kita meruning yang kedua kalinya
# maka tadi kan sudah dibuat file data_7.txtnya sama si except
# jadi saat kita runing yang kedua maka program akan langsung 
# masuk ke try , karena kita telah mempunyai filenya 