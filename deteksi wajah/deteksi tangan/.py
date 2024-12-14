from cvzone.HandTrackingModule import HandDetector
import cv2
import math
from pynput.mouse import Controller, Button 
import time

mouse = Controller()
camera = cv2.VideoCapture(0)

# Mengecek apakah kamera berhasil dibuka
if not camera.isOpened():
    print("Kamera tidak ditemukan atau tidak dapat dibuka.")
    exit()

detector = HandDetector(detectionCon=0.3, maxHands=1)

def main():
    
    
    while True:
        ret, frame = camera.read()
        frame = cv2.flip(frame, 1)
        if not ret:
            print("Gagal membaca frame dari kamera.")
            break         

        hands, gambar = detector.findHands(frame)

        if hands:
            hand = hands[0]  # Mengambil tangan pertama jika lebih dari satu tangan terdeteksi
            lmList = hand["lmList"]  # Menggunakan 'lmList' untuk mendapatkan titik landmark tangan

            if len(lmList) != 0:
                # Mendapatkan koordinat titik pada jari-jari tertentu (indeks dan jempol)
                x1, y1 = lmList[4][0], lmList[4][1]  # Titik pada ujung jempol (ID 4)
                x2, y2 = lmList[8][0], lmList[8][1]  # Titik pada ujung telunjuk (ID 8)
                x3, y3 = lmList[12][0], lmList[12][1] # titik pada ujung jari tengah (id 12)
                cx, cy = (x1 + x2) // 2, (y1 + y2) // 2  # Titik tengah antara jempol dan telunjuk

                # Menambahkan lingkaran pada jari dan garis antara jempol dan telunjuk
                cv2.circle(gambar, (x1, y1), 5, (0, 0, 255), cv2.FILLED)
                cv2.circle(gambar, (x2, y2), 5, (0, 0, 255), cv2.FILLED)
                cv2.circle(gambar, (x3, y3), 5, (0, 0, 0), cv2.FILLED)
                cv2.line(gambar, (x1, y1), (x2, y2), (0, 0, 0), 3)

                panjang = math.hypot(x2 - x1, y2 - y1)  # Menghitung jarak antara kedua titik
                if panjang < 50:
                    # Scroll ke atas jika jarak kecil
                    mouse.scroll(0, 1)  
                    cv2.circle(gambar, (cx, cy), 5, (0, 255, 0), cv2.FILLED)  # Tampilkan titik hijau
                    
                    # Menggerakkan kursor ke posisi telunjuk
                    mouse.position = (x3, y3)  # Menggerakkan kursor ke posisi telunjuk

                elif panjang > 100:
                    mouse.scroll(0, -1)  # Scroll ke bawah jika jarak besar
                    cv2.circle(gambar, (cx, cy), 5, (0, 0, 0), cv2.FILLED)  # Tampilkan titik merah
                else:
                    cv2.circle(gambar, (cx, cy), 5, (0, 0, 255), cv2.FILLED)  # Tampilkan titik ungu

        time.sleep(0.016)
        cv2.imshow("program scroll", gambar)
        cv2.resizeWindow("program scroll", 700, 500)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    camera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()