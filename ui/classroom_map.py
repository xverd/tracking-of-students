import customtkinter as ctk
from config import COLORS, FONT_MAIN

class ClassroomMapWidget(ctk.CTkScrollableFrame):

    def __init__(self, parent):
        super().__init__(parent, fg_color=COLORS["bg"])

        self.rows = 3
        self.seats_per_row = 4

        self.seat_buttons = {}

        self._render_headers()

        self._render_seats()

    def _render_headers(self):
        for i in range(1, self.rows + 1):
            label = ctk.CTkLabel(
                self, 
                text=f"{i} ряд", 
                font=FONT_MAIN,
                width=60,
                anchor="e"
            )
            label.grid(row=i, column=0, padx=(0, 10), pady=10, sticky="e")

    def _render_seats(self):
        for row in range(1, self.rows + 1):
            for col in range(1, self.seats_per_row + 1):
                seat_id = f"{row}-{col}"

                status = self._get_mock_status(row, col)
                color = self._get_seat_color(status)

                btn = ctk.CTkButton(
                    self,
                    text="",
                    width=80,
                    height=50,
                    fg_color=color,
                    hover_color=self._get_hover_color(color),
                    corner_radius=8,
                    command=lambda sid=seat_id: self._on_seat_click(sid)
                )
                btn.grid(row=row, column=col, padx=5, pady=10)
                self.seat_buttons[seat_id] = btn
    def _get_mock_status(self, row: int, col: int) -> str:
        if (row + col) % 3 == 0:
            return "absent"
        elif (row + col) % 5 == 0:
            return "pending"
        return "present"

    def _get_seat_color(self, status: str) -> str:
        colors = {
            "present": COLORS["accent"],   
            "absent": COLORS["danger"],    
            "pending": "#FFC107",         
            "free": COLORS["secondary"]  
        }
        return colors.get(status, COLORS["secondary"])

    def _get_haver_color(self, base_color: str) -> str:
        return base_color[:6] + "CC" if len(base_color) == 7 else base_color

    def _on_seat_click(self, seat_id: str):
        print(f"Клик по месту: {seat_id}")