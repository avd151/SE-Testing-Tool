from tkinter import *



def register_user():
    username_info = username.get()
    password_info = password.get()
    # print(username_info)
    # print(password_info)
    file = open('user.txt', "a")
    file.write(username_info + "\n")
    file.write(password_info)
    file.write("\n")
    file.close()
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    Label(register_screen, text="Registration Successful!", width='300',
          height='2', font=('Times New Roman', 20), fg='green').pack()

def register():
    global username
    global password
    global username_entry
    global password_entry
    global register_screen
    register_screen = Toplevel(screen)
    register_screen.title('Register')
    register_screen.geometry('800x500')
    username = StringVar()
    password = StringVar()

    Label(register_screen, text='Please enter details below to Register', width='300',
          height='2', font=('Times New Roman', 20)).pack()
    Label(register_screen, text='').pack()

    Label(register_screen, text='Username *', width='300',
          height='2', font=('Times New Roman', 20)).pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    Label(register_screen, text='').pack()

    Label(register_screen, text='Password *', width='300',
          height='2', font=('Times New Roman', 20)).pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text='').pack()

    Button(register_screen, text='Register', height='2', width='10', bg='grey',
           font=('Times New Roman', 15), command=register_user).pack()

def student_register():
    pass

def faculty_register():
    pass

'''
Not to be used for now...

def login_verify():
    # print('working')
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)


def login():
    global username_verify
    global password_verify
    global username_login_entry
    global password_login_entry
    login_screen = Toplevel(screen)
    login_screen.title("Login")
    login_screen.geometry("800x500")
    Label(login_screen, text='Please enter details below to Login', width='300',
          height='2', font=('Times New Roman', 20)).pack()
    Label(login_screen, text="").pack()

    username_verify = StringVar()
    password_verify = StringVar()

    Label(login_screen, text='Username *', width='300',
          height='2', font=('Times New Roman', 20)).pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()

    Label(login_screen, text='Password *', width='300',
          height='2', font=('Times New Roman', 20)).pack()
    password__login_entry = Entry(
        login_screen, textvariable=password_verify, show='*')
    password__login_entry.pack()
    Label(login_screen, text="").pack()

    Button(login_screen, text='Login', height='2', width='10', bg='grey',
           font=('Times New Roman', 15), command=login_verify).pack()

'''



def main_screen():
    global screen
    screen = Tk()
    screen.geometry('800x500')
    screen.title('College Management System 1.0')
    Label(text='College Management System - to Store Student and Faculty Details', bg='grey', width='300', height='2', font=('Times New Roman', 20)).pack()
    Label(text='').pack()
    Button(text='Register as Student', height='2', width='10', bg='white', font=('Times New Roman', 15), command=student_register).pack()
    Label(text='').pack()
    Button(text='Register as Faculty', height='2', width='10', bg='white', font=('Times New Roman', 15), command=faculty_register).pack()

    screen.mainloop()

main_screen()
