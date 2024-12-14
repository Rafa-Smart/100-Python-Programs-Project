import tkinter as tk

def start_timer():
    try:
        # Ambil waktu dari entry dan konversi ke detik
        total_seconds = int(entry.get())
        countdown(total_seconds)
    except ValueError:
        label.config(text="Masukkan angka yang valid!")

def countdown(seconds):
    if seconds >= 0:
        # Mengubah detik menjadi format mm:ss
        minutes, secs = divmod(seconds, 60)
        time_format = f"{minutes:02}:{secs:02}"
        label.config(text=time_format)
        window.after(1000, countdown, seconds - 1)
    else:
        label.config(text="Waktu Habis!")

# Membuat jendela utama
window = tk.Tk()
window.title("Timer")
# Entry untuk memasukkan waktu dalam detik
entry = tk.Entry(window)
entry.pack(pady=10)

# Tombol untuk memulai timer
start_button = tk.Button(window, text="Mulai Timer", command=start_timer)
start_button.pack(pady=10)

# Label untuk menampilkan waktu
label = tk.Label(window, text="00:00", font=("Helvetica", 48))
label.pack(pady=20)

# Menjalankan aplikasi
window.mainloop()
