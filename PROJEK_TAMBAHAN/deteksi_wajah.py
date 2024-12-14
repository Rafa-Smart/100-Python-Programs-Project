import cv2

# Muat model deteksi wajah
face_referensi = cv2.CascadeClassifier("face_referensi.xml")
camera = cv2.VideoCapture(0)

def deteksi_wajah(frame):
    # Ubah frame menjadi grayscale
    alat_pengoptimal = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    # Deteksi wajah
    wajah = face_referensi.detectMultiScale(alat_pengoptimal, scaleFactor=1.1)
    return wajah

def menggambar_kotak_wajah(frame):
    # Dapatkan koordinat wajah
    for x, y, lebar, tinggi in deteksi_wajah(frame):
        # Gambar kotak di sekitar wajah
        cv2.rectangle(frame, (x, y), (x + lebar, y + tinggi), (255, 0, 0), thickness=4)

def keluar_program():
    camera.release()
    cv2.destroyAllWindows()
    exit()

def main():
    while True:
        # Baca frame dari kamera
        _, frame = camera.read()
        frame = cv2.flip(frame,1)
        # Gambar kotak di sekitar wajah
        menggambar_kotak_wajah(frame)
        # Tampilkan frame
        cv2.imshow("program face_detection", frame)
        # Keluar jika tombol 'l' ditekan
        if cv2.waitKey(1) & 0xFF == ord("l"):
            keluar_program()

if __name__ == "__main__":
    main()