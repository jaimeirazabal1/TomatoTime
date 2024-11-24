import tkinter as tk
from tkinter import messagebox
import time
import threading
from playsound import playsound
# nombre_del_entorno\Scripts\activate


# Configuración inicial
class TomatoTimeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("TomatoTime 🍅")
        self.root.geometry("400x400")
        self.root.config(bg="#FF6347")

        # Variables
        self.running = False
        self.time_left = 25 * 60  # 25 minutos

        # Estilo visual
        self.create_ui()

    def create_ui(self):
        # Título
        self.title_label = tk.Label(self.root, text="TomatoTime 🍅", font=("Helvetica", 24, "bold"), bg="#FF6347", fg="#FFFFFF")
        self.title_label.pack(pady=20)

        # Temporizador
        self.timer_label = tk.Label(self.root, text=self.format_time(self.time_left), font=("Helvetica", 48), bg="#FF6347", fg="#FFFFFF")
        self.timer_label.pack(pady=20)

        # Botones
        self.start_button = tk.Button(self.root, text="Iniciar", font=("Helvetica", 14), bg="#FFFFFF", fg="#FF6347", command=self.start_timer)
        self.start_button.pack(side=tk.LEFT, padx=20, pady=20)

        self.pause_button = tk.Button(self.root, text="Pausar", font=("Helvetica", 14), bg="#FFFFFF", fg="#FF6347", command=self.pause_timer)
        self.pause_button.pack(side=tk.LEFT, padx=20, pady=20)

        self.reset_button = tk.Button(self.root, text="Reiniciar", font=("Helvetica", 14), bg="#FFFFFF", fg="#FF6347", command=self.reset_timer)
        self.reset_button.pack(side=tk.LEFT, padx=20, pady=20)

    def format_time(self, seconds):
        minutes = seconds // 60
        seconds = seconds % 60
        return f"{minutes:02d}:{seconds:02d}"

    def update_timer(self):
        while self.running and self.time_left > 0:
            time.sleep(1)
            self.time_left -= 1
            self.timer_label.config(text=self.format_time(self.time_left))
            self.root.update()

        if self.time_left == 0:
            self.running = False
            playsound("alarm.mp3")  # Reproduce un sonido de alarma
            messagebox.showinfo("TomatoTime 🍅", "¡Ciclo completado! Es hora de un descanso.")

    def start_timer(self):
        if not self.running:
            self.running = True
            threading.Thread(target=self.update_timer).start()

    def pause_timer(self):
        self.running = False

    def reset_timer(self):
        self.running = False
        self.time_left = 25 * 60
        self.timer_label.config(text=self.format_time(self.time_left))

# Crear la ventana principal
if __name__ == "__main__":
    root = tk.Tk()
    app = TomatoTimeApp(root)
    root.mainloop()