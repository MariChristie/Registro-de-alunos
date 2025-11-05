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
    #messagebox.showinfo("Sucess", "Student registered successfully!")

    def view_all_students(self):
        self.c.execute("SELECT * FROM students")
        dados = self.c.fetchall()
        
        return dados
        
    def search_student(self, id):
        self.c.execute("SELECT * FROM students WHERE id=?", (id,))
        dados = self.c.fetchall()

        return dados

    def update_student(self, nova_valores):
        query = "UPDATE students SET name=?, email=?, tel=?, sex=?, date_of_birth=?, address=?, course=?, picture=? WHERE id=?"
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

#studant = ("Joao", "email", '123456', 'M', '01/01/2000', 'Address', 'Course', 'picture.jpg') 
#sistema_de_registro.register_student(studant)

#see studants
#all_students = sistema_de_registro.view_all_students()

#procurar aluno
# aluno = sistema_de_registro.search_student(3)

#atualizar aluno
#studant = ("Joao", "email", '555', 'M', '01/01/2000', 'Address', 'Course', 'picture.jpg', 1) 
#studant = sistema_de_registro.update_student(studant)

# sistema_de_registro.delete_student(1)
# all_students = sistema_de_registro.view_all_students()