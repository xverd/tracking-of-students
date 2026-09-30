# ui/classroom_window.py
import customtkinter as ctk
from ui.classroom_map import ClassroomMapWidget
from ui.attendance_list import AttendanceListWidget
from config import COLORS, FONT_HEADER


class ClassroomWindowManager:
    """Управляет единственным окном класса. Предотвращает дубли и зависания."""
    
    _instance = None  # Храним ссылку на созданное окно

    def __init__(self, parent_app):
        self.parent = parent_app
        self.current_mode = "map"
        
        # Если окно уже создавалось, просто показываем его
        if ClassroomWindowManager._instance and ClassroomWindowManager._instance.winfo_exists():
            self.window = ClassroomWindowManager._instance
            self.window.deiconify()  # Показываем скрытое окно
            self.window.lift()       # Выводим на передний план
            self._update_ui_texts()  # Обновляем тексты на случай смены режима
            return

        # Создаем окно впервые
        self.window = ctk.CTkToplevel(self.parent)
        self.window.title("Класс 6А - Посещаемость")
        self.window.geometry("1200x800")
        
        # Перехватываем закрытие крестиком -> просто прячем окно
        self.window.protocol("WM_DELETE_WINDOW", self.hide)
        
        # Сохраняем экземпляр
        ClassroomWindowManager._instance = self.window
        
        self._build_static_ui()
        self._update_content()

    def _build_static_ui(self):
        """Создает неизменяемые элементы интерфейса."""
        # Верхняя панель
        self.top_bar = ctk.CTkFrame(self.window, fg_color="transparent", height=60)
        self.top_bar.pack(fill="x", padx=20, pady=(20, 0))
        
        # Заголовок (будем менять текст)
        self.header_label = ctk.CTkLabel(
            self.top_bar, text="", font=FONT_HEADER, anchor="w"
        )
        self.header_label.pack(side="left")
        
        # Панель кнопок
        controls = ctk.CTkFrame(self.top_bar, fg_color="transparent")
        controls.pack(side="right")
        
        # Кнопка переключения (будем менять текст)
        self.toggle_btn = ctk.CTkButton(
            controls, text="", width=180, height=35,
            fg_color=COLORS["primary"], hover_color="#6D4C2B",
            command=self.toggle_mode
        )
        self.toggle_btn.pack(side="right", padx=(0, 10))
        
        # Кнопка закрытия (просто прячет окно)
        ctk.CTkButton(
            controls, text="Закрыть", width=100, height=35,
            fg_color=COLORS["secondary"], text_color=COLORS["text"],
            command=self.hide
        ).pack(side="right")
        
        # Контейнер для сменного контента
        self.content_container = ctk.CTkFrame(self.window, fg_color=COLORS["bg"])
        self.content_container.pack(fill="both", expand=True, padx=20, pady=20)

    def _update_ui_texts(self):
        """Обновляет надписи в зависимости от текущего режима."""
        if self.current_mode == "map":
            self.header_label.configure(text="Схема рассадки: 6А")
            self.toggle_btn.configure(text="Переключить на Журнал")
        else:
            self.header_label.configure(text="Журнал посещаемости: 6А")
            self.toggle_btn.configure(text="Переключить на Карту")

    def _update_content(self):
        """Безопасно меняет виджет внутри контейнера."""
        # Удаляем всё старое
        for widget in self.content_container.winfo_children():
            widget.destroy()
            
        # Добавляем новое
        if self.current_mode == "map":
            ClassroomMapWidget(self.content_container).pack(fill="both", expand=True)
        else:
            AttendanceListWidget(self.content_container).pack(fill="both", expand=True)

    def toggle_mode(self):
        """Переключает режим и обновляет интерфейс."""
        self.current_mode = "list" if self.current_mode == "map" else "map"
        self._update_ui_texts()
        self._update_content()

    def hide(self):
        """Прячет окно вместо уничтожения."""
        if self.window.winfo_exists():
            self.window.withdraw()