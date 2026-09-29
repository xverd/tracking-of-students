import customtkinter as ctk
from config import COLORS, FONT_MAIN, FONT_HEADER


class LoginScreen(ctk.CTkFrame):
    def __init__(self, parent, on_login_success):
        super().__init__(parent, fg_color=COLORS["bg"])
        self.on_login_success = on_login_success
        
        container = ctk.CTkFrame(self, fg_color=COLORS["bg"], width=400, height=300)
        container.place(relx=0.5, rely=0.5, anchor="center")
        
        title = ctk.CTkLabel(
            container, 
            text="Вход для преподавателя", 
            font=FONT_HEADER,
            text_color=COLORS["text"]
        )
        title.pack(pady=(0, 20))
        
        self.login_entry = ctk.CTkEntry(
            container, 
            placeholder_text="Логин", 
            font=FONT_MAIN,
            height=40,
            border_color=COLORS["secondary"]
        )
        self.login_entry.pack(pady=5, fill="x")
        
        self.password_entry = ctk.CTkEntry(
            container, 
            placeholder_text="Пароль", 
            show="*", 
            font=FONT_MAIN,
            height=40,
            border_color=COLORS["secondary"]
        )
        self.password_entry.pack(pady=5, fill="x")
        
        btn = ctk.CTkButton(
            container, 
            text="Вход", 
            command=self.handle_login,
            height=45,
            fg_color=COLORS["primary"],
            hover_color="#6D4C2B",
            font=FONT_MAIN
        )
        btn.pack(pady=20, fill="x")
        
        self.error_label = ctk.CTkLabel(
            container, 
            text="", 
            text_color=COLORS["danger"],
            font=FONT_MAIN
        )
        self.error_label.pack()

    def handle_login(self):
        login = self.login_entry.get().strip()
        password = self.password_entry.get().strip()
        
        if not login or not password:
            self.error_label.configure(text="Заполните все поля!")
            return
            
        self.on_login_success(login)