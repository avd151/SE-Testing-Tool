#Referred-https://www.geeksforgeeks.org/dropdown-menus-tkinter/
def faculty_register():
    global fac_fields 
    fac_fields = ['Full Name','Mobile Number','Aadhar Number', 'Department']
    options = ["Computer", "Electrical", "Electronics", "Mechanical", "Metallurgy", "Instrumentation", "Civil", "Planning", "Production"]
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
    fac_dept.set("Computer") #default value
    drop = OptionMenu(fac_register_screen ,fac_dept , *options )
    drop.place(x=850,y=320)
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
    button = Button(fac_register_screen , text = "Select Department" , command ="").pack()
    label = Label(fac_register_screen , text = " " )
    label.pack()
    fac_dept_entry = create_entry(
        fac_register_screen, fac_fields[3] + ' *', '300', '2', 'Times New Roman', 12, fac_dept, 100)
    Button(fac_register_screen, text='Submit', height='2', width='10', bg='green',
           font=('Times New Roman', 14), command=faculty_register_util).pack()
