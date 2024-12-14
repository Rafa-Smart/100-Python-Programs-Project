import os
from pytube import YouTube
from pathlib import Path

# Hapus konsol untuk Windows atau Unix
os.system("cls" if os.name == "nt" else "clear")

def display():
    print(30 * "=")
    print("PROGRAM MENDOWNLOAD VIDEO YOUTUBE".center(30))
    print(30 * "=")

def unduh_video(url):
    try:
        yt = YouTube(url)
        video = yt.streams.get_highest_resolution()  # Mendapatkan resolusi tertinggi
        nama_folder_gede = Path(r"C:\PROJEK_PROJEK_PYTHON\hasil download video")

        if not os.path.exists(nama_folder_gede):
            os.makedirs(nama_folder_gede)  # Membuat folder jika tidak ada

        # Mengambil info judul dari video YouTube
        title = yt.title
        
        # Mengganti nama judul yang aman bagi Windows
        title = title.replace(" ", "_").replace("/", "_").replace("\\", "_")
        
        # Membuat nama file berdasarkan judul dan menggunakan ekstensi yang benar
        name_file = f"{title}.mp4"

        # Membuat path file
        file_path = nama_folder_gede / Path(name_file)

        # Download video
        video.download(nama_folder_gede)  # Download video di folder yang ditunjuk
        print("proses mendownload......")
        print(f"File {file_path} telah dibuat di folder {nama_folder_gede}")
        print("info video :")
        print(f"judul : {title}\npenonton : {yt.views:,.}\nwaktu : {yt.length // 60} menit {yt.length % 60} detik")
    except Exception as e:
        print(f"Kesalahan yang terjadi adalah : {e}")

if __name__ == "__main__":
    display()
    url_video = input("Masukan URL video yang ingin diunduh: ")
    unduh_video(url_video)