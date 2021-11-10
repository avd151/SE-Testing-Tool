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
           font=('Times New Roman', 12), command=register_user).pack()


def create_entry(screen_name, text_field, width_field, height_field, font_name, font_size, variable_name, entry_width):
    Label(screen_name, text=text_field, width=width_field,
          height=height_field, font=(font_name, font_size)).pack()
    field_name_entry = Entry(
        screen_name, textvariable=variable_name, width=entry_width)
    field_name_entry.pack()
    Label(screen_name, text='').pack()
    return field_name_entry


def student_register_util():
    student_name_info = student_name.get()
    student_misno_info = student_misno.get()
    student_mobileno_info = student_mobileno.get()
    student_emailaddr_info = student_emailaddr.get()
    student_year_info = student_year.get()
    student_branch_info = student_branch.get()
    student_dob_info = student_dob.get()
    student_aadharno_info = student_aadharno.get()
    fs = open('student_info.txt', 'a')
    fs.write(student_fields[0] + ' - ' + student_name_info + '\n')
    fs.write(student_fields[1] + ' - ' + student_misno_info + '\n')
    fs.write(student_fields[2] + ' - ' + student_mobileno_info + '\n')
    fs.write(student_fields[3] + ' - ' + student_emailaddr_info + '\n')
    fs.write(student_fields[4] + ' - ' + student_year_info + '\n')
    fs.write(student_fields[5] + ' - ' + student_branch_info + '\n')
    fs.write(student_fields[6] + ' - ' + student_dob_info + '\n')
    fs.write(student_fields[7] + ' - ' + student_aadharno_info + '\n')
    fs.write('\n')
    Label(screen_name, text='').pack()
    Label(student_register_screen, text="Student Registration Successful!", width='300',
          height='2', font=('Times New Roman', 20), fg='green').pack()

def student_register():
    # 'Admission Date' 'Secondary Email Address' remains doubtful to add
    global student_fields 
    student_fields = ['Full Name', 'MIS Number', 'Mobile Number', 'Email Address', 'Year of Study', 'Branch', 'Date of Birth', 'Aadhar Number']
    global student_register_screen
    student_register_screen = Toplevel(screen)
    student_register_screen.title('Student Registration Form')
    student_register_screen.geometry('800x1200')
    student_register_screen.state('zoomed')
    global student_name
    global student_misno
    global student_mobileno
    global student_emailaddr
    global student_year
    global student_branch
    global student_dob
    global student_aadharno
    # student_name, student_misno, student_mobileno, student_emailaddr, student_year, student_branch, student_dob, student_aadharno = StringVar()
    student_name = StringVar()
    student_misno = StringVar()
    student_mobileno = StringVar()
    student_emailaddr = StringVar()
    student_year = StringVar()
    student_branch = StringVar()
    student_dob = StringVar()
    student_aadharno = StringVar()
    #Label
    Label(student_register_screen, text='Please Enter Details below to Register as Student', width='300',
          height='2', bg='grey', font=('Times New Roman', 15)).pack()
    Label(student_register_screen, text='').pack()

    #Student full name
    student_name_entry = create_entry(student_register_screen, student_fields[0] + ' *', '300', '2', 'Times New Roman', 12, student_name, 100)
    print(student_name)
    # #Student mis no.
    mis_name_entry = create_entry(student_register_screen, student_fields[1] + ' *', '300', '2', 'Times New Roman', 12, student_misno, 100)
    print(student_misno)
    # #Student mobile no.
    student_mobileno_entry = create_entry(
        student_register_screen, student_fields[2] + ' *', '300', '2', 'Times New Roman', 12, student_mobileno, 100)
    print(student_mobileno)
    # #Student email address
    student_emailaddr_entry = create_entry(
        student_register_screen, student_fields[3] + ' *', '300', '2', 'Times New Roman', 12, student_emailaddr, 100)
    print(student_emailaddr)
    # #Student year of study
    student_year_entry = create_entry(
        student_register_screen, student_fields[4] + ' *', '300', '2', 'Times New Roman', 12, student_year, 100)
    print(student_year)
    # #Student branch
    student_branch_entry = create_entry(
        student_register_screen, student_fields[5] + ' *', '300', '2', 'Times New Roman', 12, student_branch, 100)
    print(student_branch)
    # #Student date of birth
    student_dob_entry = create_entry(
        student_register_screen, student_fields[6] + ' *', '300', '2', 'Times New Roman', 12, student_dob, 100)
    print(student_dob)
    # #Student aadhar no.
    student_aadharno_entry = create_entry(
        student_register_screen, student_fields[7] + ' *', '300', '2', 'Times New Roman', 12, student_aadharno, 100)
    print(student_aadharno)

    Button(student_register_screen, text='Submit', height='2', width='10', bg='green',
           font=('Times New Roman', 14), command=student_register_util).pack()

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
           font=('Times New Roman', 12), command=login_verify).pack()

'''



def main_screen():
    global screen
    screen = Tk()
    screen.geometry('800x500')
    screen.title('College Management System 1.0')
    Label(text='College Management System - to Store Student and Faculty Details', bg='grey', width='300', height='2', font=('Times New Roman', 15)).pack()
    Label(text='').pack()
    Button(text='Register as Student', height='2', width='50', bg='white', font=('Times New Roman', 12), command=student_register).pack()
    Label(text='').pack()
    Button(text='Register as Faculty', height='2', width='50', bg='white', font=('Times New Roman', 12), command=faculty_register).pack()
    screen.state('zoomed')
    screen.mainloop()

main_screen()
