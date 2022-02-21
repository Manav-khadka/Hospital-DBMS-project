'''
This is hostial management software
made by using Python module TKINTER
and for database I use MySQL

developer: Manav Khadka
Branch: Btech CSE
Enrollment no.:LNCBBTCSE062
'''

from tkinter import*  # module for making GUI window
from tkinter import messagebox  # Module to show msgbox like errror, info
# module to import importang GUI widgets like Entry , Frame, label
from tkinter import ttk
import mysql.connector  # module to connect gui or python to  mysql database


login = Tk()  # starting login window
login.title("HOSPITAL MANAGEMENT SYSTEM")
# for icon of hospital management system
login.iconbitmap("./resources/hospital.ico")
login.geometry("1540x800+100+50")  # defining the size of our login window

user_login_image = PhotoImage(file="./resources/Login.png")
label_background = Label(login, image=user_login_image)  # labeling login UI
label_background.pack()

# Entry box for usename
entry_username = Entry(login, font=("times new roman", 20))
entry_username.place(x=280, y=215)

entry_password = Entry(login, font=("times new roman", 20),
                       show=("*"))  # ENtry box for PAssword
entry_password.place(x=280, y=280)
# this is management function here we define selection button like patient management,
# doctor manmagement , staff managment


def mgmnt():
    # if condition to check that id and password is correct or not
    if entry_username.get() == "Admin" and entry_password.get() == "1234":
        login.destroy()  # destroying login window after Successfully login
        management = Tk()  # Selection window after successfully login
        management.iconbitmap("./resources/hospital.ico")
        management.geometry("1500x800+100+50")
        management.title("Select Management System")
        mgmnt_image = PhotoImage(file="./resources/selection.png")
        label2_background = Label(management, image=mgmnt_image)
        label2_background.pack()
        # if user select patient in managment system then second login page will open
        # where we should give  our server information

        def login2():
            management.destroy()  # after successfully login and connection with MySQL server
            # management login destroy
            mysqlhosting = Tk()  # login 2 window is started
            mysqlhosting.title("HOSTING DETAILS")
            mysqlhosting.iconbitmap("./resources/hospital.ico")
            mysqlhosting.geometry("500x400+100+50")
            mysql_image = PhotoImage(file="./resources/sqllogin.png")
            mysql_background = Label(mysqlhosting, image=mysql_image)
            mysql_background.pack()

            h = StringVar()
            u = StringVar()
            p = StringVar()
            entry_host = Entry(mysqlhosting, font=(
                "times new roman", 20), textvariable=h, bg="light green")
            entry_host.place(x=160, y=113)  # entry box for host server address
            entry_user = Entry(mysqlhosting, font=(
                "times new roman", 20), textvariable=u, bg="light green")
            entry_user.place(x=160, y=190)  # entry box for host address
            entry_pass = Entry(mysqlhosting, font=(
                "times new roman", 20), textvariable=p, bg="light green", show=("*"))
            # entry box for our data base password
            entry_pass.place(x=160, y=260)

            def patient():  # defining the function for patient body
        # after successfully login sql login page will destroy and new root or main window will open
                mysqlhosting.destroy()
                conn = mysql.connector.connect(host=h.get(), username=u.get(
                ), password=p.get())  # connecting to our database
                my_cursor = conn.cursor()
                # CReating databse if not exist using MySQL Query
                operation = """CREATE DATABASE IF NOT EXISTS new"""  
                my_cursor.execute(operation)
                operation = """USE new"""  # using  data base that we created
                my_cursor.execute(operation)
                # creating table if not exit using MySQL query
                operation = """CREATE TABLE IF NOT EXISTS patient_details( 
                        Patient_ID             VARCHAR(50)          NOT NULL    PRIMARY KEY,
                        Patient_name           VARCHAR(50)          NOT NULL,
                        Age                    VARCHAR(50)          NOT NULL,
                        Disease_Name           VARCHAR(50)          NOT NULL,
                        Medicine_Name          VARCHAR(50)          NOT NULL,
                        Blood_pressure         VARCHAR(50)          NOT NULL,
                        blood_group            VARCHAR(50)          NOT NULL,
                        Medication             VARCHAR(50)          NOT NULL,
                        Checked_by             VARCHAR(50)          NOT NULL,
                        Contact_NO             VARCHAR(50)          NOT NULL)"""
                my_cursor.execute(operation)
                root = Tk()  # creating main or root window affte successfull login
                root.iconbitmap("./resources/hospital.ico")
                root.title("PATIENT'S MANAGEMENT SYSTEM")
                root.geometry("1500x800+0+0")
                # stopping resizing the main window
                root.resizable(False, False)
    # ================================Heading of title========================================================================
            # Labelling heading on main window using Label widget
                H = Label(root, bd=20, relief=GROOVE, font=("times new roman", 50),  
                          text="PATIENT's MANAGEMENT SYSTEM", width=1490, bg="#DC0049")
                H.pack()
        # ========================================detail frame===============================================================
                # MAking data frame on main window using Frame widget
                DF = Frame(root, bd=20, relief=GROOVE,)
                DF.place(x=0, y=100, width=1500, height=400)
                # labelingon frame for left data frame in which we enter patient detail
                DFL = LabelFrame(DF, bd=15, relief=GROOVE, font=(
                    "times new roman", 18), text="Patient's Detail", bg="#E5F5D0")
                DFL.place(x=0, y=0, width=1000, height=360)
                DFR = LabelFrame(DF, bd=15, relief=GROOVE, font=(
                    "times new roman", 18), text="Prescription", bg="#E5F5D0")
                DFR.place(x=1005, y=0, width=460, height=360)

                txtpresciption = Text(DFR, font=(
                    "times new roman", 18), bg="#F1F6DD")
                txtpresciption.pack()
                # ==========================================button frame=============================================================
                btnF = LabelFrame(root, bd=15, relief=GROOVE,
                                  font=("times new roman", 18),)
                btnF.place(x=0, y=450, width=1500, height=85)
                # =========================================database frame===================================================
                DFD = Frame(root, bd=15, relief=GROOVE)
                DFD.place(x=0, y=520, width=1500, height=265)
    # ================================================================================================================
            # defining the type of variable
                id = StringVar()
                pn = StringVar()
                age = StringVar()
                dn = StringVar()
                mn = StringVar()
                bp = StringVar()
                bg = StringVar()
                medication = StringVar()
                dr = StringVar()
                cn = StringVar()
                # Entry for patient detail entry
                lbl_patient_id = Label(DFL, font=(
                    "times new roman", 20), text="Patient ID.:", padx=5, pady=10, bg="#E5F5D0")
                lbl_patient_id.grid(column=0, row=0, sticky=W)
                entry_patient_id = Entry(DFL, font=(
                    "times new roman", 20), textvariable=id, bg="#FFF3E2")
                entry_patient_id.grid(column=1, row=0, sticky=W)

                lbl_patient_name = Label(DFL, font=(
                    "times new roman", 20), text="Patient name:", padx=5, pady=10, bg="#E5F5D0")
                lbl_patient_name.grid(column=0, row=1, sticky=W)
                entry_patient_name = Entry(DFL, font=(
                    "times new roman", 20), textvariable=pn, bg="#FFF3E2")
                entry_patient_name.grid(column=1, row=1, sticky=W)

                lbl_age = Label(DFL, font=("times new roman", 20),
                                text="Age:", padx=5, pady=10, bg="#E5F5D0")
                lbl_age.grid(column=0, row=2, sticky=W)
                entry_age = Entry(DFL, font=("times new roman", 20),
                                  textvariable=age, bg="#FFF3E2")
                entry_age.grid(column=1, row=2, sticky=W)

                lbl_disease = Label(DFL, font=("times new roman", 20),
                                    text="Disease Name:", padx=5, pady=10, bg="#E5F5D0")
                lbl_disease.grid(column=0, row=3, sticky=W)
                entry_disease = Entry(DFL, font=("times new roman", 20),
                                      textvariable=dn, bg="#FFF3E2")
                entry_disease.grid(column=1, row=3, sticky=W)

                lbl_medicine = Label(DFL, font=("times new roman", 20),
                                     text="Medicine Name:", padx=5, pady=10, bg="#E5F5D0")
                lbl_medicine.grid(column=0, row=4, sticky=W)
                entry_medicine = Entry(DFL, font=(
                    "times new roman", 20), textvariable=mn, bg="#FFF3E2")
                entry_medicine.grid(column=1, row=4, sticky=W)

                lbl_bp = Label(DFL, font=("times new roman", 20),
                               text="Blood pressure:", padx=5, pady=10, bg="#E5F5D0")
                lbl_bp.grid(column=3, row=0, sticky=W)
                entry_bp = Entry(DFL, font=("times new roman", 20),
                                 textvariable=bp, bg="#FFF3E2")
                entry_bp.grid(column=4, row=0, sticky=W)

                lbl_bg = Label(DFL, font=("times new roman", 20),
                               text="Blood group:", padx=5, pady=10, bg="#E5F5D0")
                lbl_bg.grid(column=3, row=1, sticky=W)
                entry_bg = Entry(DFL, font=("times new roman", 20),
                                 textvariable=bg, bg="#FFF3E2")
                entry_bg.grid(column=4, row=1, sticky=W)

                lbl_medication = Label(DFL, font=(
                    "times new roman", 20), text="Medication:", padx=5, pady=10, bg="#E5F5D0")
                lbl_medication.grid(column=3, row=2, sticky=W)
                entry_medication = Entry(DFL, font=(
                    "times new roman", 20), textvariable=medication, bg="#FFF3E2")
                entry_medication.grid(column=4, row=2, sticky=W)

                lbl_checked_by = Label(DFL, font=(
                    "times new roman", 20), text="Checked by:", padx=5, pady=10, bg="#E5F5D0")
                lbl_checked_by.grid(column=3, row=3, sticky=W)
                entry_checked_by = Entry(DFL, font=(
                    "times new roman", 20), textvariable=dr, bg="#FFF3E2")
                entry_checked_by.grid(column=4, row=3, sticky=W)

                lbl_contact = Label(DFL, font=("times new roman", 20),
                                    text="Contact NO:", padx=5, pady=10, bg="#E5F5D0")
                lbl_contact.grid(column=3, row=4, sticky=W)
                entry_contact = Entry(DFL, font=("times new roman", 20),
                                      textvariable=cn, bg="#FFF3E2")
                entry_contact.grid(column=4, row=4, sticky=W)

                # ==========================================Scroll bar=============================================================================================================================
                scroll_x = Scrollbar(DFD, orient=HORIZONTAL)

                #   hospital_table=ttk.Treeview(DFD,"pn","rn","age","dn","mn",xscrollcommand=scroll_x.set)
                trv = ttk.Treeview(DFD, columns=(
                    "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"), xscrollcommand=scroll_x.set)
                scroll_x.pack(side=BOTTOM, fill=X)
                scroll_x.config(command=trv.xview)
                style = ttk.Style()
                style.configure("Treeview.Heading", font=(
                    "times new roman", 11, "bold"))

            # making colums and colums heading in table where detail will show from database
                trv.heading("1", text="Patient ID", anchor="w",)
                trv.heading("2", text="Patient Name", anchor="w")
                trv.heading("3", text="Age", anchor="w")
                trv.heading("4", text="Disease Name", anchor="w")
                trv.heading("5", text="Medicine Name", anchor="w")
                trv.heading("6", text="Blood Pressure", anchor="w")
                trv.heading("7", text="Blood group", anchor="w")
                trv.heading("8", text="Medication", anchor="w")
                trv.heading("9", text="Checked by", anchor="w")
                trv.heading("10", text="Contact No.", anchor="w")
                trv['show'] = 'headings'
                trv.column("1", width=80,)
                trv.column("2", width=80, )
                trv.column("3", width=60, )
                trv.column("4", width=80, )
                trv.column("5", width=80, )
                trv.column("6", width=80, )
                trv.column("7", width=80, )
                trv.column("8", width=80, )
                trv.column("9", width=80, )
                trv.column("10", width=80, )
                trv.pack(fill=BOTH)
        # =============================defining function for button===============================================

                def update():  # update function to update the patient data here We use MySQL Query
                    if pn.get() == "" or id.get() == "":
                        messagebox.showinfo("Info", "Select data to update")
                    else:
                        my_cursor.execute("""UPDATE patient_details SET 
                                        Patient_name=%s,
                                        Age=%s,
                                        Disease_Name=%s,
                                        Medicine_Name=%s,
                                        Blood_pressure=%s,
                                        Blood_group=%s,
                                        Medication=%s,
                                        Checked_by=%s,
                                        Contact_NO=%s
                                        WHERE Patient_ID=%s""", (
                            entry_patient_name.get(),
                            entry_age.get(),
                            entry_disease.get(),
                            entry_medicine.get(),
                            entry_bp.get(),
                            entry_bg.get(),
                            entry_medication.get(),
                            entry_checked_by.get(),
                            entry_contact.get(),
                            entry_patient_id.get(),)
                        )
                        conn.commit()
                        fetch_data()
                        entry_patient_name.delete(0, END)
                        entry_patient_id.delete(0, END)
                        entry_age.delete(0, END)
                        entry_disease.delete(0, END)
                        entry_medicine.delete(0, END)
                        entry_bp.delete(0, END)
                        entry_bg.delete(0, END)
                        entry_medication.delete(0, END)
                        entry_checked_by.delete(0, END)
                        entry_contact.delete(0, END)
                        messagebox.showinfo("info", "successfully updated")

        # ------------------------------------------------search function----------------------------------------------

                def search():
                    search = Tk()
                    search.title("SEARCH PATIENT DETAIL")
                    search.geometry("400x300")
                    lbl_search = Label(search, font=(
                        "times new roman", 25,), text="Patient ID:-")
                    lbl_search.place(x=140, y=30)
                    s = StringVar()
                    entry_search = Entry(search, font=(
                        "times new roman", 25), textvariable=s,)
                    entry_search.place(x=40, y=80)

                    def show():

                        for record in trv.get_children():
                            # deleting all children from table
                            trv.delete(record)
                        s1 = entry_search.get()  # getting from search box
                        # Query for selecting patient name
                        my_cursor.execute(
                            "SELECT * FROM patient_details WHERE Patient_name LIKE '%"+s1+"%'")
                        rows = my_cursor.fetchall()
                        trv.delete(*trv.get_children())
                        for i in rows:
                            trv.insert("", END, values=(i))
                        search.destroy()

                    btn_search = Button(search, text="Search", font=(
                        "times new roman", 20), command=show)
                    btn_search.place(x=110, y=130, width=150)
                    search.mainloop()

                def fetch_data():  # function tp fetched data from database
                    my_cursor.execute("SELECT * FROM patient_details")
                    rows = my_cursor.fetchall()
                    if len(rows) != 0:

                        # Deleting all children
                        trv.delete(*trv.get_children())

                        for i in rows:
                            # after deleting all children
                            trv.insert("", END, value=(i))
                fetch_data()

                def presciption():  # function to print presciption
                    txtpresciption.delete("1.0", "end")

                    txtpresciption.insert(
                        END, "Patient ID:\t\t"+entry_patient_id.get()+"\n",)
                    txtpresciption.insert(
                        END, "Patient Name:\t\t"+entry_patient_name.get()+"\n")
                    txtpresciption.insert(END, "Age:\t\t"+entry_age.get()+"\n")
                    txtpresciption.insert(
                        END, "Disease Name:\t\t"+entry_disease.get()+"\n")
                    txtpresciption.insert(
                        END, "Medicine Name:\t\t"+entry_medicine.get()+"\n")
                    txtpresciption.insert(
                        END, "Blood Pressure:\t\t"+entry_bp.get()+"\n")
                    txtpresciption.insert(
                        END, "Blood Group:\t\t"+entry_bg.get()+"\n")
                    txtpresciption.insert(
                        END, "Medication:\t\t"+entry_medication.get()+"\n")
                    txtpresciption.insert(
                        END, "Checked By:\t\t"+entry_checked_by.get()+"\n")
                    txtpresciption.insert(
                        END, "Contact NO:\t\t"+entry_contact.get()+"\n")

                def select():  # Function for selection of data from table and show into the entry box
                    # here first we delete all entry boxes
                    entry_patient_id.delete(0, END)
                    entry_patient_name.delete(0, END)
                    entry_age.delete(0, END)
                    entry_disease.delete(0, END)
                    entry_medicine.delete(0, END)
                    entry_bp.delete(0, END)
                    entry_bg.delete(0, END)
                    entry_medication.delete(0, END)
                    entry_checked_by.delete(0, END)
                    entry_contact.delete(0, END)
                    selected = trv.focus()  # focusing values of treevie on entry boxes
                    values = trv.item(selected, 'values')
                # After deleting we insert selected item back on entry boxes
                    entry_patient_id.insert(0, values[0])
                    entry_patient_name.insert(1, values[1])
                    entry_age.insert(2, values[2])
                    entry_disease.insert(3, values[3])
                    entry_medicine.insert(4, values[4])
                    entry_bp.insert(5, values[5])
                    entry_bg.insert(6, values[6])
                    entry_medication.insert(7, values[7])
                    entry_checked_by.insert(8, values[8])
                    entry_contact.insert(9, values[9])

                def delete():  # function for delete selected data of ptient
                    if pn.get() == "" or id.get() == "":
                        messagebox.showerror("Error", "Select to delete")
                    else:
                        my_cursor.execute(
                            """DELETE FROM patient_details WHERE Patient_ID=%s""", (entry_patient_id.get(),))
                        conn.commit()
                        fetch_data()
                        entry_patient_name.delete(0, END)
                        entry_patient_id.delete(0, END)
                        entry_age.delete(0, END)
                        entry_disease.delete(0, END)
                        entry_medicine.delete(0, END)
                        entry_bp.delete(0, END)
                        entry_bg.delete(0, END)
                        entry_medication.delete(0, END)
                        entry_checked_by.delete(0, END)
                        entry_contact.delete(0, END)
                        fetch_data()
                        messagebox.showinfo("info", "deleted")

                def save():  # function to save the patient data record
                    insert_stmt = ("""
                        "INSERT INTO patient_details(Patient_ID,Patient_name, Age, Disease_Name,
                                                        Medicine_Name, Blood_pressure,Blood_group,
                                                        Medication,Checked_by,Contact_NO)"
                        "VALUES (%s, %s, %s, %s ,%s,%s,%s,%s,%s,%s)" """)
                    data = (id.get(), pn.get(),      age.get(),   dn.get(),   mn.get(
                    ),   bp.get(),   bg.get(),   medication.get(),   dr.get(),   cn.get())
                    if pn.get() == "" or id.get() == "" or age.get() == "" :
                        messagebox.showerror(
                            "Error ", "All field are mandatory")
                    else:
                        try:
                            my_cursor.execute(insert_stmt, data)
                            messagebox.showinfo("info", "stored successfully")
                        except:
                            conn.rollback()
                            messagebox.showinfo(
                                "info", "data Stored unsuccessfull")
                    conn.commit()
                    fetch_data()

                def exit():

                    root.destroy()
    # ========================================= button ===========================================================================================================================
        # =========================================select==========================================
                btn_select = Button(btnF, font=("times new roman", 17, "bold"),
                                    text="Select", width=14, bg="light blue", command=select)
                btn_select.grid(column=2, row=0)
        # ====================================================presciption button===================================

                btn_presciption = Button(btnF, font=("times new roman", 17, "bold"),
                                         text="presciption", width=20, bg="light blue",
                                         command=presciption)
                btn_presciption.grid(column=1, row=0)
        # ==================================================Save=================================
                btn_save = Button(btnF, font=("times new roman", 17, "bold"),
                                  text="Save", width=13, bg="light blue", command=save,)
                btn_save.grid(column=0, row=0)
        # ===========================================================Delete===========================================
                btn_delete = Button(btnF, font=("times new roman", 17, "bold"),
                                    text="Delete", width=15, bg="light blue", command=delete)
                btn_delete.grid(column=4, row=0)
        # =====================================================Update button===========================================
                btn_update = Button(btnF, font=("times new roman", 17, "bold"),
                                    text="Update", width=14, bg="light blue", command=update)
                btn_update.grid(column=3, row=0)
        # ===================================Exit button==============================================================
                btn_search = Button(btnF, font=("times new roman", 17, "bold"),
                                    text="Search", width=13, bg="light blue", command=search)
                btn_search.grid(column=5, row=0)
        # =================================search==============================================
                btn_exit = Button(btnF, font=("times new roman", 17, "bold"),
                                  text="Exit", width=10, bg="light blue", command=exit)
                btn_exit.grid(column=6, row=0)

                root.mainloop()
            btn_mysql = Button(mysqlhosting, text="LOGIN", font=(
                "times new roman", 20, "bold"), command=patient, bg="blue", fg="white")
            btn_mysql.place(x=190, y=350, width=200, height=40)
            mysqlhosting.mainloop()

        img_patient_mgmnt = PhotoImage(
            file="C:/Users/manav/Desktop/final project/patientmanagement.png")
        btn_patient_mgmnt = Button(
            management, image=img_patient_mgmnt, borderwidth=0, command=login2)
        btn_patient_mgmnt.place(x=111, y=222, width=485, height=50)

        img_dr_mgmnt = PhotoImage(
            file="C:/Users/manav/Desktop/final project/drmngment.png")
        btn_dr_mgmnt = Button(management, image=img_dr_mgmnt, borderwidth=0)
        btn_dr_mgmnt.place(x=111, y=285, width=485, height=50)

        img_staff_mgmnt = PhotoImage(
            file="C:/Users/manav/Desktop/final project/staff.png")
        btn_staff_mgmnt = Button(
            management, image=img_staff_mgmnt, borderwidth=0)
        btn_staff_mgmnt.place(x=111, y=350, width=485, height=50)
        management.resizable(False, False)
        management.mainloop()

    else:
        messagebox.showerror("Error 404", "Wrong creditial")


but_login = Button(login, font=("times new roman", 15),
                   text="Login", command=mgmnt)
but_login.place(x=310, y=340, width=200)
login.resizable(False, False)
login.mainloop()
