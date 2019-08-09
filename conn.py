from tkinter import *
import sqlite3
from sqlite3 import Error

def clean_errors(error_frame):
    # Cleans errors
    if len(error_frame.winfo_children()) > 0:
        error_frame.winfo_children()[0].destroy()


def register_user(conn, frame, error_frame, first_name, last_name, username, password, confirm_password, remember_me):
    # check fields completion
    is_completed = len(first_name) > 0 and len(last_name) > 0 and len(username) > 0 and len(password) > 0
    if password == confirm_password and is_completed:
        # connect db and create data
        user_info = (first_name, last_name, username, password, remember_me)
        create_user_table(conn)
        insert_user_info(conn, user_info)
        frame.destroy()


    elif not is_completed:
        clean_errors(error_frame)
        invalid_submission = Label(error_frame, text='Error: Please complete all fields')
        invalid_submission.pack()
    else:
        clean_errors(error_frame)
        invalid_password = Label(error_frame, text='Error: Passwords do not match')
        invalid_password.pack()


def login_user(conn, entry_frame, frame, error_frame, username, password):
    is_completed = len(username) > 0 and len(password) > 0
    if is_completed:

        user_log = search_user(conn, username, password)
        if user_log == None:
            clean_errors(error_frame)
            invalid_login = Label(error_frame, text='Error: incorrect user/pass')
            invalid_login.pack()

        else:
            error_frame.destroy()
            entry_frame.destroy()
            
            welcome_msg = Label(entry_frame, text='Welcome')
            conn.close()

    else:
        clean_errors(error_frame)
        missing = Label(error_frame, text='Error: Please complete all fields')
        missing.pack()


def search_user(conn, username, password):
    try:
        c = conn.cursor()
        c.execute('SELECT * FROM users WHERE username=? AND password=?', (username,password))
        print(c.fetchall())
        return c.fetchall()
    except Error as e:
        print(e)

    return None


def create_user_table(conn):
    try:
        c = conn.cursor()
        c.execute(sql_create_table_user)
    except Error as e:
        print(e)


def insert_user_info(conn, user_info):
    try:
        c = conn.cursor()
        c.execute("INSERT INTO users(firstname, lastname, username,password,rememberme) VALUES(?, ?, ?, ?, ?)", (user_info[0], user_info[1],user_info[2],user_info[3],user_info[4]))
        conn.commit()
    except Error as e:
        print(e)


sql_create_table_user = '''    
    CREATE TABLE IF NOT EXISTS users(
        firstname text NOT NULL,
        lastname text NOT NULL,
        username text NOT NULL,
        password text NOT NULL,
        rememberme integer
    );
'''
