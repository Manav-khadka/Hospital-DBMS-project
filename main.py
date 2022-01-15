
from cgitb import text
from ctypes.wintypes import SIZE
from msilib.schema import ComboBox
from tkinter import*
from tkinter import ttk
import random
import datetime
from tkinter import messagebox
from tkinter import font
from turtle import width
import mysql.connector


class hospital:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital management system")
        self.root.geometry("1540x800+0+0")
        l1 = Label(self.root, bd=10, relief=GROOVE, text="HOSPITAL MANAGEMENT SYSYTEM",
                   bg="cyan", fg="purple", font=("Arial Bold", 50, "bold",))

        l1.pack(side=TOP, fill=X)
        dataframe = Frame(self.root, bd=15, relief=GROOVE)
        dataframe.place(x=0, y=125, width=1530, height=400)
        # l1.grid(column=0, row=0)
        dataframeleft = LabelFrame(dataframe, bd=10, relief=GROOVE,
                              padx=10,font=("times new roman",20,), text="Patient's Information" )
        dataframeleft.place(x=0, y=0, width=960, height=365,)
                            
        dataframeright = LabelFrame(dataframe, bd=10, relief=GROOVE, 
                                padx=10,font=("times new roman",20,),text="Presciption")
        dataframeright.place(x=965, y=0, width=527, height=365)
        dataframedown = LabelFrame(self.root, bd=10, relief=GROOVE
                                )
        dataframedown.place(x=0, y=490, width=1530, height=60)
        # ============================details=========================
        # =====================patient name============================================
        lblname=Label(dataframeleft,font=("Arial",15),text="Name of Patient's =",padx=2)
        lblname.grid(column=0,row=0)
        txtname=Entry(dataframeleft,font=("Arial",14),width=35)
        txtname.grid(column=1,row=0)
        # =================================Age of patient====================================
        lbl=Label(dataframeleft,font=("Arial",15),text="Age of patient       =",padx=2)
        lbl.grid(column=0,row=2)
        txt=Entry(dataframeleft,font=("arial",14),width=35)
        txt.grid(column=1,row=2)
        
        # ===================================name of disease===============

        lbldiseases=Label(dataframeleft,font=("Arial",15),text="Name of disease  =",padx=2)
        lbldiseases.grid(column=0,row=3)
        txtdisease=Entry(dataframeleft,font=("arial",14),width=35)
        txtdisease.grid(column=1,row=3)
         # ===================================Medicine used===============

        lblmedicine=Label(dataframeleft,font=("Arial",15),text="Medicine used      =",padx=2)
        lblmedicine.grid(column=0,row=4)
        txtmedicine=Entry(dataframeleft,font=("arial",14),width=35)
        txtmedicine.grid(column=1,row=4)
        # ===================================prescribed by==================================
        lblpres=Label(dataframeleft,font=("Arial",15),text="Prescribed by       =",padx=2)
        lblpres.grid(column=0,row=5)
        txtpres=Entry(dataframeleft,font=("arial",14),width=35)
        txtpres.grid(column=1,row=5)
        # ===========================Address of patient==========================================
        lbladdress=Label(dataframeleft,font=("Arial",15),text="Address of patient =",padx=2)
        lbladdress.grid(column=0,row=6)
        txtaddress=Entry(dataframeleft,font=("arial",14),width=35)
        txtaddress.grid(column=1,row=6)
         # ======================================================================
          # ===========================contact of patient==========================================
        lblcontact=Label(dataframeleft,font=("Arial",15),text="Contact of patient =",padx=2)
        lblcontact.grid(column=0,row=7)
        txtcontact=Entry(dataframeleft,font=("arial",14),width=35)
        txtcontact.grid(column=1,row=7)
         # ======================================================================
           # ===========================decription of disease==========================================
        lbldescri=Label(dataframeleft,font=("Arial",15),text="Description of disease =",padx=2)
        lbldescri.grid(column=0,row=8)
        txtdescri=Text(dataframeleft,font=("arial",14),width=35,height=50)
        txtdescri.grid(column=1,row=8)
         # ======================================================================
        btn1=Button(dataframedown,text=("presciption",))
        btn1.pack(side=LEFT,padx=2)
        btn2=Button(dataframedown,text=("next button",))
        btn2.pack(side=LEFT,padx=2)


        


root = Tk()
ob = hospital(root)
root.mainloop()
