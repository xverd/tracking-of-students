import customtkinter as ctk
from config import APP_TITLE, COLORS, WINDOW_DEFAULT_WIDTH, WINDOW_DEFAULT_HEIGHT, WINDOW_MIN_WIDTH, WINDOW_MIN_HEIGHT
from ui.login_screen import LoginScreen
from ui.dashboard import Dashboard


class TeacherApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title(APP_TITLE)
        self.geometry(f"{WINDOW_DEFAULT_WIDTH}x{WINDOW_DEFAULT_HEIGHT}")
        self.minsize(WINDOW_MIN_WIDTH, WINDOW_MIN_HEIGHT)
        
        self.current_user = None
        self.current_frame = None
        
        self.bind("<Configure>", self._on_window_resize)
        
        self.show_login()

    def _on_window_resize(self, event):
        pass

    def show_login(self):
        if self.current_frame:
            self.current_frame.destroy()
        self.current_frame = LoginScreen(self, on_login_success=self.on_login_success)
        self.current_frame.pack(fill="both", expand=True)

    def show_dashboard(self):
        if self.current_frame:
            self.current_frame.destroy()
        self.current_frame = Dashboard(self, user=self.current_user)
        self.current_frame.pack(fill="both", expand=True)

    def on_login_success(self, username: str):
        self.current_user = username
        self.show_dashboard()