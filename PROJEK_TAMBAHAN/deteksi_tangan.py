import cv2
from cvzone.HandTrackingModule import HandDetector

# Membuat fungsi untuk menutup window
def close_window(camera):
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        camera.release()
        cv2.destroyAllWindows()
        exit()

# Membuka kamera utama
camera = cv2.VideoCapture(0)

detector = HandDetector(detectionCon=0.3, maxHands=1)

def main():
    while camera.isOpened():
        ret, frame = camera.read()
        if not ret:
            print("Gagal membaca kamera")
            break

        # Membalik gambar agar seperti cermin
        frame = cv2.flip(frame, 1)

        # Mendeteksi tangan
        hands, gambar = detector.findHands(frame)

        if hands:  # Jika tangan terdeteksi
            hand = hands[0]  # Mengambil tangan pertama
            lmList = hand["lmList"]  # Mendapatkan daftar landmark tangan
            
            if len(lmList) != 0:  # Jika ada titik-titik landmark
                # Mendapatkan koordinat dari ujung jempol dan telunjuk
                x1, y1 = lmList[4][0], lmList[4][1]  # Jempol
                x2, y2 = lmList[8][0], lmList[8][1]  # Telunjuk

                # Menambahkan lingkaran pada jari, tapi tanpa garis
                cv2.circle(gambar, (x1, y1), 5, (0, 0, 255), cv2.FILLED)
                cv2.circle(gambar, (x2, y2), 5, (0, 0, 255), cv2.FILLED)

        cv2.imshow("Tangan mu", gambar)
        close_window(camera)

if __name__ == "__main__":
    main()
