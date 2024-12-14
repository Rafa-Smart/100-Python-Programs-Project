'''type hint untuk fungsi'''

# bentuk standar fungsi

# def nama_fungsi(parameter/argumen):
    # print(parameter)
# nama_fungsi("rafa")
# nama_fungsi(True)

# sekarang bagaimana jika gini
'''
studi kasus
# def nama_fungsi(parameter/argumen):
    # HASIL = parameter**2
    # print(HASIL)
# nama_fungsi(3)
# nama_fungsi("rafa")
# nama_fungsi(True)
'''
# nah bagaimana jika parameternya pake string(yang tidak bisa di kuadratkan)

# jadi kita harus memberi tahu user bahwa ini adalah fungsi yang wajib 
# misal memasukan argumen yang bertipe int atau float, dan bukan string
# caranya dengan type hint

# penggunaan type hint
'''
def fungsi_dengan_hint(parameter:masukan typenya int)     <...
    output = 10**parameter                                   .
    return output                                            .
HASIL = fungsi_dengan_hint(2)                                .
print(HASIL)                                                 .
'''                                                        
# jadi saat kita menggerakan mouse tepat ke parameternya  ----
# maka akan ada info bahwa parameter ini khusus memasukan input bertipe int

# contoh lagi
def fungsi_tambah(angka1,angka2:int) -> int: # jadi ini maksudnya hasilnya akan menghasilnya int
    hasil = angka1 + angka2
    print(f"hasilnya adalah = {hasil}")
    return hasil
fungsi_tambah(4,7)

# jadi gini 
# def fungsi(angka:int) -> int:
    # print("rafa")
# jadi int di angka:int --> adalah maksudnya inputnnya harus integer
# --> int adalah maksudnya outputnya akan integer