# ui/app.py
import customtkinter as ctk
from config import APP_TITLE, COLORS, WINDOW_DEFAULT_WIDTH, WINDOW_DEFAULT_HEIGHT, WINDOW_MIN_WIDTH, WINDOW_MIN_HEIGHT
from ui.login_screen import LoginScreen
from ui.dashboard import Dashboard


class TeacherApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Базовые настройки окна
        self.title(APP_TITLE)
        self.geometry(f"{WINDOW_DEFAULT_WIDTH}x{WINDOW_DEFAULT_HEIGHT}")
        self.minsize(WINDOW_MIN_WIDTH, WINDOW_MIN_HEIGHT)
        
        # Хранилище состояния
        self.current_user = None
        
        # Создаем оба экрана ОДИН РАЗ при запуске
        self.login_screen = LoginScreen(self, on_login_success=self.on_login_success)
        self.dashboard_screen = Dashboard(self, user="") # user обновится позже
        
        # По умолчанию показываем вход, дашборд скрыт
        self.login_screen.pack(fill="both", expand=True)
        self.dashboard_screen.pack_forget() 

    def show_login(self):
        """Переключает на экран авторизации."""
        self.dashboard_screen.pack_forget() # Скрываем дашборд
        self.login_screen.pack(fill="both", expand=True) # Показываем вход
        
        # Очищаем поля ввода для безопасности
        self.login_screen.login_entry.delete(0, "end")
        self.login_screen.password_entry.delete(0, "end")
        self.login_screen.error_label.configure(text="")

    def show_dashboard(self):
        """Переключает на главный экран после успешного входа."""
        self.login_screen.pack_forget() # Скрываем вход
        self.dashboard_screen.pack(fill="both", expand=True) # Показываем дашборд
        
        # Обновляем данные пользователя в дашборде
        self.dashboard_screen.update_user(self.current_user)

    def on_login_success(self, username: str):
        """Коллбек при успешной авторизации."""
        self.current_user = username
        self.show_dashboard()