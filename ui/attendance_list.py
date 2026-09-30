# ui/attendance_list.py
import customtkinter as ctk
from config import COLORS, FONT_MAIN
from database import StudentRepository


class AttendanceListWidget(ctk.CTkScrollableFrame):
    
    def __init__(self, parent, group_id: int = 1, **kwargs):
        super().__init__(parent, fg_color=COLORS["bg"])
        
        self.group_id = group_id
        self._load_and_render_students()

    def _load_and_render_students(self):
        try:
            students = StudentRepository.get_students_by_group(self.group_id)
            
            if not students:
                ctk.CTkLabel(
                    self, text="Студенты не найдены", 
                    font=(FONT_MAIN[0], 16), text_color="#999"
                ).pack(pady=50)
                return

            header_frame = ctk.CTkFrame(self, fg_color="transparent")
            header_frame.pack(fill="x", padx=20, pady=(10, 5))
            
            bold_font = (FONT_MAIN[0], 14, "bold")
            
            ctk.CTkLabel(header_frame, text="№", width=50, anchor="w", font=bold_font).pack(side="left")
            ctk.CTkLabel(header_frame, text="ФИО", width=300, anchor="w", font=bold_font).pack(side="left", padx=10)
            ctk.CTkLabel(header_frame, text="Место", width=100, anchor="e", font=bold_font).pack(side="right", padx=10)

            for idx, student in enumerate(students, start=1):
                self._draw_student_row(idx, student)
                
        except Exception as e:
            ctk.CTkLabel(
                self, text=f"Ошибка загрузки: {e}", 
                text_color=COLORS["danger"], font=FONT_MAIN
            ).pack(pady=50)

    def _draw_student_row(self, index: int, student: dict):
        """Рисует одну строку студента с фиксированными размерами."""
        row_frame = ctk.CTkFrame(self, fg_color="#F5F5F5", height=40)
        row_frame.pack(fill="x", padx=20, pady=2)
        row_frame.pack_propagate(False) 
        
        ctk.CTkLabel(row_frame, text=str(index), width=50, anchor="w", font=FONT_MAIN).pack(side="left")
        
        ctk.CTkLabel(row_frame, text=student["full_name"], width=300, anchor="w", font=FONT_MAIN).pack(side="left", padx=10)
        
        seat_text = f"{student['seat_row']}-{student['seat_col']}-{student['seat_side']}"
        ctk.CTkLabel(row_frame, text=seat_text, width=100, anchor="e", font=FONT_MAIN).pack(side="right", padx=10)