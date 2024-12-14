# contoh membuat exception

# misal 
# nah disini kita pengen jika a + b itu dua duanya harus number 
# tidak boleh pake string
from numbers import Number
# Kode ini mengimpor kelas Number dari modul numbers.
# Kelas ini digunakan untuk memeriksa apakah suatu nilai adalah
# angka (baik integer, float, dll).
def tambah(a,b):
    # malakukan pemeriksaan tipe data
    if not isinstance(a,Number) or not isinstance(b,Number):
        # pake logika or karena jika 2 2 nya salah
        # maka akan langsung di raise/except

        # membuat except erorr 
        raise ValueError("input pertama harus angka")
    return a + b
# print(tambah("a","c"))
print(tambah(8,6))

# jadi gini cara kerjanya
# isinstance(): Ini adalah fungsi bawaan Python yang digunakan untuk memeriksa apakah suatu nilai
# (misalnya, variabel) merupakan jenis data tertentu. Dalam hal ini, kita memeriksa apakah a dan b adalah angka.
# jadi di isnstantce ini kita bisa juga ngecek apakah string dll dan jangan lupa importnya

# Number: Ini adalah kelas dari modul numbers yang mencakup semua jenis angka, seperti integer (bilangan bulat) 
# dan float (bilangan desimal).
# not: Kata kunci ini digunakan untuk membalikkan hasil. Jika isinstance(a, Number) mengembalikan True (artinya a adalah angka),
# maka not akan mengubahnya menjadi False. Sebaliknya, jika a bukan angka, maka not akan membuatnya menjadi True.
# or: Ini adalah operator logika yang berarti "atau". Ini menghubungkan dua kondisi. Jika salah satu dari kondisi
# di sebelah kiri atau kanan adalah True, maka keseluruhan ekspresi akan menjadi True.

# Apa yang Dilakukan Kode Ini?
# Kode ini memeriksa apakah a tidak adalah angka atau b tidak adalah angka.
# Jika salah satu dari a atau b bukan angka, maka kondisi dalam if akan menjadi True,
# dan kode di dalam blok if (yaitu, menimbulkan exception) akan dijalankan.
# Contoh
# Jika a adalah 5 (angka) dan b adalah "c" (bukan angka):
# isinstance(a, Number) → True
# isinstance(b, Number) → False
# Karena salah satu adalah False, keseluruhan ekspresi menjadi True, dan exception akan ditimbulkan.
# Jika keduanya adalah angka, misalnya a = 5 dan b = 6:
# isinstance(a, Number) → True
# isinstance(b, Number) → True
# Maka keseluruhan ekspresi menjadi False, dan exception tidak akan ditimbulkan.
