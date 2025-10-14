import sqlite3
from tkinter import messagebox

class SistemadeRegistro:
    def __init__(self):
        self.conn = sqlite3.connect('study.db')