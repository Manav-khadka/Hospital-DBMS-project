from logging import root
from tkinter import*
from tkinter import messagebox
from tkinter import ttk

import mysql.connector



login=Tk()
login.title("HOSPITAL MANAGEMENT SYSTEM")
login.geometry("1540x800+0+0")
user_login_image=PhotoImage(file="./res/h.png")
label_background=Label(login,image=user_login_image)
label_background.pack()

entry_username=Entry(login,font=("times new roman",20))
entry_username.place(x=280,y=215)

entry_password=Entry(login,font=("times new roman",20),show=("*"))
entry_password.place(x=280,y=280)
  

        

def mgmnt():
    
    if entry_username.get()=="Admin" and entry_password.get()=="hospital":
    
        login.destroy()
        management=Tk()
         
        
        
         
        management.geometry("1500x800+0+0")
        management.title("Select Management System")
        mgmnt_image=PhotoImage(file="./res/h2.png")
        label2_background=Label(management,image=mgmnt_image)
        label2_background.pack()
        def patient():
            management.destroy()
            
            
            conn = mysql.connector.connect(
                host="localhost", username="root", password="#manav@123", database="new")
            my_cursor = conn.cursor()
               
            def save(): 
                insert_stmt = (
                            "INSERT INTO first(  Patient_ID,Patient_name, Age, Disease_Name, Medicine_Name, Blood_pressure,Blood_group,Medication,Checked_by,Contact_NO)"
                            "VALUES (%s, %s, %s, %s ,%s,%s,%s,%s,%s,%s)")
                data = (id.get(),pn.get(),      age.get(),   dn.get(),   mn.get(
                        ),   bp.get(),   bg.get(),   medication.get(),   dr.get(),   cn.get())
                if pn.get() == "" or id.get() == "" or age.get()=="" or dn.get()=="" or mn.get()=="" or bp.get()=="" or bg.get()=="" or medication.get()=="" or dr.get()=="" or cn.get()=="":
                            messagebox.showerror("Error ", "All field are mandatory")
                else:
                    try:
                        my_cursor.execute(insert_stmt, data)
                        messagebox.showinfo("info", "stored successfully")
                    except:
                        conn.rollback()
                        messagebox.showinfo("info", "data Stored unsuccessfull")
                conn.commit()
                fetch_data()

            def exit():
                root.destroy()
                               

            def update():
                if pn.get()=="" or id.get()=="":
                    messagebox.showinfo("Info","Select data to update")
                else:
                    
                    
                            
                                    
                    my_cursor.execute("""UPDATE first SET 
                                    Patient_name=%s,
                                    Age=%s,
                                    Disease_Name=%s,
                                    Medicine_Name=%s,
                                    Blood_pressure=%s,
                                    Blood_group=%s,
                                    Medication=%s,
                                    Checked_by=%s,
                                    Contact_NO=%s
                                    WHERE Patient_ID=%s""",(
                                    
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
                    entry_patient_name.delete(0,END)
                    entry_patient_id.delete(0,END)
                    entry_age.delete(0,END)
                    entry_disease.delete(0,END)
                    entry_medicine.delete(0,END)
                    entry_bp.delete(0,END)
                    entry_bg.delete(0,END)
                    entry_medication.delete(0,END)
                    entry_checked_by.delete(0,END)
                    entry_contact.delete(0,END)

                    
                    
                    
                    messagebox.showinfo("info","successfully updated")

            def delete():
                if pn.get()=="" or id.get()=="":
                        messagebox.showerror("Eror","Select to delete")
                else:
                            
                                    
                    my_cursor.execute("""DELETE FROM first WHERE 
                                    
                                    Patient_ID=%s""",(
                                    
                                        
                                        entry_patient_id.get(),)
                                        
                                    )
                    conn.commit()
                    fetch_data()
                    entry_patient_name.delete(0,END)
                    entry_patient_id.delete(0,END)
                    entry_age.delete(0,END)
                    entry_disease.delete(0,END)
                    entry_medicine.delete(0,END)
                    entry_bp.delete(0,END)
                    entry_bg.delete(0,END)
                    entry_medication.delete(0,END)
                    entry_checked_by.delete(0,END)
                    entry_contact.delete(0,END)

                    
                    
                    fetch_data()

                    
                    messagebox.showinfo("info","deleted")
            root = Tk()
            root.title("PATIENT'S MANAGEMENT SYSTEM")
            root.geometry("1500x800+0+0")
            root.resizable(False, False)

                    # ================================Heading of title========================================================================
            H = Label(root, bd=20, relief=GROOVE, font=("times new roman", 50),
                                text="PATIENT's MANAGEMENT SYSTEM", width=1490, bg="#DC0049")
            H.pack()
                    # ========================================detail frame===============================================================
            DF = Frame(root, bd=20, relief=GROOVE,)
            DF.place(x=0, y=100, width=1500, height=400)
            DFL = LabelFrame(DF, bd=15, relief=GROOVE, font=(
                        "times new roman", 18), text="Patient's Detail", bg="#E5F5D0")
            DFL.place(x=0, y=0, width=1000, height=360)
            DFR = LabelFrame(DF, bd=15, relief=GROOVE, font=(
                        "times new roman", 18), text="Prescription", bg="#E5F5D0")
            DFR.place(x=1005, y=0, width=460, height=360)

            txtpresciption=Text(DFR,font=("times new roman",18),bg="#F1F6DD")
            txtpresciption.pack()
                    # ==========================================button frame=============================================================
            btnF = LabelFrame(root, bd=15, relief=GROOVE,
                                        font=("times new roman", 18),)
            btnF.place(x=0, y=450, width=1500, height=85)
                    # ========================================================================================================database frame===================================================
            DFD = Frame(root, bd=15, relief=GROOVE)
            DFD.place(x=0, y=520, width=1500, height=265)
                    # ========================================================================

                    # ================================================================================================================
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
                # ================================button ===========================================================================================================================
            btn1 = Button(btnF, font=("times new roman", 17, "bold"),
                                text="Save", width=18, bg="light blue", command=save,)
            btn1.grid(column=0, row=0)
                # ====================================================presciption button================================================================================
                # =====================================================Update button=================================================================================================
                    # ===========================================================Delete================================================================================================
            btn5 = Button(btnF, font=("times new roman", 17, "bold"),
                                text="Delete", width=18, bg="light blue",command=delete)
            btn5.grid(column=4, row=0)
            btn4 = Button(btnF, font=("times new roman", 17, "bold"),
                                text="Update", width=16, bg="light blue",command=update)
            btn4.grid(column=3, row=0)
                    # ===================================Exit button=============================================================================================================

            btn6 = Button(btnF, font=("times new roman",17, "bold"),
                                text="Exit", width=14, bg="light blue",command=exit)
            btn6.grid(column=5, row=0)
            

            def presciption():
                txtpresciption.delete("1.0","end")
                    
                txtpresciption.insert(END,"Patient ID:\t\t"+entry_patient_id.get()+"\n",)
                txtpresciption.insert(END,"Patient Name:\t\t"+entry_patient_name.get()+"\n")
                txtpresciption.insert(END,"Age:\t\t"+entry_age.get()+"\n")
                txtpresciption.insert(END,"Disease Name:\t\t"+entry_disease.get()+"\n")
                txtpresciption.insert(END,"Medicine Name:\t\t"+entry_medicine.get()+"\n")
                txtpresciption.insert(END,"Blood Pressure:\t\t"+entry_bp.get()+"\n")
                txtpresciption.insert(END,"Blood Group:\t\t"+entry_bg.get()+"\n")
                txtpresciption.insert(END,"Medication:\t\t"+entry_medication.get()+"\n")
                txtpresciption.insert(END,"Checked By:\t\t"+entry_checked_by.get()+"\n")
                txtpresciption.insert(END,"Contact NO:\t\t"+entry_contact.get()+"\n")

                # btn7=Bu
            btn2 = Button(btnF, font=("times new roman", 17, "bold"),
                                text="presciption", width=20, bg="light blue",command=presciption)
            btn2.grid(column=1, row=0)
                # ==========================================Scroll bar=============================================================================================================================
            scroll_x = Scrollbar(DFD, orient=HORIZONTAL)

                    #   hospital_table=ttk.Treeview(DFD,"pn","rn","age","dn","mn",xscrollcommand=scroll_x.set)
            trv = ttk.Treeview(DFD, columns=(
                            "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"), xscrollcommand=scroll_x.set)
            scroll_x.pack(side=BOTTOM, fill=X)
            scroll_x.config(command=trv.xview)
            style = ttk.Style()
            style.configure("Treeview.Heading", font=("times new roman", 11,"bold"))


            trv.heading("1", text="Patient ID",anchor="w",)
            trv.heading("2", text="Patient Name",anchor="w")
            trv.heading("3", text="Age",anchor="w")
            trv.heading("4", text="Disease Name",anchor="w")
            trv.heading("5", text="Medicine Name",anchor="w")
            trv.heading("6", text="Blood Pressure",anchor="w")
            trv.heading("7", text="Blood group",anchor="w")
            trv.heading("8", text="Medication",anchor="w")
            trv.heading("9", text="Checked by",anchor="w")
            trv.heading("10", text="Contact No.",anchor="w")
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
            def fetch_data():
                my_cursor.execute("SELECT * FROM first")
                rows = my_cursor.fetchall()
                if len(rows)!=0:
                    trv.delete(*trv.get_children())
                        
                    for i in rows:
                        trv.insert("", END, value=(i))
            fetch_data()


            def get_cursor(): 
                entry_patient_id.delete(0,END)
                entry_patient_name.delete(0,END)
                entry_age.delete(0,END)
                entry_disease.delete(0,END)
                entry_medicine.delete(0,END)
                entry_bp.delete(0,END)
                entry_bg.delete(0,END)
                entry_medication.delete(0,END)
                entry_checked_by.delete(0,END)
                entry_contact.delete(0,END)
                selected=trv.focus()
                values=trv.item(selected,'values')
                    
                entry_patient_id.insert(0,values[0])
                entry_patient_name.insert(1,values[1])
                entry_age.insert(2,values[2])
                entry_disease.insert(3,values[3])
                entry_medicine.insert(4,values[4])
                entry_bp.insert(5,values[5])
                entry_bg.insert(6,values[6])
                entry_medication.insert(7,values[7])
                entry_checked_by.insert(8,values[8])
                entry_contact.insert(9,values[9])
            btn3 = Button(btnF, font=("times new roman", 17, "bold"),
                                text="Select", width=14, bg="light blue",command=get_cursor)
            btn3.grid(column=2, row=0)

            root.mainloop()
        
            
        
        
        # =============================defining function for button===============================================
            
    
            
        img_patient_mgmnt=PhotoImage(file="C:/Users/manav/Desktop/final project/patientmanagement.png")
        btn_patient_mgmnt=Button(management,image=img_patient_mgmnt,borderwidth=0,command=patient)
        btn_patient_mgmnt.place(x=111,y=222,width=485,height=50)

        img_dr_mgmnt=PhotoImage(file="C:/Users/manav/Desktop/final project/drmngment.png")
        btn_dr_mgmnt=Button(management,image=img_dr_mgmnt,borderwidth=0)
        btn_dr_mgmnt.place(x=111,y=285,width=485,height=50)
        
        img_staff_mgmnt=PhotoImage(file="C:/Users/manav/Desktop/final project/staff.png")
        btn_staff_mgmnt=Button(management,image=img_staff_mgmnt,borderwidth=0)
        btn_staff_mgmnt.place(x=111,y=350,width=485,height=50)
        management.resizable(False, False)
        management.mainloop()
        # management.mainloop()
    else:
        messagebox.showerror("Error 404","Wrong creditial")        



but_login=Button(login,font=("times new roman",15),text="Login",command=mgmnt)
but_login.place(x=310,y=340,width=200)
login.resizable(False, False)
login.mainloop()
