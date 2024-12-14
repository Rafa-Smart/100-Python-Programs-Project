# penelasan program 
# 1. tempatkan kursor di tempat yang ingin di scroll
# 2. lakukan scroll ke atas dengan cara menjauhkan jarak antara jempol dan telunjuk
# 2. lakukan scroll ke bawah dengan cara mendekatkan jarak antara jempol dan telunjuk


# Mengimpor modul yang diperlukan
from cvzone.HandTrackingModule import HandDetector  # Mengimpor modul untuk mendeteksi tangan
import cv2  # Mengimpor OpenCV untuk pemrosesan gambar
import math  # Mengimpor modul matematika untuk perhitungan
from pynput.mouse import Controller  # Mengimpor modul untuk mengontrol mouse
import time  # Mengimpor modul untuk mengatur waktu

# Membuat objek Controller untuk mengontrol mouse
mouse = Controller()  
# Membuka kamera dengan ID 0 (kamera default)
kamera = cv2.VideoCapture(0)

# Mengecek apakah kamera berhasil dibuka
if not kamera.isOpened():  
    print("Kamera tidak ditemukan atau tidak dapat dibuka.")  # Menampilkan pesan jika kamera tidak dapat dibuka
    exit()  # Keluar dari program jika kamera tidak tersedia

# Membuat objek HandDetector dengan tingkat kepercayaan deteksi 0.3 dan maksimum 1 tangan
detektor = HandDetector(detectionCon=0.3, maxHands=1)

# Variabel untuk menyimpan nilai scroll sebelumnya
scroll_sebelumnya = 0  

def main():  # fungsi utama
    global scroll_sebelumnya  # Menggunakan variabel global scroll_sebelumnya
    while True:  # Loop utama program
        ret, frame = kamera.read()  # Membaca frame dari kamera
        frame = cv2.flip(frame, 1)  # Membalik frame secara horizontal
        if not ret:  # Mengecek apakah frame berhasil dibaca
            print("Gagal membaca frame dari kamera.")  # Menampilkan pesan jika gagal
            break  # Keluar dari loop jika gagal

        # Mendeteksi tangan dalam frame
        tangan, gambar = detektor.findHands(frame)  

        if tangan:  # Jika ada tangan yang terdeteksiq
            tangan_pertama = tangan[0]  # Mengambil tangan pertama jika lebih dari satu tangan terdeteksi
            daftar_landmark = tangan_pertama["lmList"]  # Menggunakan 'lmList' untuk mendapatkan titik landmark tangan

                        # Menentukan posisi teks untuk ditampilkan di bawah telapak tangan
            text_x = int(daftar_landmark[0][0]) - 110 # Posisi x dari pergelangan tangan
            text_y = int(daftar_landmark[0][1]) + 50 # Posisi y dari pergelangan tangan, sedikit di bawah

            if len(daftar_landmark) != 0:  # Mengecek apakah ada landmark yang terdeteksi
                # Mendapatkan koordinat titik pada jari-jari tertentu (indeks dan jempol)
                x1, y1 = daftar_landmark[4][0], daftar_landmark[4][1]  # Titik pada ujung jempol (ID 4)
                x2, y2 = daftar_landmark[8][0], daftar_landmark[8][1]  # Titik pada ujung telunjuk (ID 8)
                cx, cy = (x1 + x2) // 2, (y1 + y2) // 2  # Titik tengah antara jempol dan telunjuk

                # Menambahkan lingkaran pada jari dan garis antara jempol dan telunjuk
                cv2.circle(gambar, (x1, y1), 5, (0, 0, 255), cv2.FILLED)  # Lingkaran merah di jempol
                cv2.circle(gambar, (x2, y2), 5, (0, 0, 255), cv2.FILLED)  # Lingkaran merah di telunjuk
                cv2.line(gambar, (x1, y1), (x2, y2), (0, 0, 0), 3)  # Garis hitam antara jempol dan telunjuk

                panjang = math.hypot(x2 - x1, y2 - y1)  # Menghitung jarak antara kedua titik
                jumlah_scroll = 0  # Inisialisasi variabel untuk jumlah scroll

                # Menentukan arah scroll berdasarkan panjang jarak antara jempol dan telunjuk
                if panjang < 50:  
                    jumlah_scroll = 1  # Scroll ke atas jika jarak kurang dari 50
                elif panjang > 100:  
                    jumlah_scroll = -1  # Scroll ke bawah jika jarak lebih dari 100

                # Membuat agar scroll jadi lebih halus
                if jumlah_scroll != 0:  # Jika ada scroll yang perlu dilakukan
                    # Menggunakan program untuk membuat scroll lebih halus
                    scroll_sebelumnya += jumlah_scroll * 0.1  # Sensitivitas scroll
                    mouse.scroll(0, scroll_sebelumnya)  # Melakukan scroll pada mouse
                    # kenapa 0 karena index pertama dari argumen ini adalah y = horizontal
                    # dan index ke 1 dari argumen ini adalah x = vertikal maka
                    # agar tidak scroll ke kanan atau ke samping maka di buat nilainya adalah 0
                    scroll_sebelumnya = max(min(scroll_sebelumnya, 1), -1)  # Batasi nilai scroll antara -1 dan 1
                    
            
                    
                # Tampilkan titik berdasarkan panjang
                if panjang < 50:
                    cv2.circle(gambar, (cx, cy), 5, (0, 255, 0), cv2.FILLED)  # Tampilkan titik hijau
                    cv2.putText(gambar,"Scroll Atas",(text_x + 35,text_y),cv2.FONT_HERSHEY_PLAIN,2,(0,0,255),4)

                elif panjang > 100:
                    cv2.circle(gambar, (cx, cy), 5, (0, 0, 0), cv2.FILLED)  # Tampilkan titik merah
                    cv2.putText(gambar,"Scroll Bawah",(text_x + 50,text_y),cv2.FONT_HERSHEY_PLAIN,2,(0,0,255),4)
                else:
                    cv2.circle(gambar, (cx, cy), 5, (0, 0, 255), cv2.FILLED)  # Tampilkan titik ungu

        time.sleep(0.016)
        cv2.imshow("program scroll", gambar)
        cv2.resizeWindow("program scroll", 700, 500)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    kamera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()