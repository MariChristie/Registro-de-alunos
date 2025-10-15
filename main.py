import sqlite3
from tkinter import messagebox

class SistemadeRegistro:
    def __init__(self):
        self.conn = sqlite3.connect('study.db')
        self.c = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS students 
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       name TEXT NOT NULL, 
                       Email TEXT NOT NULL,
                       tel TEXT NOT NULL,
                       sex TEXT NOT NULL,
                       ''')