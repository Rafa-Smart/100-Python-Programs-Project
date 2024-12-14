# penjelasan program ini

# 1. jika kamu membuka seluruh jari kamu maka tidak ada aksi apa apa
# 2. jika kamu menutup semua jari kecuali jari telunjuk saja maka kursor akan bergerak sesuai dnegan jari telunjuk kamu
#       dan untuk klick kiri kamu hanya perlu mengangkat lagi jari tengah kamu
#           artinya kamu akan klick kiri jika menutup semua jari kecuali jari telunjuk dan tengah
#       dan untuk klick kanan kamu hanya perlu mengangkat lagi jari kelingking kamu 
#           artinya kamu akan klick kanan jika menutup semua jari kecuali jari telunjuk dan kelingking




import cv2  # Mengimpor pustaka OpenCV untuk pemrosesan gambar
import numpy as np  # Mengimpor pustaka NumPy untuk operasi array
import pyautogui  # Mengimpor pustaka PyAutoGUI untuk mengontrol mouse dan keyboard
from cvzone.HandTrackingModule import HandDetector  # Mengimpor modul deteksi tangan dari CVZone

# Membuat fungsi untuk menutup window
def close_window(camera):
    key = cv2.waitKey(1) & 0xFF  # Mengambil input dari keyboard
    if key == ord("q"):  # Jika tombol 'q' ditekan
        camera.release()  # akan mematikan kamera
        cv2.destroyAllWindows()  # Menutup semua jendela dari OpenCV
        exit()  # Keluar dari program

# Membuka kamera utama yang ada pada laptop
camera = cv2.VideoCapture(0)  # Mengakses kamera dengan indeks 0 yaitu kamera bawaan / utama

# Membuat objek HandDetector dengan tingkat kepercayaan deteksi dan jumlah tangan maksimum
detector = HandDetector(detectionCon=0.3, maxHands=1)

def program_utama():
    while camera.isOpened():  # jadi Selama kamera terbuka
        ret, frame = camera.read()  # Membaca frame dari kamera
        if not ret:  # Jika gagal membuka kamera maka akan menampilkan pesan
            print("Gagal membuka kamera") 
            break  # Keluar dari loopingan
        frame = cv2.flip(frame,1)


        # Mendeteksi tangan
        hands, gambar = detector.findHands(frame)  # Mencari tangan dalam frame

        if hands:  # Jika tangan terdeteksi
            hand = hands[0]  # Mengambil tangan pertama
            lmList = hand["lmList"]  # Mendapatkan daftar landmark tangan liat aja di dokmentasi goggle
            
            if len(lmList) != 0:  # Jika berhasil menemukan titik-titik landmark
                # Mendapatkan status jari
                fingers = detector.fingersUp(hand)  # Mendapatkan status jari yang terbuka

                # Mendapatkan koordinat dari ujung jari telunjuk dan jari kelingking
                x1, y1 = lmList[8][0], lmList[8][1]  # Koordinat ujung jari telunjuk
                x5, y5 = lmList[20][0], lmList[20][1]  # Koordinat ujung jari kelingking

                # Mengatur ukuran gambar untuk kursor
                h, w, _ = frame.shape  # Mendapatkan tinggi dan lebar frame
                x1 = np.clip(x1, 0, w)  # Mengatur x1 agar tidak melebihi lebar frame
                y1 = np.clip(y1, 0, h)  # Mengatur y1 agar tidak melebihi tinggi frame

                # Jika semua jari tertutup
                if sum(fingers) == 0:
                    pass  # Tidak ada aksi / dilewat ajah

                # Jika hanya telunjuk yang terbuka
                elif fingers[1] == 1 and sum(fingers) == 1:
                    # Menggerakkan kursor
                    pyautogui.moveTo(x1, y1)  # Menggerakkan kursor sesuai dengan posisi telunjuk

                # Jika telunjuk dan jari tengah terbuka saja
                elif fingers[1] == 1 and fingers[2] == 1 and sum(fingers) == 2:
                    # Klik kiri
                    pyautogui.click(button='left')  # Melakukan klik kiri
                    cv2.putText(gambar, "Klik Kiri!", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)  # Menampilkan teks "Klik Kiri!"

                # Jika telunjuk dan kelingking terbuka
                elif fingers[1] == 1 and fingers[4] == 1 and sum(fingers) == 2:
                    # Klik kanan
                    pyautogui.click(button='right')  # Melakukan klik kanan
                    cv2.putText(gambar, "Klik Kanan!", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)  # Menampilkan teks "Klik Kanan!"

        cv2.imshow("program deteksi tangan", gambar) 
        close_window(camera)  

if __name__ == "__main__":
    program_utama()  