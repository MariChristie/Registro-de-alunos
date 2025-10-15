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
                       date of birth Text NOT NULL,
                       address TEXT NOT NULL,
                       course text NOT NULL,
                       picture TEXT NOT NULL)''')
        
def register_student(self, student):
    self.c.execute("INSERT INTO students(name, email, tel, sex, date_of_birth, address, course, picture) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                   (student))
    self.conn.commit()

    #mostrando mensagem de sucesso
    messagebox.showinfo("Sucess", "Student registered successfully!")

    def view_all_students(self):
        self.c.execute("SELECT * FROM students")
        dados = self.fetchall()

        for i in dados:
            print(f'ID: {i[0]} | Name: {i[1]} | Email: {i[2]} | Tel: {i[3]} | Sex: {i[4]} | Date of Birth: {i[5]} | Address: {i[6]} | Course: {i[7]} | Picture: {i[8]}')
        return dados
        