import pygame
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

class MusicPlayer:
    def __init__(self, master):
        self.master = master
        master.title("Music Player")

        # Create buttons
        self.play_button = ttk.Button(master, text="Play", command=self.play_music)
        self.pause_button = ttk.Button(master, text="Pause", command=self.pause_music)
        self.stop_button = ttk.Button(master, text="Stop", command=self.stop_music)
        self.open_button = ttk.Button(master, text="Open", command=self.open_music)

        # Position buttons
        self.play_button.grid(row=0, column=0, padx=5, pady=5)
        self.pause_button.grid(row=0, column=1, padx=5, pady=5)
        self.stop_button.grid(row=0, column=2, padx=5, pady=5)
        self.open_button.grid(row=0, column=3, padx=5, pady=5)

        # Initialize Pygame mixer
        pygame.mixer.init()

    def play_music(self):
        # Check if music is loaded and not playing
        if hasattr(self, 'music') and not pygame.mixer.music.get_busy():
            pygame.mixer.music.play()

    def pause_music(self):
        # Check if music is loaded and playing
        if hasattr(self, 'music') and pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()

    def stop_music(self):
        # Check if music is loaded and playing
        if hasattr(self, 'music') and pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()

    def open_music(self):
        # Show file dialog to select music file
        file_path = filedialog.askopenfilename(title="Select Music File", filetypes=[("Audio Files", "*.mp3;*.wav;*.ogg")])

        if file_path:
            # Load music file
            pygame.mixer.music.load(file_path)
            self.music = file_path

if __name__ == '__main__':
    root = tk.Tk()
    app = MusicPlayer(root)
    root.mainloop()
