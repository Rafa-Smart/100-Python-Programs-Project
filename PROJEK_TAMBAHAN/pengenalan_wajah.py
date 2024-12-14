import os
import cv2

# Clear the screen
os.system("cls" if os.name == "nt" else "clear")

# Create directories if they do not exist
folder_data_wajah = "data_wajah"
os.makedirs(folder_data_wajah, exist_ok=True)

folder_latih_wajah = "data_latih"
os.makedirs(folder_latih_wajah, exist_ok=True)

# Initialize camera
camera = cv2.VideoCapture(0)

# Load face detection model
face_deteksi = cv2.CascadeClassifier("face_referensi.xml")
if face_deteksi.empty():
    print("tidak bisa mendeteksi wajah anda.")
    camera.release()
    exit()

# Initialize face recognizer
face_recognizer = cv2.face.LBPHFaceRecognizer_create()
name = ["tidak diketahui"]  

# menambahkan nama pada list
for filename in os.listdir(folder_latih_wajah):
    if filename.endswith(".xml"):
        nama_dari_file = filename.split("_")[0]  
        name.append(nama_dari_file)  # menambahkan nama kelist
        face_recognizer.read(os.path.join(folder_latih_wajah, filename))  # Load model

def close_window(camera):
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        camera.release()
        cv2.destroyAllWindows()
        exit()

def main():
    while True:
        # Clear the screen
        os.system("cls" if os.name == "nt" else "clear")
        
        # Capture frame from camera
        ret, frame = camera.read()
        if not ret:
            print("gagal untuk mengambil gambar.")
            break

        frame = cv2.flip(frame,1)  # agar muka sama kayak di cermin
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert frame to grayscale
        wajah = face_deteksi.detectMultiScale(frame_gray, scaleFactor=1.1)

        # Draw rectangles around detected faces
        for (x, y, w, h) in wajah:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 3)
            id, confidence = face_recognizer.predict(frame_gray[y:y + h, x:x + w])

            if confidence <= 40:  # Confidence threshold
                name_id = name[id] if 0 <= id < len(name) else name[0]
                print(f"{name_id} telah masuk kelas")
            else:
                name_id = name[0]
 
            confidence_text = f"{round(100 - confidence)} % kemiripan"
            posisi_x = x + 25
            posisi_y = y - 15
            cv2.putText(frame, str(name_id), (posisi_x, posisi_y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2)
            cv2.putText(frame, confidence_text, (posisi_x - 15, posisi_y + h + 50), cv2.FONT_HERSHEY_SIMPLEX, 1.1, (0, 255, 0), 5)

        cv2.imshow("Wajahmu Sayang", frame)
        close_window(camera)

    # Release camera when done
    camera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()