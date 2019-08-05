from tkinter import *
import sqlite3


def register_user(frame, first_name, last_name, username, password, confirm_password, remember_me):
    is_completed = len(first_name) > 0 and len(last_name) > 0 and len(username) > 0 and len(password) > 0
    print(is_completed)
    if password == confirm_password and is_completed:
        conn = create_db()
        user_info = (1, first_name, last_name, username, password, remember_me)
        create_user_table(conn)
        insert_user_info(conn, user_info)

        # c = conn.cursor()
        # c.execute('SELECT * FROM users')
        # users = c.fetchall()
        # for user in users:
        #     print(user)
        print('hello')

        conn.close()

    elif not is_completed:
        invalid_submission = Label(frame, text='Error: Please complete text fields')
    else:
        invalid_password = Label(frame, text='Error: Passwords do not match')

def login_user(frame, username, password):
    pass


def create_db():
    try:
        conn = sqlite3.connect(':memory:')
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
        c.execute('INSERT INTO users(id,firstName,lastName,username,password,rememberMe)VALUES(?,?,?,?,?,?)', user_info)
    except Exception as e:
        print(e)

sql_create_table_user = '''    
    CREATE TABLE IF NOT EXISTS users(
        id integer PRIMARY KEY,
        firstName text,
        lastName text ,
        username text,
        password text,
        rememberMe boolean
    )
'''
