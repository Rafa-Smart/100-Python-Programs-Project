# ini merupakan sebuah program konversi tempratur 
# di buat pada 07/10/2024
# di buat oleh Rafa Khadafi
print(20*"=")
print("PROGRAM KONVERSI TEMPERATUR".center(30))
print(20*"=")

celcius = float(input("masukan suhu dalam celcius :"))
print("suhu celcius = ",celcius, "celcius")

reamur = (4/5)* celcius
print("suhu dalam reamur = ",reamur, "reamur")

fahrenheit = ((9/5) * celcius) + 32
print("suhu dalam fahrenheit = ",fahrenheit, "fahrenheit")

kelvin = celcius + 273
print("suhu dalam kelvin = ",kelvin,"kelvin")