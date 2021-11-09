from tkinter import * 

print("\t\t\t\t STUDENT INFORMATION FORM \t\t\t\t")
def student():
        fp = open("studform.txt", "a")
        sdnamei = sdname.get()
        fp.write("Name: " + sdnamei + "\n")
        sdmisi = sdmis.get()
        fp.write("MIS ID : " + sdmisi + "\n")
        sdyeari = sdyear.get()
        fp.write("Year: " + sdyeari + "\n")
        sdbranchi = sdbranch.get()
        fp.write("Branch: " + sdbranchi + "\n")
        sdemaili = sdmail.get()
        fp.write("Email ID: " + sdemaili + "\n")
        sdnumi = sdnum.get()
        fp.write("Contact Number: " + sdnumi + "\n")
        sdaddressi = sdaddr.get()
        fp.write("Address: " + sdaddressi +"\n")
        sdcgpai = sdcgpa.get()
        fp.write("CGPA: " + sdcgpai + "\n")
        fp.write("\n")
        fp.close()
        return

def display():
        fp = open("studform.txt", "r")
        for data in fp:
                print(data)



app = Tk()

app.geometry("700x740")

app.title("STUDENT INFORMATION FORM")

name = Label(text="Name :")
mis = Label(text="MIS ID :")
year = Label(text="Year Of Study :")
branch = Label(text="Branch :")
email = Label(text="Email Id :")
number = Label(text="Contact Number :")
addr = Label(text="Address :")
cgpa = Label(text="CGPA :")

name.place(x=15,y=70)
mis.place(x=15,y=140)
year.place(x=15,y=210)
branch.place(x=15,y=280)
email.place(x=15,y=350)
number.place(x=15,y=420)
addr.place(x=15,y=490)
cgpa.place(x=15,y=560)

sdname = StringVar()
sdmis = StringVar()
sdyear = StringVar()
sdbranch = StringVar()
sdmail = StringVar()
sdnum = StringVar()
sdaddr = StringVar()
sdcgpa = StringVar()


namebox = Entry(textvariable=sdname,width="30")
misbox = Entry(textvariable=sdmis,width="30")
yearbox = Entry(textvariable=sdyear,width="30")
branchbox = Entry(textvariable=sdbranch,width="30")
mailbox = Entry(textvariable=sdmail,width="30")
numbox = Entry(textvariable=sdnum,width="30")
addrbox = Entry(textvariable=sdaddr,width="30")
cgpabox = Entry(textvariable=sdcgpa,width="30")

namebox.place(x=15,y=100)
misbox.place(x=15,y=180)
yearbox.place(x=15,y=240)
branchbox.place(x=15,y=300)
mailbox.place(x=15,y=370)
numbox.place(x=15,y=440)
addrbox.place(x=15,y=510)
cgpabox.place(x=15,y=580)

button1 = Button(app,text="Submit", command=student,width="30",height="2",bg="grey")

button1.place(x=15,y=680)

button2 = Button(app, text="Display", command=display,width="30",height="2",bg="grey")

button2.place(x=15,y=710)

mainloop()
