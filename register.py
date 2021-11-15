from tkinter import *
import mysql.connector
from tkinter import messagebox


mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="se_cms")
mycursor=mysqldb.cursor()


#Function to create an entry box with given fields and on given screen
def create_entry(screen_name, text_field, width_field, height_field, font_name, font_size, variable_name, entry_width):
    Label(screen_name, text=text_field, width=width_field,
          height=height_field, font=(font_name, font_size)).pack()
    field_name_entry = Entry(
        screen_name, textvariable=variable_name, width=entry_width)
    field_name_entry.pack()
    Label(screen_name, text='').pack()
    return field_name_entry

def validate_email(email_addr):
    if '@coep.ac.in' in email_addr:
        return True
    else:
        return False

def validate_mobileno(mobile_no):
    if len(mobile_no) == 10:
        return True
    else:
        return False

def validate_dob(dob):
    if len(dob) == 10:
        if (int(dob[6:]) <= 2003):
            print(int(dob[6:]))
            return True
        else:
            return False
    else:
        return False

def validate_misno(misno):
    if len(misno) == 9:
        return True
    else:
        return False

def popup_msg():
    mis_flag = False
    mobile_flag = False
    email_flag = False
    dob_flag = False
    student_name_info = student_name.get()
    student_misno_info = student_misno.get()
    student_mobileno_info = student_mobileno.get()
    student_emailaddr_info = student_emailaddr.get()
    student_year_info = student_year.get()
    student_branch_info = student_branch.get()
    student_dob_info = student_dob.get()

    #Validate mis no.
    if (validate_misno(student_misno_info) == False):
        messagebox.showerror('Invalid MIS Number',
                             'Please enter a valid MIS No. e.g. 111903010')
        return
    else:
        mis_flag = True

    #Validate mobile number
    if (validate_mobileno(student_mobileno_info) == False):
        messagebox.showerror('Invalid Mobile Number',
                             'Please enter a valid Mobile Number e.g. 9420456891')
        return
    else:
        mobile_flag = True

    #Valid email address
    if (validate_email(student_emailaddr_info) == False):
        messagebox.showwarning('Invalid Email Address',
                             'Please enter a valid college email address e.g. deshpandeav19.comp@coep.ac.in')
        return
    else:
        email_flag = True
        
    #Validate DOB
    if (validate_dob(student_dob_info) == False):
        messagebox.showerror('Invalid Date of Birth',
                             'Please enter correct date of birth details. If they are still correct, you are below 18 years of age, hence not eligible to join the college.')
        return
    else:
        dob_flag = True

    if (mobile_flag and email_flag and dob_flag and mis_flag):
        student_register_util()

#Function to store student details in a file
def student_register_util():
    student_name_info = student_name.get()
    student_misno_info = student_misno.get()
    student_mobileno_info = student_mobileno.get()
    student_emailaddr_info = student_emailaddr.get()
    student_year_info = student_year.get()
    student_branch_info = student_branch.get()
    student_dob_info = student_dob.get()
    
    #popup()
    # fs = open('student_info.txt', 'a')
    # fs.write(student_fields[0] + ' - ' + student_name_info + '\n')
    # fs.write(student_fields[1] + ' - ' + student_misno_info + '\n')
    # fs.write(student_fields[2] + ' - ' + student_mobileno_info + '\n')
    # fs.write(student_fields[3] + ' - ' + student_emailaddr_info + '\n')
    # fs.write(student_fields[4] + ' - ' + student_year_info + '\n')
    # fs.write(student_fields[5] + ' - ' + student_branch_info + '\n')
    # fs.write(student_fields[6] + ' - ' + student_dob_info + '\n')
    # fs.write(student_fields[7] + ' - ' + student_aadharno_info + '\n')
    # fs.write('\n')
    Label(student_register_screen, text='').pack()
    Label(student_register_screen, text="Student Registration Successful!", width='300',
          height='2', font=('Times New Roman', 20), fg='green').pack()
    try:
        #student dob is doubtful
        #sql = "INSERT INTO  student (stud_misno, stud_name, stud_mobileno, stud_year) VALUES (%s, %s, %s, %s)"
        sql = "INSERT INTO student_register (student_name, student_misno, student_mobileno, student_emailaddr, student_year, student_branch, student_dob) VALUES(%s, %s, %s, %s, %s, %s, %s)"
        val = (student_name_info, student_misno_info, student_mobileno_info, student_emailaddr_info, student_year_info, student_branch_info, student_dob_info)
        mycursor.execute(sql, val)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        print("Student data saved successfully")
        # messagebox.showinfo("information", "Student Record Saved Successfully")
    #    e1.delete(0, END)
    #    e2.delete(0, END)
    #    e3.delete(0, END)
    #    e4.delete(0, END)
    #    e1.focus_set()
    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()
