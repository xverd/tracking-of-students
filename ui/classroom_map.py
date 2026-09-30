# ui/classroom_map.py
import customtkinter as ctk
from config import COLORS, FONT_MAIN


class ClassroomMapWidget(ctk.CTkScrollableFrame):
    """Визуальная схема класса: коричневые парты, 2 места, статусы."""

    def __init__(self, parent, **kwargs):
        # Устанавливаем белый фон по умолчанию, если не передан другой
        if 'fg_color' not in kwargs:
            kwargs['fg_color'] = COLORS["bg"]
            
        super().__init__(parent, **kwargs)
        
        # Параметры рассадки
        self.total_rows = 5      
        self.desks_per_row = 3   
        
        self._build_layout()

    def _build_layout(self):
        """Создает сетку: Парты слева, Подписи рядов справа."""
        
        for row_idx in range(1, self.total_rows + 1):
            # Контейнер для парт ряда
            desks_frame = ctk.CTkFrame(self, fg_color="transparent")
            desks_frame.grid(row=row_idx, column=0, padx=(20, 10), pady=15, sticky="w")
            
            for desk_idx in range(1, self.desks_per_row + 1):
                desk_widget = self._create_desk(row_idx, desk_idx)
                desk_widget.pack(side="left", padx=15)

            # Подпись ряда
            row_label = ctk.CTkLabel(
                self, 
                text=f"{row_idx} ряд", 
                font=(*FONT_MAIN[0], 16, "bold"),
                text_color=COLORS["text"],
                width=60,
                anchor="w"
            )
            row_label.grid(row=row_idx, column=1, padx=(10, 40), pady=15, sticky="e")

    def _create_desk(self, row: int, col: int) -> ctk.CTkFrame:
        """Рисует пустую парту (коричневый прямоугольник)."""
        
        # Коричневая основа парты
        desk = ctk.CTkFrame(self, fg_color="#8B5A2B", width=140, height=70)
        desk.pack_propagate(False) 
        
        # Пока не добавляем сюда индикаторы статусов (черные/белые квадраты),
        # так как ты просил "пустые места".
        # Позже мы добавим метод update_desk_status(row, col, status), 
        # который будет динамически добавлять эти квадраты.
        
        # Добавим легкую рамку или эффект при наведении, чтобы было видно, что это интерактивный элемент
        desk.bind("<Enter>", lambda e, d=desk: d.configure(fg_color="#9C6B3C"))
        desk.bind("<Leave>", lambda e, d=desk: d.configure(fg_color="#8B5A2B"))
        
        return desk

    def _create_seat_indicator(self, parent, is_present: bool) -> ctk.CTkFrame:
        """Рисует маленький квадратик статуса (Черный=Присутствует, Белый=Отсутствует)."""
        color = "#000000" if is_present else "#FFFFFF"
        border = "#333333" if not is_present else "#000000"

        indicator = ctk.CTkFrame(
            parent,
            fg_color=color,
            border_color=border,
            border_width=2,
            width=24,
            height=24,
        )
        return indicator

    def _get_mock_status(self, row: int, col: int, seat_num: int) -> bool:
        """Генерирует случайный статус для демо (True = присутствует)."""
        # Простая логика для разнообразия цветов
        val = (row * 10 + col * 3 + seat_num) % 4
        return val != 0  # 75% присутствуют, 25% отсутствуют
