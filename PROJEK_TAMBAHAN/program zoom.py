# penjelasan program 
# 1. jika anda menutup semua jari anda maka akan zoom in
# 2. jika anda membuka semua jari  maka akan zoom out
# 3. jika anda menutup semua jari kecuali jari telunjuk dan tengah maka tidak akan terjadi apa apa

import cv2
from cvzone.HandTrackingModule import HandDetector

# Membuat fungsi untuk menutup window
def close_window(camera):
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        camera.release()
        cv2.destroyAllWindows()
        exit()

# untuk membuka kamera utama di laptop saya
camera = cv2.VideoCapture(0)

detector = HandDetector(detectionCon=0.3, maxHands=1)
# berati 30 % tingkat kepercayaan dan leih sensitif

# membuat variable inisiasi untuk zoom
zoom_level = 1.0
# jadi ini itu adalah zoom default

# program utama 
def main():
    # membuat variable global buat zoom_level
    global zoom_level
    # mengecek apakah camera bisa terdeteksi dan terbuka
    while camera.isOpened():
        ret, frame = camera.read()
        if not ret:
            print("Gagal membuka kamera")
            break

        frame = cv2.flip(frame, 1)

        # program mendeteksi tangan
        hands, gambar = detector.findHands(frame)

         # Jika tangan terdeteksi
        if hands: 
            hand = hands[0]  # Mengambil tangan pertama
            lmList = hand["lmList"]  # Mendapatkan daftar landmark tangan cari aja di google
                                    #   dan baca dokumentasinya
            
            
            # Menentukan posisi teks untuk ditampilkan di bawah telapak tangan
            text_x = int(lmList[0][0]) - 110 # Posisi x dari pergelangan tangan
            text_y = int(lmList[0][1]) + 50 # Posisi y dari pergelangan tangan, sedikit di bawah

 

             # Jika titik-titik landmark jari terbaca dan terdeteksi maka :
            if len(lmList) != 0: 
                # Mendapatkan dan mendeteksi jari jari tnangn
                fingers = detector.fingersUp(hand)



                # kondisi kondisi jari jari tangan :

                # Cek jika semua jari tertutup maka :
                if fingers == [0, 0, 0, 0, 0]:  # ini kode jika Semua jari tertutup
                    # menambah kan zoom level
                    zoom_level = 1.5  # maka akan Zoom in
                    cv2.putText(frame,"Zoom In",(text_x + 20,text_y),cv2.FONT_HERSHEY_PLAIN,2,(255,0,0),4)

                # cek jika hanya jari telunjuk dan tnegah saja yang terbuka maka :
                elif fingers == [0, 1, 1, 0, 0]:  # ini kode jari telunjuk dan tengah terbuka
                    zoom_level = 1.0  # Tidak ada zoom
                    cv2.putText(frame,"Tidak Zoom",(text_x,text_y),cv2.FONT_HERSHEY_PLAIN,2,(255,0,0),4)


                # Jika semua jari terbuka maka :
                else: 
                    # mengurangi zoom level
                    zoom_level = 0.5  # Zoom out
                    cv2.putText(frame,"Zoom Out",(text_x - 20,text_y),cv2.FONT_HERSHEY_PLAIN,2,(255,0,0),4)

                # Mengubah ukuran gambar berdasarkan zoom level
                height, width,_ = gambar.shape
                gambar = cv2.resize(gambar, (int(width * zoom_level), int(height * zoom_level)))

        cv2.imshow("Tangan mu", gambar)
        close_window(camera)

if __name__ == "__main__":
    main()


# Format Daftar fingers:

# Daftar fingers terdiri dari 5 elemen, masing-masing mewakili jari tangan:
# fingers[0]: Jari kelingking
# fingers[1]: Jari manis
# fingers[2]: Jari tengah
# fingers[3]: Jari telunjuk
# fingers[4]: Jari ibu jari
# Nilai dalam Daftar:

# Setiap elemen dalam daftar fingers dapat memiliki dua nilai:
# 0: Menandakan bahwa jari tersebut tertutup.
# 1: Menandakan bahwa jari tersebut terbuka.
# Contoh fingers == [0, 0, 0, 0, 0]
# Makna:
# Ketika kondisi if fingers == [0, 0, 0, 0, 0]: terpenuhi, itu berarti semua jari tangan tertutup. Dalam konteks aplikasi, ini bisa digunakan untuk mengindikasikan bahwa pengguna ingin melakukan suatu tindakan tertentu, seperti memperbesar tampilan (zoom in).
# Contoh Lain
# fingers == [1, 1, 0, 0, 0]:

# Ini berarti jari telunjuk dan jari tengah terbuka, sementara jari lainnya tertutup. Dalam konteks aplikasi, ini bisa digunakan untuk menunjukkan bahwa pengguna tidak ingin melakukan zoom atau ingin melakukan tindakan tertentu yang berbeda.
# fingers == [1, 1, 1, 1, 1]:

# Ini berarti semua jari terbuka, yang bisa digunakan untuk mengindikasikan tindakan lain, seperti zoom out.