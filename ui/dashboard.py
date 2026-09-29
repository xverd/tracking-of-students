import customtkinter as ctk
from config import COLORS, FONT_MAIN, FONT_HEADER


class Dashboard(ctk.CTkFrame):
    def __init__(self, parent, user: str):
        super().__init__(parent, fg_color=COLORS["bg"])
        self.user = user
        
        header = ctk.CTkFrame(self, fg_color=COLORS["bg"], height=80)
        header.pack(fill="x", padx=20, pady=(20, 0))
        
        welcome = ctk.CTkLabel(
            header, 
            text=f"Здравствуйте, {user}", 
            font=FONT_HEADER,
            anchor="w"
        )
        welcome.pack(side="left", padx=10, pady=10)
        
        exit_btn = ctk.CTkButton(
            header, 
            text="Выйти", 
            width=100,
            height=35,
            fg_color=COLORS["secondary"],
            text_color=COLORS["text"],
            command=lambda: parent.show_login()
        )
        exit_btn.pack(side="right", padx=10, pady=10)
        
        info_frame = ctk.CTkFrame(self, fg_color=COLORS["bg"])
        info_frame.pack(fill="x", padx=20, pady=20)
        
        for label_text in ["Предмет: наименование", "Урок: номер урока", "Класс: 6А"]:
            lbl = ctk.CTkLabel(
                info_frame, 
                text=label_text, 
                font=FONT_MAIN,
                anchor="w"
            )
            lbl.pack(fill="x", pady=2)
            
        absent_label = ctk.CTkLabel(
            info_frame, 
            text="(0) Учеников отсутствует", 
            font=FONT_MAIN,
            text_color=COLORS["danger"],
            anchor="w"
        )
        absent_label.pack(fill="x", pady=(10, 0))
        
        actions_frame = ctk.CTkFrame(self, fg_color=COLORS["bg"])
        actions_frame.pack(fill="x", padx=20, pady=20, side="bottom")
        
        diary_btn = ctk.CTkButton(
            actions_frame, 
            text="Распечатать дневник", 
            height=50,
            fg_color=COLORS["secondary"],
            text_color=COLORS["text"],
            font=FONT_MAIN
        )
        diary_btn.pack(side="left", expand=True, fill="x", padx=(0, 10))
        
        attendance_btn = ctk.CTkButton(
            actions_frame, 
            text="Открыть класс посещаемости", 
            height=50,
            fg_color=COLORS["primary"],
            hover_color="#6D4C2B",
            font=FONT_MAIN
        )
        attendance_btn.pack(side="right", expand=True, fill="x", padx=(10, 0))