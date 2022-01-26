

from tkinter import*
from tkinter import messagebox
from tkinter import ttk
import mysql.connector


conn = mysql.connector.connect(
    host="sql6.freemysqlhosting.net", username="sql6467164", password="00manav00", database="sql6467164")
my_cursor = conn.cursor()


class hospital:

    def __init__(self, root):
        def new():
           
                insert_stmt = (
                                "INSERT INTO first( patient_name, refer_no, Age, disease, medicine, Blood_pressure,blood_group,medicaton,checked_by,contact_no)"
                                "VALUES (%s, %s, %s, %s ,%s,%s,%s,%s,%s,%s)")
                data = (self.pn.get(), self.id.get(), self.age.get(), self.dn.get(),self.mn.get(),self.bp.get(),self.bg.get(),self.medication.get(),self.dr.get(),self.cn.get())
                try:
                        my_cursor.execute(insert_stmt, data)
                        conn.commit()
                        messagebox.showinfo("info", "stored successfully")
                except:
                        conn.rollback()
                        messagebox.showinfo("info", "data Stored unsuccessfull")

       
        self.root = root
        self.root.title("HOSPITAL MANAGEMENT SYSTEM")
        self.root.geometry("1500x800+0+0")

        # ================================Heading of title========================================================================
        H = Label(self.root, bd=20, relief=GROOVE, font=("times new roman", 50),
                  text="HOSPITAL MANAGEMENT SYSTEM", width=1490, bg="#DC0049")
        H.pack()
        # ========================================detail frame===============================================================
        DF = Frame(self.root, bd=20, relief=GROOVE,)
        DF.place(x=0, y=100, width=1500, height=400)
        DFL = LabelFrame(DF, bd=15, relief=GROOVE, font=(
            "times new roman", 18), text="Patient's Detail", bg="#E5F5D0")
        DFL.place(x=0, y=0, width=1000, height=360)
        DFR = LabelFrame(DF, bd=15, relief=GROOVE, font=(
            "times new roman", 18), text="Prescription Detail", bg="#E5F5D0")
        DFR.place(x=1005, y=0, width=460, height=360)

        # ==========================================button frame=============================================================
        btnF = LabelFrame(self.root, bd=15, relief=GROOVE,
                          font=("times new roman", 18),)
        btnF.place(x=0, y=450, width=1500, height=85)
        # ========================================================================================================database frame===================================================
        DFD = Frame(self.root, bd=15, relief=GROOVE)
        DFD.place(x=0, y=520, width=1500, height=265)
        # ========================================================================

        # ================================================================================================================
        self.pn = StringVar()
        self.id = StringVar()
        self.age = StringVar()
        self.dn = StringVar()
        self.mn = StringVar()
        self.bp = StringVar()
        self.bg = StringVar()
        self.medication = StringVar()
        self.dr = StringVar()
        self.cn = StringVar()
        lbl_patient_name = Label(DFL, font=("times new roman", 20),text="Patient name:", padx=5, pady=10, bg="#E5F5D0")
        lbl_patient_name.grid(column=0, row=0, sticky=W)
        entry_patient_name = Entry(DFL, font=("times new roman", 20),textvariable=self.pn, bg="#FFF3E2")
        entry_patient_name.grid(column=1, row=0, sticky=W)

        lbl_patient_id = Label(DFL, font=("times new roman", 20),text="Patient ID.:", padx=5, pady=10, bg="#E5F5D0")
        lbl_patient_id.grid(column=0, row=1, sticky=W)
        entry_patient_id = Entry(DFL, font=("times new roman", 20),textvariable=self.id, bg="#FFF3E2")
        entry_patient_id.grid(column=1, row=1, sticky=W)

        lbl_age = Label(DFL, font=("times new roman", 20),text="Age:", padx=5, pady=10, bg="#E5F5D0")
        lbl_age.grid(column=0, row=2, sticky=W)
        entry_age = Entry(DFL, font=("times new roman", 20),textvariable=self.age, bg="#FFF3E2")
        entry_age.grid(column=1, row=2, sticky=W)

        lbl_disease = Label(DFL, font=("times new roman", 20),text="Disease Name:", padx=5, pady=10, bg="#E5F5D0")
        lbl_disease.grid(column=0, row=3, sticky=W)
        entry_disease = Entry(DFL, font=("times new roman", 20),textvariable=self.dn, bg="#FFF3E2")
        entry_disease.grid(column=1, row=3, sticky=W)

        lbl_medicine = Label(DFL, font=("times new roman", 20),text="Medicine Name:", padx=5, pady=10, bg="#E5F5D0")
        lbl_medicine.grid(column=0, row=4, sticky=W)
        entry_medicine = Entry(DFL, font=("times new roman", 20),textvariable=self.mn, bg="#FFF3E2")
        entry_medicine.grid(column=1, row=4, sticky=W)

        lbl_bp = Label(DFL, font=("times new roman", 20),text="Blood pressure:", padx=5, pady=10, bg="#E5F5D0")
        lbl_bp.grid(column=3, row=0, sticky=W)
        entry_bp = Entry(DFL, font=("times new roman", 20),textvariable=self.bp, bg="#FFF3E2")
        entry_bp.grid(column=4, row=0, sticky=W)

        lbl_bg = Label(DFL, font=("times new roman", 20),text="Blood group:", padx=5, pady=10, bg="#E5F5D0")
        lbl_bg.grid(column=3, row=1, sticky=W)
        entry_bg = Entry(DFL, font=("times new roman", 20),textvariable=self.bg, bg="#FFF3E2")
        entry_bg.grid(column=4, row=1, sticky=W)

        lbl_medication = Label(DFL, font=("times new roman", 20),text="Medication:", padx=5, pady=10, bg="#E5F5D0")
        lbl_medication.grid(column=3, row=2, sticky=W)
        entry_medication = Entry(DFL, font=("times new roman", 20),textvariable=self.medication, bg="#FFF3E2")
        entry_medication.grid(column=4, row=2, sticky=W)

        lbl_checked_by = Label(DFL, font=("times new roman", 20),text="Checked by:", padx=5, pady=10, bg="#E5F5D0")
        lbl_checked_by.grid(column=3, row=3, sticky=W)
        entry_checked_by = Entry(DFL, font=("times new roman", 20),textvariable=self.dr, bg="#FFF3E2")
        entry_checked_by.grid(column=4, row=3, sticky=W)

        lbl_contact = Label(DFL, font=("times new roman", 20),text="Contact NO:", padx=5, pady=10, bg="#E5F5D0")
        lbl_contact.grid(column=3, row=4, sticky=W)
        entry_contact = Entry(DFL, font=("times new roman", 20),textvariable=self.cn, bg="#FFF3E2")
        entry_contact.grid(column=4, row=4, sticky=W)