#Function for student registration form
def student_register():
    # 'Admission Date' 'Secondary Email Address' remains doubtful to add or not
    global student_fields 
    student_fields = ['Full Name', 'MIS Number', 'Mobile Number', 'Email Address', 'Year of Study', 'Branch', 'Date of Birth(DD-MM-YYYY)']
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
    # student_name, student_misno, student_mobileno, student_emailaddr, student_year, student_branch, student_dob, student_aadharno = StringVar()
    student_name = StringVar()
    student_misno = StringVar()
    student_mobileno = StringVar()
    student_emailaddr = StringVar()
    student_year = StringVar()
    student_branch = StringVar()
    student_dob = StringVar()
    #Label
    Label(student_register_screen, text='Please Enter Details below', width='300',
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
    #Submit button
    Button(student_register_screen, text='Submit', height='2', width='10', bg='green',
           font=('Times New Roman', 14), command=popup_msg).pack()

#Stores faculty details
def faculty_register_util():
    fac_name_info = fac_name.get()
    fac_mobileno_info = fac_mobileno.get()
    fac_aadharno_info = fac_aadharno.get()
    fac_dept_info = fac_dept.get()
    fs = open('faculty_info.txt', 'a')
    fs.write(fac_fields[0] + ' - ' + fac_name_info + '\n')
    fs.write(fac_fields[1] + ' - ' + fac_mobileno_info + '\n')
    fs.write(fac_fields[2] + ' - ' + fac_emailaddr_info + '\n')
    fs.write(fac_fields[3] + ' - ' + fac_dept_info + '\n')
    Label(screen_name, text='').pack()
    Label(fac_register_screen, text="Faculty Registration Successful!", width='300',
          height='2', font=('Times New Roman', 20), fg='green').pack()
    
def faculty_register():
    global fac_fields 
    fac_fields = ['Full Name','Mobile Number','Aadhar Number', 'Department']
    global fac_register_screen
    fac_register_screen = Toplevel(screen)
    fac_register_screen.title('Faculty Registration Form')
    fac_register_screen.geometry('800x1200')
    fac_register_screen.state('zoomed')
    global fac_name
    global fac_mobileno
    global fac_aadharno
    global fac_dept
    fac_name = StringVar()
    fac_aadharno = StringVar()
    fac_mobileno = StringVar()
    fac_dept = StringVar()
    #Label
    Label(fac_register_screen, text='Please Enter Details below', width='300',
          height='2', bg='grey', font=('Times New Roman', 15)).pack()
    Label(fac_register_screen, text='').pack()
    #Faculty name
    fac_name_entry = create_entry(fac_register_screen, fac_fields[0] + ' *', '300', '2', 'Times New Roman', 12, fac_name, 100)
    print(fac_name)
    #Faculty mobile
    fac_mobile_entry = create_entry(fac_register_screen, fac_fields[1] + ' *', '300', '2', 'Times New Roman', 12, fac_mobileno, 100)
    print(fac_mobileno)
    #Faculty aadhar
    fac_aadhar_entry = create_entry(
        fac_register_screen, fac_fields[2] + ' *', '300', '2', 'Times New Roman', 12, fac_aadharno, 100)
    print(fac_aadharno)
    #Faculty Department
    fac_dept_entry = create_entry(
        fac_register_screen, fac_fields[3] + ' *', '300', '2', 'Times New Roman', 12, fac_dept, 100)
    Button(fac_register_screen, text='Submit', height='2', width='10', bg='green',
           font=('Times New Roman', 14), command=faculty_register_util).pack()



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
