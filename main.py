# main.py
import customtkinter as ctk
from ui.app import TeacherApp

if __name__ == "__main__":
    # Установка глобальной темы
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")
    
    app = TeacherApp()
    app.mainloop()