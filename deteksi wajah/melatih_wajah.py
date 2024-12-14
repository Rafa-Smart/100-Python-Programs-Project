import cv2
import os
import numpy as np
from PIL import Image

# Membersihkan layar
os.system("cls" if os.name == "nt" else "clear")
folder_data_wajah = "data_wajah"
if not os.path.exists(folder_data_wajah):
    os.makedirs(folder_data_wajah)

folder_latih_wajah = "data_latih"
if not os.path.exists(folder_latih_wajah):
    os.makedirs(folder_latih_wajah)

# Fungsi untuk membaca gambar dalam folder data wajah
def get_image_label(path):
# Daftar untuk menyimpan path file gambar
    image_path = []

# Iterasi semua file dalam folder yang ditentukan
    for file_name in os.listdir(path):
    # Periksa apakah file memiliki ekstensi .jpg atau .png
        if file_name.endswith('.jpg') or file_name.endswith('.png'):
            # Gabungkan path folder dengan nama file
            full_path = os.path.join(path, file_name)
            # Tambahkan path lengkap ke daftar
            image_path.append(full_path)
    face_samples = []
    id_wajah_1 = []
    file_names = []  # Menyimpan nama file tanpa ekstensi
    
    for i in image_path:
        PILL_image = Image.open(i).convert("L")  # Convert ke grayscale
        image_num = np.array(PILL_image, "uint8")
        
        # Ambil ID dari nama file dan pastikan formatnya benar
# Ambil ID dari nama file dan pastikan formatnya benar
        try:
            file_parts = os.path.split(i)[-1].split(".")
            if len(file_parts) < 2:
                print(f"Nama file tidak valid: {i}")
                continue

            id_wajah_2 = int(file_parts[1])  # Ambil ID dari nama file
            wajah = face_detektor.detectMultiScale(image_num)
            
            # Ambil nama file tanpa ekstensi
            file_name = file_parts[0]  # Nama file tanpa ekstensi
            file_names.append(file_name)
            
            for (x, y, w, h) in wajah:
                face_samples.append(image_num[y:y+h, x:x+w])
                id_wajah_1.append(id_wajah_2)
        
        except ValueError:
            print(f"ID tidak valid untuk file: {i}")
            continue
    
    return face_samples, id_wajah_1, file_names

# Inisialisasi detektor wajah
face_detektor = cv2.CascadeClassifier("face_referensi.xml")

print("Program sedang melakukan training data wajah...")
print("Tunggu beberapa saat...")

# Mengambil semua gambar dan ID
face_samples, id_1, file_names = get_image_label(folder_data_wajah)

# Mengelompokkan wajah berdasarkan ID
unique_ids = np.unique(id_1)

# Melatih model untuk setiap ID unik dan menyimpan ke file terpisah
for unique_id in unique_ids:
    # Ambil semua wajah dengan ID yang sama
    wajah_id = [face_samples[i] for i in range(len(id_1)) if id_1[i] == unique_id]
    
    if len(wajah_id) > 0:
        face_recognizer = cv2.face.LBPHFaceRecognizer_create()  # Buat instance baru untuk setiap ID
        face_recognizer.train(wajah_id, np.array([unique_id] * len(wajah_id)))  # Latih model
        
        # Ambil semua indeks yang sesuai dengan unique_id
        indices = [i for i, id_val in enumerate(id_1) if id_val == unique_id]
        
        if indices:  # Pastikan ada indeks yang ditemukan
            index = indices[0]  # Ambil indeks pertama
            if index < len(file_names):  # Pastikan indeks dalam batas
                file_name_without_ext = file_names[index]  # Ambil nama file yang sesuai
                file_name = f"{folder_latih_wajah}/{file_name_without_ext}_{unique_id}.xml"
                
                face_recognizer.write(file_name)  # Simpan model
                print(f"Model untuk {file_name_without_ext} disimpan sebagai {file_name}.")
            else:
                print(f"Indeks {index} di luar jangkauan untuk file_names.")
        else:
            print(f"Tidak ada indeks yang ditemukan untuk ID {unique_id}.")

print(f"Sebanyak {len(unique_ids)} data wajah telah di training ke mesin.")