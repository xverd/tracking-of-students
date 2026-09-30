import sqlite3
import os

DB_PATH = os.path.join("data", "attendance.db")

def get_connection():
    if not os.path.exists(DB_PATH):
        raise FileNotFoundError(f"База данных не найдена по пути: {DB_PATH}")
        
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

class StudentRepository:
    
    @staticmethod
    def get_students_by_group(group_id: int) -> list[dict]:
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT id, full_name, seat_row, seat_col, seat_side 
            FROM students 
            WHERE group_id = ? 
            ORDER BY seat_row, seat_col, seat_side
        """, (group_id,))
        
        rows = cursor.fetchall()
        conn.close()
        
        return [dict(row) for row in rows]