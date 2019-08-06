from tkinter import *
import sqlite3

def clean_errors(error_frame):
    if len(error_frame.winfo_children()) > 0:
        error_frame.winfo_children()[0].destroy()

def register_user(frame, error_frame, first_name, last_name, username, password, confirm_password, remember_me):
    # check fields completion
    is_completed = len(first_name) > 0 and len(last_name) > 0 and len(username) > 0 and len(password) > 0
    if password == confirm_password and is_completed:
        # connect db and create data
        conn = connect_db()
        user_info = (first_name, last_name, username, password, remember_me)
        create_user_table(conn)
        insert_user_info(conn, user_info)
        error_frame.destroy()
        frame.destroy()
        conn.close()

    elif not is_completed:
        clean_errors(error_frame)
        invalid_submission = Label(error_frame, text='Error: Please complete all fields')
        invalid_submission.pack()
    else:
        clean_errors(error_frame)
        invalid_password = Label(error_frame, text='Error: Passwords do not match')
        invalid_password.pack()

def login_user(entry_frame, frame, error_frame, username, password):
    is_completed = len(username) > 0 and len(password) > 0
    if is_completed:
        conn = connect_db()
        user_log = search_user(conn, username, password)
        if user_log is None:
            clean_errors(error_frame)
            invalid_login = Label(error_frame, text='Error: Username or Password is incorrect')
            invalid_login.pack()

        else:
            frame.destroy()
            error_frame.destroy()
            print(user_log)
            welcome_msg = Label(entry_frame, text='Welcome')

        conn.close()
    else:
        clean_errors(error_frame)
        missing = Label(error_frame, text='Error: Please complete all fields')
        missing.pack()

def search_user(conn, username, password):
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
    user_log = c.fetchone()
    if user_log is None:
        return None
    return user_log


def connect_db():
    try:
        conn = sqlite3.connect('clients.db')
        return conn
    except Exception as e:
        print(e)

    return None


def create_user_table(conn):
    try:
        c = conn.cursor()
        c.execute(sql_create_table_user)
    except Exception as e:
        print(e)


def insert_user_info(conn, user_info):
    try:
        c = conn.cursor()
        c.execute('INSERT INTO users(firstName,lastName,username,password,rememberMe)VALUES(?,?,?,?,?)', user_info)
    except Exception as e:
        print(e)


sql_create_table_user = '''    
    CREATE TABLE IF NOT EXISTS users(
        firstName text,
        lastName text ,
        username text,
        password text,
        rememberMe boolean
    )
'''
