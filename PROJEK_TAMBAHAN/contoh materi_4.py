# contoh, kita sudah tau ini akan erorr
# maka

angka = 0
try:
    # ini adalah Exception
    hasil = 10/angka
except ZeroDivisionError as erorr_massage:
    print(erorr_massage)


# atau bisa juga seperti ini


# angka = 0
# try:
#     # ini adalah Exception
#     hasil = 10/angka
# except Exception as erorr_massage:
#     print(erorr_massage)