# ================================button ===========================================================================================================================
        btn1 = Button(btnF, font=("times new roman", 20, "bold"),
                      text="Save", width=18, bg="light blue", command=new)
        btn1.grid(column=0, row=0)
# ====================================================presciption button================================================================================
        btn2 = Button(btnF, font=("times new roman", 20, "bold"),
                      text="presciption data", width=20, bg="light blue")
        btn2.grid(column=1, row=0)
# =====================================================Update button=================================================================================================
        btn3 = Button(btnF, font=("times new roman", 20, "bold"),
                      text="Update", width=18, bg="light blue")
        btn3.grid(column=2, row=0)
        # ===========================================================Delete================================================================================================
        btn4 = Button(btnF, font=("times new roman", 20, "bold"),
                      text="Delete", width=18, bg="light blue")
        btn4.grid(column=3, row=0)
        # ===================================Exit button=============================================================================================================
        btn4 = Button(btnF, font=("times new roman", 20, "bold"),
                      text="Exit", width=14, bg="light blue")
        btn4.grid(column=4, row=0)
# ==========================================Scroll bar=============================================================================================================================
        scroll_x = Scrollbar(DFD, orient=HORIZONTAL)

        # self.hospital_table=ttk.Treeview(DFD,"pn","rn","age","dn","mn",xscrollcommand=scroll_x.set)
        self.trv = ttk.Treeview(DFD, columns=(
            "1", "2", "3", "4", "5","6","7","8","9","10"), xscrollcommand=scroll_x.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_x.config(command=self.trv.xview)

        self.trv.pack(fill=BOTH)
        # trv["columns"] = ("1", "2", "3", "4", "5")

# Defining heading
        self.trv['show'] = 'headings'

# width of columns and alignment
        self.trv.column("1", width=80, )
        self.trv.column("2", width=80, )
        self.trv.column("3", width=80, )
        self.trv.column("4", width=80, )
        self.trv.column("6", width=80, )
        self.trv.column("7", width=80, )
        self.trv.column("8", width=80, )
        self.trv.column("9", width=80, )
        self.trv.column("10", width=80, )

# Headings
# respective columns
        self.trv.heading("1", text="Patient name")
        self.trv.heading("2", text="Patient id")
        self.trv.heading("3", text="Age")
        self.trv.heading("4", text="Disease name")
        self.trv.heading("5", text="medicine name")
        self.trv.heading("6", text="Blood Pressure")
        self.trv.heading("7", text="Blood group")
        self.trv.heading("8", text="Medication")
        self.trv.heading("9", text="Checked by")
        self.trv.heading("10", text="Contact No.")

# scroll_y.pack( side = RIGHT, fill = Y )


root = Tk()
ob = hospital(root)
root.mainloop()
