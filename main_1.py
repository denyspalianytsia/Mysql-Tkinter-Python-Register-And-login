from multiprocessing import connection
import mysql.connector
import tkinter as tk
from tkinter import *
from tkinter import messagebox 
from tkinter import filedialog
root = Tk()
root.title("Base")
root.geometry("300x260")

con = mysql.connector.connect(host='localhost',
                                database='base',
                                user='denis',
                                password='denis',
                                auth_plugin='mysql_native_password')

cursor = con.cursor()

def registration():
    root.destroy()
    root1 = Tk()
    root1.title("Register")
    root1.geometry("300x260")

    text = Label(text="Для входа в систему зарегистрируйтесь")
    text_log = Label(text="Введите ваш логин")
    registr_login = Entry()
    text_password1 = Label(text="Введите ваш пароль")
    registr_password1 = Entry()
    text_password2 = Label(text="Введите ваш пароль еще раз")
    registr_password2 = Entry(show="*")
    button_registr = Button(text="Зарегистрироваться", command=save(registr_login, registr_password1, registr_password2))
    text.pack()
    text_log.pack()
    registr_login.pack()
    text_password1.pack()
    registr_password1.pack()
    text_password2.pack()
    registr_password2.pack()
    button_registr.pack()

    root1.mainloop()

def save(registr_login, registr_password1, registr_password2):

    if registr_login.get() != '' and registr_password1.get() != ''and registr_password2.get() != '':
        if registr_password1.get() == registr_password2.get():
            cursor.execute('INSERT INTO BASE (login, password) VALUES ("{}", "{}")'.format(registr_login.get(), registr_password1.get()))
        else:
            messagebox.showinfo('Information', 'Repeat the password')
    else:
        messagebox.showerror('Information', 'The line is empty') 

def login():
    root.destroy()
    root2 = Tk()
    root2.title("Log in")
    root2.geometry("300x260")

    text_log = Label(text="Поздравляем теперь ви можете войти в систему")
    text_enter_login = Label(text="Введите ваш логин ") 
    enter_login = Entry()
    text_enter_pass = Label(text="Введите ваш пароль")
    enter_password = Entry(show="*")
    button_enter = Button(text="Войти", command=lambda: exit(enter_login, enter_password))
    text_log.pack()
    text_enter_login.pack()
    enter_login.pack()
    text_enter_pass.pack()
    enter_password.pack()
    button_enter.pack()

    root2.mainloop()

def exit (enter_login, enter_password):
    login = enter_login.get()
    password = enter_password.get()
    y = cursor.execute("SELECT login,password FROM BASE WHERE login = %s AND password = %s ", (login,password)) 

    if cursor.fetchone():
        messagebox.showinfo('Information', 'You lig in')
    else:
        messagebox.showerror('Information', 'You not lig in')

def buttons():
    button_register = Button( text="Регистрация", command=lambda: registration())
    button_register.place(x=30, y=40, width=260, height=80)    
    button_login = Button( text="Войти в систему", command=lambda: login())
    button_login.place(x=30, y=140, width=260, height=80)
    
buttons()

root.mainloop()

cursor.close()