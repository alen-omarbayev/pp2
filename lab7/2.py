

# import pygame
# import os

# # Initialize Pygame
# pygame.init()

# # Set the screen dimensions
# screen_width = 400
# screen_height = 500
# screen = pygame.display.set_mode((screen_width, screen_height))
# pygame.display.set_caption("Pygame Music Player")

# # Set the directory where your music files are stored
# music_directory = "music"

# # Load image
# image = pygame.image.load(r"C:\Users\ASUS\OneDrive\Рабочий стол\pp2\pp2\lab7\shrek.jpg")  # Замените "image.jpg" на ваше изображение
# image = pygame.transform.scale(image, (screen_width, screen_height))
# image_rect = image.get_rect()

# # Set image position to center
# image_rect.center = (screen_width // 2, screen_height // 2)

# # Function to load and play music
# def play_music(file):
#     pygame.mixer.music.load(file)
#     pygame.mixer.music.play()

# # Function to pause music
# def pause_music():
#     pygame.mixer.music.pause()

# # Function to unpause music
# def unpause_music():
#     pygame.mixer.music.unpause()

# # Function to stop music
# def stop_music():
#     pygame.mixer.music.stop()

# # Function to display text on the screen
# def draw_text(text, x, y):
#     font = pygame.font.Font(None, 36)
#     text_surface = font.render(text, True, (255, 255, 255))
#     screen.blit(text_surface, (x, y))

# # Main loop
# running = True
# while running:
#     screen.fill((0, 0, 0))

#     # Get events
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_p:  # Play/Pause music
#                 if pygame.mixer.music.get_busy():
#                     if pygame.mixer.music.get_pos() > 0:
#                         pause_music()
#                     else:
#                         unpause_music()
#                 else:
#                     play_music(r"C:\Users\ASUS\OneDrive\Рабочий стол\pp2\pp2\lab7\Asphalt8.mp3")
#             elif event.key == pygame.K_s:  # Stop music
#                 stop_music()

#     # Draw image
#     screen.blit(image, image_rect)

#     # Display controls
#     draw_text("Press 'P' to Play/Pause, 'S' to Stop", 10, 10)

#     pygame.display.flip()

# pygame.quit()


import pygame
import os

# Initialize Pygame
pygame.init()

# Set the screen dimensions
screen_width = 1000
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Music Player")

# Load image
image = pygame.image.load(r"C:\Users\ASUS\OneDrive\Рабочий стол\pp2\pp2\lab7\shrek.jpg")  
image = pygame.transform.scale(image, (screen_width, screen_height))
image_rect = image.get_rect()

# Set the directory where your music files are stored
music_directory = "music"

#musicList
song1 = r"C:\Users\ASUS\OneDrive\Рабочий стол\pp2\pp2\lab7\Asphalt8.mp3"
song2 = r"C:\Users\ASUS\OneDrive\Рабочий стол\pp2\pp2\lab7\Runaway.mp3"
song3 = r"C:\Users\ASUS\OneDrive\Рабочий стол\pp2\pp2\lab7\pokerface.mp3"

# List of music files
playlist = [song1, song2, song3]  # Замените названиями ваших песен

# Index of the current song
current_song_index = 0

# Function to load and play music
def play_music(file):
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()

# Function to pause music
def pause_music():
    pygame.mixer.music.pause()

# Function to unpause music
def unpause_music():
    pygame.mixer.music.unpause()

# Function to stop music
def stop_music():
    pygame.mixer.music.stop()

# Function to display text on the screen
def draw_text(text, x, y):
    font = pygame.font.Font(None, 36)
    text_surface = font.render(text, True, (255, 255, 255))
    screen.blit(text_surface, (x, y))

# Main loop
running = True
while running:
    screen.fill((0, 0, 0))

    # Get events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:  # Play/Pause music
                if pygame.mixer.music.get_busy():
                    if pygame.mixer.music.get_pos() > 0:
                        pause_music()
                    else:
                        unpause_music()
                else:
                    play_music(playlist[current_song_index])
            elif event.key == pygame.K_s:  # Stop music
                stop_music()
            elif event.key == pygame.K_RIGHT:  # Switch to next song
                current_song_index = (current_song_index + 1) % len(playlist)
                stop_music()
                play_music(playlist[current_song_index])
            elif event.key == pygame.K_LEFT:  # Switch to previous song
                current_song_index = (current_song_index - 1) % len(playlist)
                stop_music()
                play_music(playlist[current_song_index])
    #Draw image
    screen.blit(image, image_rect)
    #Display controls
    draw_text("Press 'P' to Play/Pause", 10, 10)
    draw_text("Press 'S' to Stop", 10, 50)
    draw_text("Press 'LEFT'/'RIGHT' to Change Song", 10, 90)

    pygame.display.flip()

pygame.quit()
