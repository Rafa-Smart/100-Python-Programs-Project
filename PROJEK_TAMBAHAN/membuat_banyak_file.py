import os
from pathlib import Path
nama_folder_gede = Path("C:\\projek mandiri")
if not os.path.exists(nama_folder_gede):
    os.makedirs(nama_folder_gede)

nama_folder = nama_folder_gede / Path("folder_kiriman")
if not os.path.exists(nama_folder):
    os.makedirs(nama_folder)

name_file = "file_kiriman.py"
# fungsi / pada library pathlib adalah untuk menggabungkan path
file_path = nama_folder / name_file

file_path.write_text("ini adalah file buatan sendiri")
print(f"file {name_file} telah dibuat di folder {nama_folder} didalam folder {nama_folder_gede}")