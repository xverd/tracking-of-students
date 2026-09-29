# config.py
APP_TITLE = "Учёт посещаемости"
API_BASE_URL = "http://localhost:8000"

# Настройки окна
WINDOW_DEFAULT_WIDTH = 1440
WINDOW_DEFAULT_HEIGHT = 1024
WINDOW_MIN_WIDTH = 1000
WINDOW_MIN_HEIGHT = 700

# Цветовая тема
COLORS = {
    "bg": "#FFFFFF",
    "primary": "#8B5A2B",      # Коричневый (парты)
    "secondary": "#D3D3D3",    # Серый (кнопки/поля)
    "text": "#000000",
    "accent": "#4CAF50",       # Зеленый (присутствует)
    "danger": "#F44336",       # Красный (отсутствует)
}

FONT_MAIN = ("Segoe UI", 14)
FONT_HEADER = ("Segoe UI", 18, "bold")