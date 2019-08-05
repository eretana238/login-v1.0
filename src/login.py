from tkinter import *
import conn


class register(Toplevel):
    def __init__(self, *args, **kwargs):
        Toplevel.__init__(self, *args, **kwargs)
        pos = 0.1
        remember_me_val = IntVar()
        self.grab_set()
        self.geometry('300x300')
        self.title('register')
        frame = Frame(self)
        frame.place(rely=pos, relx=.3)

        label_first_name = Label(frame, text='First Name')
        label_first_name.pack()

        first_name = Entry(frame)
        first_name.pack()

        label_last_name = Label(frame, text='Last Name')
        label_last_name.pack()

        last_name = Entry(frame)
        last_name.pack()

        label_user = Label(frame, text='Create Username')
        label_user.pack()

        username = Entry(frame)
        username.pack()

        label_pass = Label(frame, text='Create Password')
        label_pass.pack()

        password = Entry(frame, show='*')
        password.pack()

        label_confirm_pass = Label(frame, text='Confirm Password')
        label_confirm_pass.pack()

        confirm_password = Entry(frame, show='*')
        confirm_password.pack()

        remember_me = Checkbutton(frame, text='remember me', variable=remember_me_val)
        remember_me.pack()

        submit = Button(frame, text='Submit',
                        command=conn.register_user(frame, first_name.get(), last_name.get(), username.get(),
                                                   password.get(), confirm_password.get(), remember_me_val.get()))
        submit.pack()


class login(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.title('Database system')

        windowWidth = 200
        windowHeight = 200

        horizontal_pos = int(main.winfo_screenwidth() / 2 - windowWidth / 2)
        vertical_pos = int(main.winfo_screenheight() / 2 - windowHeight / 2)

        self.master.geometry('+{}+{}'.format(horizontal_pos, vertical_pos))
        self.master.resizable(width=False, height=False)

        frame = Frame(self.master)
        frame.place(rely=.2, relx=.2)

        label_user = Label(frame, text='Username:')
        label_user.pack()

        username = Entry(frame, bd=1, textvariable=StringVar())
        username.pack()

        label_pass = Label(frame, text='Password:')
        label_pass.pack()

        password = Entry(frame, show='*', bd=1, textvariable=StringVar())
        password.pack()

        login = Button(frame, text='Login', bd=1, command=conn.login_user(frame, username.get(), password.get()))
        # add login command
        login.pack()

        reg = Button(frame, text='Register', bd=0, fg='PURPLE', command=register)
        reg.pack()


if __name__ == "__main__":
    main = Tk()
    login_screen = login(main)
    main.mainloop()
