# ui/attendance_list.py
import customtkinter as ctk
from config import COLORS, FONT_MAIN


class AttendanceListWidget(ctk.CTkScrollableFrame):
    """Заглушка для списка студентов (Журнал)."""
    
    def __init__(self, parent, **kwargs):
        if 'fg_color' not in kwargs:
            kwargs['fg_color'] = COLORS["bg"]
        super().__init__(parent, **kwargs)
        
        # Временная надпись по центру
        placeholder = ctk.CTkLabel(
            self,
            text="Здесь будет список студентов (Frame 3-5)\n\nДанные пока не загружены.",
            font=(*FONT_MAIN[0], 20),
            text_color="#999999",
            justify="center"
        )
        placeholder.pack(expand=True, pady=100)