import pygame
import tkinter as tk
from tkinter import filedialog

def play_audio():
    file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3;*.wav;*.ogg")])
    if file_path:
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()

def stop_audio():
    pygame.mixer.music.stop()
    pygame.quit()

# GUI
root = tk.Tk()
root.title("Audio Player")

play_button = tk.Button(root, text="Play", command=play_audio)
play_button.pack(pady=20)

stop_button = tk.Button(root, text="Stop", command=stop_audio)
stop_button.pack(pady=10)

root.mainloop()
