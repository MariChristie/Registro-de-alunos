import sqlite3
from tkinter import messagebox

class SistemadeRegistro:
    def __init__(self):
        self.conn = sqlite3.connect('study.db')
        self.c = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS students (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       name TEXT NOT NULL, 
                       Email TEXT NOT NULL,
                       tel TEXT NOT NULL,
                       sex TEXT NOT NULL,
                       date_of_birth Text NOT NULL,
                       address TEXT NOT NULL,
                       course text NOT NULL,
                       picture TEXT NOT NULL)''')
        
    def register_student(self, student):
        self.c.execute("INSERT INTO students(name, email, tel, sex, date_of_birth, address, course, picture) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                    student)
        self.conn.commit()

    #mostrando mensagem de sucesso
    messagebox.showinfo("Sucess", "Student registered successfully!")

    def view_all_students(self):
        self.c.execute("SELECT * FROM students")
        dados = self.c.fetchall()

        for i in dados:
            print(f'ID: {i[0]} | Name: {i[1]} | Email: {i[2]} | Tel: {i[3]} | Sex: {i[4]} | Date of Birth: {i[5]} | Address: {i[6]} | Course: {i[7]} | Picture: {i[8]}')
        
    def search_student(self, id):
        self.c.execute("SELECT * FROM students WHERE id=?", (id,))
        dados = self.c.fetchall()

        print(f'ID: {dados[0]} | Name: {dados[1]} | Email: {dados[2]} | Tel: {dados[3]} | Sex: {dados[4]} | Date of Birth: {dados[5]} | Address: {dados[6]} | Course: {dados[7]} | Picture: {dados[8]}')

    def update_student(self, nova_valores):
        query = "UPDATE students SET name=?, email=?, tel=?, sex=?, data_of_birth=?, address=?, course=?, picture=? WHERE id=?"
        self.c.execute(query, nova_valores)
        self.conn.commit()

        #mostrando mensagem de sucesso
        messagebox.showinfo("Sucess", f"Student with ID {nova_valores[8]} updated successfully!")
    
    def delete_student(self, id):
        self.c.execute("DELETE FROM students WHERE id=?", (id,))
        self.conn.commit()

        #mostrando mensagem de sucesso
        messagebox.showinfo("Sucess", f"Student with ID{id} deleted successfully!")


# Criando uma instância do sistema de registro
sistema_de_registro = SistemadeRegistro()

# information
# studant = ("Joao", "email", '123456', 'M', '01/01/2000', 'Address', 'Course', 'picture.jpg')
# sistema_de_registro.register_student(studant)