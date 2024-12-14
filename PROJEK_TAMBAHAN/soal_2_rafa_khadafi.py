from datetime import datetime as dt
print("soal 2")
print()


hari_ini = dt.now()

format_waktu = hari_ini.strftime("%d of %B on %Y, %H:%M:%S %p")

print(f"hasil= {format_waktu}")

