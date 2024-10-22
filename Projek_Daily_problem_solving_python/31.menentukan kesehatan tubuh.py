# ini merupakan sebuah program menentukan kesehatan tubuh
# di buat pada 21/10/2024
# di buat oleh Rafa Khadafi
import os

while True:
    os.system("cls")
    print(30 * "\033[94m=")
    print("\033[94mPROGRAM MENENTUKAN KESEHATAN TUBUH\033[0m".center(29))
    print(30 * "\033[94m=")
    print()
    try:            
        # Meminta input dari pengguna
        berat_badan = float(input("Masukkan berat badan Anda (contoh 70) = "))
        tinggi_badan = float(input("Masukkan tinggi badan Anda (contoh 1.75) = "))
        usia = int(input("Masukkan usia Anda (dalam tahun) = "))

        # Menghitung BMI
        # BMI = Body Mass Index = indeks massa tubuh
        bmi = berat_badan  /  (tinggi_badan ** 2)

        # Menentukan kategori BMI dan risiko kesehatan
        if bmi < 18.5:
            kategori = " anda Kekurangan berat badan"
            risiko = "anda beresiko tinggi untuk:\n- Malnutrisi\n- Osteoporosis\n- Sistem imun yang lemah"
        elif 18.5 <= bmi < 24.9:
            kategori = "Berat badan normal"
            risiko = "anda beresiko rendah untuk masalah kesehatan."
        elif 25 <= bmi < 29.9:
            kategori = "Kelebihan berat badan"
            risiko = "anda resiko meningkat untuk:\n- Diabetes tipe 2\n- Penyakit jantung\n- Tekanan darah tinggi"
        else:
            kategori = "Obesitas"
            risiko = "anda beresiko tinggi untuk:\n- Diabetes tipe 2\n- Penyakit jantung\n- Hipertensi\n- Masalah tidur (sleep apnea)\n- Beberapa jenis kanker"

        # Menampilkan hasil
        print(f"\nIndeks Massa Tubuh (BMI) Anda: {bmi:.2f}")
        print(f"Kategori: {kategori}")
        print("Risiko kesehatan:")
        print(risiko)
        while True:
            isdone = input("Apakah masih mau lagi? (y/t) = ").strip().lower()
            if isdone == "y":
                break  # Kembali ke awal loop
            elif isdone == "t":
                print("Terima kasih! Program selesai.")
                exit()  # Keluar dari program
            else:
                print("Input tidak valid. Silakan masukkan 'y' untuk ya atau 't' untuk tidak.")
    except ValueError:
        print("Anda memasukkan data yang salah.")
        print("Silakan masukkan angka bulat atau float.")