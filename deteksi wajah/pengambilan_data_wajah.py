import cv2
import os

def close_window(camera, ambil_data):
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        camera.release()
        cv2.destroyAllWindows()
        exit()
    elif ambil_data > 100:
        print("Pengambilan data wajah selesai.")
        camera.release()
        cv2.destroyAllWindows()
        exit()
camera = cv2.VideoCapture(0)
face_deteksi = cv2.CascadeClassifier("face_referensi.xml")
mata_deteksi = cv2.CascadeClassifier("mata_referensi.xml")

nama_user = str(input("masukan nama anda = "))
id_wajah = int(input("Masukkan nomor absen Anda = "))


folder_data_wajah = "data_wajah"

# mengetes jika ternyata folder data_wajah tidak ada
# maka akan langsung dibuatkan oleh program ini
if not os.path.exists(folder_data_wajah):
    os.makedirs(folder_data_wajah)

jumlah_data = 1

def main():
    global jumlah_data
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("Arahkan wajah Anda ke webcam")
        print("Proses pengambilan data wajah...")
        _, frame = camera.read()
        frame = cv2.flip(frame,1)  # agar muka sama kayak di cermin
        frame_abu = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        wajah = face_deteksi.detectMultiScale(frame_abu, scaleFactor=1.1) 

        # Menggambar kotak pada wajah yang terdeteksi
        for (x, y, w, h) in wajah:
            frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 0), 3)
            cv2.putText(frame, "Halo Sayang", (x + 80, y - 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)

            # memasukan foto foto ke folder data_wajah
            nama_file = f"{nama_user}.{jumlah_data}.jpg"
            cv2.imwrite(os.path.join(folder_data_wajah, nama_file), frame)
            jumlah_data += 1

            mata_abu = frame_abu[y:y+h, x:x+w]
            mata_berwarna = frame[y:y+h, x:x+w]
            mata = mata_deteksi.detectMultiScale(mata_abu)
            for (x_mata, y_mata, w_mata, h_mata) in mata:
                cv2.rectangle(mata_berwarna, (x_mata, y_mata), (x_mata + w_mata, y_mata + h_mata), (255, 0, 0), 2)

        cv2.imshow("Wajahmu Sayang", frame)
        # mamasukan parameter camera dan ambil_data ke fungsi close_window
        close_window(camera, jumlah_data)

if __name__ == "__main__":
    main()
