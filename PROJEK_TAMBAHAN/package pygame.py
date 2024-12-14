import pygame

# struktur game 
# 1. init
# 2. user input / input dari data base
# 3. update asset pada game 
# 4. render ke display

# coba kita buat

# 1. init 
pygame.init() # untuk memulai gamenya

# beberapa variable gamenya
is_run = True

# membuat objek game nya

# koordianat / posisi
x = 250
y = 250

# ukuran objek
panjang = 20
lebar = 20

# kecepatan gerak
speed = 10



# membuat display untuk menempatkan semua objeknya
window = pygame.display.set_mode((500 ,500))


# while True: # untuk melooping gamenya jadi ga langsung close

#     # membuat keluarnya / memberhentikan gamenya
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             print("game selesai")
#             break

# pygame.QUIT()

# nah yang diatas jika kita tulis pygame.QUIT()
# niatnya adalah agar saat kita close window gamenya
# maka akan langsung ke close
# tapi tidak bisa karena kita ngebreak di for 
# bukan di while truenya maka caranya adalah

while is_run: # untuk melooping gamenya jadi ga langsung close

# 2. user input

    # membuat keluarnya / memberhentikan gamenya
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_run = False

# 3. update asset
window.fill((255, 255, 255))  # Mengisi layar dengan warna putih
pygame.draw.rect(window, (0, 0, 255), (x, y, panjang, lebar))  # Menggambar objek (segi empat)
    
# 4. render ke display
pygame.display.update()  # agar mengupdate tampilan






# membuat bisa mengclose window dari gamenya
# nah ini akan bisa
pygame.QUIT()

