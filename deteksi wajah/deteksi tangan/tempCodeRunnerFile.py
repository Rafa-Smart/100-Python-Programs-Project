 # Cek jika semua jari tertutup
                if fingers == [0, 0, 0, 0, 0]:  # Semua jari tertutup
                    zoom_level = 1.5  # Zoom in
                    screenshot_taken = False  # Reset status screenshot
                elif fingers == [1, 1, 0, 0, 0]:  # Hanya jari telunjuk dan tengah terbuka
                    zoom_level = 1.0  # Tidak ada zoom
                    screenshot_taken = False  # Reset status screenshot
                elif fingers == [0, 1, 0, 0, 1]:  # Jari telunjuk, jempol, dan kelingking terbuka
                    zoom_level = 1.0  # Tidak ada zoom
                    screenshot_taken = True  # Menandakan screenshot diambil
                else:  # Jika jari terbuka lainnya
                    zoom_level = 0.5  # Zoom out
                    screenshot_taken = False  # Reset status screenshot