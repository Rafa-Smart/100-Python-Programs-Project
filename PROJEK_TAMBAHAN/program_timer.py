import tkinter as tk
import time

class MenghitungMundurWaktu:
    def __init__(self, master):
        self.master = master
        self.master.title("Timer Hitung Mundur")

        self.label = tk.Label(master, text="Masukkan waktu (detik):")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.start_button = tk.Button(master, text="Mulai", command=self.start_timer)
        self.start_button.pack()

        self.time_label = tk.Label(master, text="", font=("Helvetica", 48))
        self.time_label.pack()

        self.remaining_time = 0
        self.timer_running = False

    def start_timer(self):
        try:
            self.remaining_time = int(self.entry.get())
            self.timer_running = True
            self.update_timer()
        except ValueError:
            self.time_label.config(text="Masukkan angka yang valid!")

    def update_timer(self):
        if self.remaining_time > 0 and self.timer_running:
            mins, secs = divmod(self.remaining_time, 60)
            timer_format = '{:02d}:{:02d}'.format(mins, secs)
            self.time_label.config(text=timer_format)
            self.remaining_time -= 1
            self.master.after(1000, self.update_timer)
        else:
            self.time_label.config(text="Waktu Habis!")
            self.timer_running = False

if __name__ == "__main__":
    root = tk.Tk()
    countdown_timer = MenghitungMundurWaktu(root)
    root.mainloop()