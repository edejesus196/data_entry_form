from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import pymysql
import random
import time

class DataEntryForm:

    def __init__(self, root):
        self.root = root
        self.root.title = ("Data Entry Form")
        self.root.geometry("1350x750+0+0")
        self.root.configure(background="gainsboro")

        RefNo = StringVar()
        Firstname = StringVar()
        Surname = StringVar()
        Address = StringVar()
        Telephone = StringVar()
        RegDate = StringVar()
        ProveID = StringVar()
        CurrentDate = StringVar()
        MemberType = StringVar()
        MemberFee = StringVar()
        DateToDay = StringVar()
        Search = StringVar()

        MainFrame = Frame(self.root, bd =10, width=1350, height = 700, relief=RIDGE)
        MainFrame.grid()

        TopFrame1 = Frame(MainFrame, bd =5, width=1340, height = 200, relief=RIDGE, bg = 'cadet blue')
        TopFrame1.grid(row=0, column=0)
        TopFrame2 = Frame(MainFrame, bd =5, width=1340, height = 50, relief=RIDGE, bg= 'cadet blue')
        TopFrame2.grid(row=1, column=0)
        TopFrame3 = Frame(MainFrame, bd =5, width=1340, height = 300, relief=RIDGE, bg= 'cadet blue')
        TopFrame3.grid(row=2, column=0)

        InnerTopFrame1 = Frame(TopFrame1, bd =5, width=1340, height = 190, relief=RIDGE)
        InnerTopFrame1.grid()
        InnerTopFrame2 = Frame(TopFrame2, bd =5, width=1340, height = 48, relief=RIDGE)
        InnerTopFrame2.grid()
        InnerTopFrame3 = Frame(TopFrame3, bd =5, width=1340, height = 280, relief=RIDGE)
        InnerTopFrame3.grid()

        RegDate.set(time.strftime("%m/%d/%y"))
        DateToDay.set(time.strftime("%m/%d/%y"))

        def Reset():
            RefNo.set("")
            Firstname.set("")
            Surname.set("")
            Address.set("")
            Telephone.set("")
            RegDate.set("")
            ProveID.set("")
            CurrentDate.set("")
            MemberType.set("")
            MemberFee.set("")
            Search.set("")
            DateToDay.set("")

            RegDate.set(time.strftime("%m/%d/%y"))
            DateToDay.set(time.strftime("%m/%d/%y"))

        def iExit():
            iExit = tkinter.messagebox.askyesno("Data Entry Form", "Do you want to exit?")
            if iExit > 0:
                root.destroy()
                return

        def addData():
            if RefNo.get() == "" or Firstname.get()=="" or  Surname.get()=="":
                tkinter.messagebox.showerror("Data Entry Form", "Enter Correct Details")
            else:
                sqlCon = pymysql.connect(host="localhost", user="root", password="edjrotn10468", database="data_entry")
                cur = sqlCon.cursor()
                cur.execute("insert into data_entry values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                RefNo.get(),
                Firstname.get(),
                Surname.get(),
                Address.get(),
                Telephone.get(),
                RegDate.get(),
                ProveID.get(),
                CurrentDate.get(),
                MemberType.get(),
                MemberFee.get()))

                sqlCon.commit()
                DisplayData()
                sqlCon.close()
                tkinter.messagebox.showinfo("Data Entry Form", "Record Entered to Database")

        def DisplayData():
            sqlCon = pymysql.connect(host="localhost", user="root", password="edjrotn10468", database="data_entry")
            cur = sqlCon.cursor()
            cur.execute("select * from data_entry")
            result = cur.fetchall()
            if len(result) !=0:
                tree_records.delete(*tree_records.get_children())
                for row in result:
                    tree_records.insert('', 'end',values = row)
                    sqlCon.commit()
                sqlCon.close()


        def LearnersInfo(ev):
            viewinfo = tree_records.focus()
            learnerData = tree_records.item(viewinfo)
            row = learnerData ['values']
            RefNo.set(row[0])
            Firstname.set(row[1])
            Surname.set(row[2])
            Address.set(row[3])
            Telephone.set(row[4])
            RegDate.set(row[5])
            ProveID.set(row[6])
            CurrentDate.set(row[7])
            MemberType.set(row[8])
            MemberFee.set(row[9])

        def update():
            sqlCon = pymysql.connect(host="localhost", user="root", password="edjrotn10468", database="data_entry")
            cur = sqlCon.cursor()
            cur.execute("update data_entry set Firstname = %s,Surname = %s, Address = %s, Telephone = %s, RegDate = %s, \
            ProveID=%s, CurrentDate=%s, MemberType=%s, MemberFee=%s where RefNo=%s",(


            Firstname.get(),
            Surname.get(),
            Address.get(),
            Telephone.get(),
            RegDate.get(),
            ProveID.get(),
            CurrentDate.get(),
            MemberType.get(),
            MemberFee.get(),
            RefNo.get()))

            sqlCon.commit()
            DisplayData()
            sqlCon.close()
            tkinter.messagebox.showinfo("Data Entry Form", "Record Successfully Updated")

        def deleteDB():
            sqlCon = pymysql.connect(host="localhost", user="root", password="edjrotn10468", database="data_entry")
            cur = sqlCon.cursor()
            cur.execute("delete from data_entry where RefNo=%s", RefNo.get())

            sqlCon.commit()
            DisplayData()
            sqlCon.close()
            tkinter.messagebox.showinfo("Data Entry Form", "Record Successfully Deleted")

        def searchDB():

            try:

                sqlCon = pymysql.connect(host="localhost", user="root", password="edjrotn10468", database="data_entry")
                cur = sqlCon.cursor()
                cur.execute("select * from data_entry where RefNo='%s'"%Search.get())

                row = cur.fetchone()

                RefNo.set(row[0])
                Firstname.set(row[1])
                Surname.set(row[2])
                Address.set(row[3])
                Telephone.set(row[4])
                RegDate.set(row[5])
                ProveID.set(row[6])
                CurrentDate.set(row[7])
                MemberType.set(row[8])
                MemberFee.set(row[9])

                sqlCon.commit()

            except:


                tkinter.messagebox.showinfo("Data Entry Form", "No Such Records Found")
                Reset()
            sqlCon.close()
            Search.set("")



#========================================Widget======================================================================

        IblReference = Label(InnerTopFrame1, font = ('arial', 12, 'bold'), text = "Reference No", bd=10)
        IblReference.grid(row=0, column=0, sticky='w')
        txtReference = Entry(InnerTopFrame1, font = ('arial', 12, 'bold'), bd=5, width=32, justify='left', textvariable=RefNo)
        txtReference.grid(row=0, column=1)

        IblFirstname = Label(InnerTopFrame1, font = ('arial', 12, 'bold'), text = "Firstname", bd=10)
        IblFirstname.grid(row=1, column=0, sticky='w')
        txtFirstname = Entry(InnerTopFrame1, font = ('arial', 12, 'bold'), bd=5, width=32, justify='left', textvariable=Firstname)
        txtFirstname.grid(row=1, column=1)

        IblSurname = Label(InnerTopFrame1, font = ('arial', 12, 'bold'), text = "Surname", bd=10)
        IblSurname.grid(row=2, column=0, sticky='w')
        txtSurname = Entry(InnerTopFrame1, font = ('arial', 12, 'bold'), bd=5, width=32, justify='left', textvariable=Surname)
        txtSurname.grid(row=2, column=1)

        self.IblAddress = Label(InnerTopFrame1, font = ('font', 12, 'bold'), text = "Address", bd=10)
        self.IblAddress.grid(row=3, column=0, sticky='w')
        self.txtAddress = Entry(InnerTopFrame1, font = ('font', 12, 'bold'), bd=5, width=83, justify='left', textvariable=Address)
        self.txtAddress.grid(row=3, column=1, columnspan=3)


        self.IblTelephone = Label(InnerTopFrame1, font = ('font', 12, 'bold'), text = "Telephone", bd=10)
        self.IblTelephone.grid(row=0, column=2, sticky='w')
        self.txtTelephone = Entry(InnerTopFrame1, font = ('font', 12, 'bold'), bd=5, width=32, justify='left', textvariable=Telephone)
        self.txtTelephone.grid(row=0, column=3)

        self.IblRegistrationDate = Label(InnerTopFrame1, font = ('font', 12, 'bold'), text = "Registration Date", bd=10)
        self.IblRegistrationDate.grid(row=1, column=2, sticky='w')
        self.txtRegistrationDate = Entry(InnerTopFrame1, font = ('font', 12, 'bold'), bd=5, width=32, justify='left', textvariable=RegDate)
        self.txtRegistrationDate.grid(row=1, column=3)

        self.IblProveID = Label(InnerTopFrame1, font = ('font', 12, 'bold'), text = "Prove of ID", bd=10)
        self.IblProveID.grid(row=2, column=2, sticky='w')

        self.cboProveOfID = ttk.Combobox(InnerTopFrame1, font=('font', 12, 'bold'), width=31, textvariable=ProveID)
        self.cboProveOfID['value'] = ('', 'Pilot Licence', 'Driving License', 'Student ID', 'Passport')
        self.cboProveOfID.current(0)
        self.cboProveOfID.grid(row=2, column=3)

        self.IblSearch = Label(InnerTopFrame1, font = ('font', 12, 'bold'), text = "Search", bd=10)
        self.IblSearch.grid(row=0, column=4, sticky='w')
        self.txtSearch = Entry(InnerTopFrame1, font = ('font', 12, 'bold'), bd=5, width=33, justify='left', textvariable=Search)
        self.txtSearch.grid(row=0, column=5)

        self.IblDate = Label(InnerTopFrame1, font = ('font', 12, 'bold'), text = "Date", bd=10)
        self.IblDate.grid(row=1, column=4, sticky='w')
        self.txtDate = Entry(InnerTopFrame1, font = ('font', 12, 'bold'), bd=5, width=33, justify='left', textvariable=DateToDay)
        self.txtDate.grid(row=1, column=5)

        self.IblMemberType = Label(InnerTopFrame1, font = ('font', 12, 'bold'), text = "Member Type", bd=10)
        self.IblMemberType.grid(row=2, column=4, sticky='w')

        self.cboMemberType = ttk.Combobox(InnerTopFrame1, font=('font', 12, 'bold'), width=31, textvariable=MemberType)
        self.cboMemberType['value'] = ('', 'Annual', 'Quarterly', 'Monthly', 'Weekly')
        self.cboMemberType.current(0)
        self.cboMemberType.grid(row=2, column=5)

        self.IblMemberFee = Label(InnerTopFrame1, font = ('font', 12, 'bold'), text = "Member Fee", bd=10)
        self.IblMemberFee.grid(row=3, column=4, sticky='w')

        self.cboMemberFee = ttk.Combobox(InnerTopFrame1, font=('font', 12, 'bold'), width=31, textvariable=MemberFee)
        self.cboMemberFee['value'] = ('', '$150.00', '$37.00', '$12.5', '$2.89')
        self.cboMemberFee.current(0)
        self.cboMemberFee.grid(row=3, column=5)


        #====================================================================================================

        scroll_x=Scrollbar(InnerTopFrame3, orient = HORIZONTAL)
        scroll_y=Scrollbar(InnerTopFrame3, orient = VERTICAL)

        tree_records = ttk.Treeview(InnerTopFrame3, height = 13, columns = ("RefNo", "Firstname", "Surname", "Address", "Telephone",
        "RegDate", "ProveID", "CurrentDate", "MemberType", "MemberFee"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side = BOTTOM, fill=X)
        scroll_y.pack(side = RIGHT, fill=Y)

        tree_records.heading("RefNo", text = "ReferenceNo.")
        tree_records.heading("Firstname", text = "Firstname")
        tree_records.heading("Surname", text = "Surname")
        tree_records.heading("Address", text = "Address")
        tree_records.heading("Telephone", text = "Telephone")
        tree_records.heading("RegDate", text = "RegDate")
        tree_records.heading("ProveID", text = "ProveID")
        tree_records.heading("CurrentDate", text = "CurrentDate")
        tree_records.heading("MemberType", text = "MemberType")
        tree_records.heading("MemberFee", text = "MemberFee")

        tree_records['show'] = 'headings'

        tree_records.column("RefNo", width=100)
        tree_records.column("Firstname", width=150)
        tree_records.column("Surname", width=150)
        tree_records.column("Address", width=252)
        tree_records.column("Telephone", width=100)
        tree_records.column("RegDate", width=100)
        tree_records.column("ProveID", width=100)
        tree_records.column("CurrentDate", width=100)
        tree_records.column("MemberType", width=150)
        tree_records.column("MemberFee", width=100)

        tree_records.pack(fill = 'both', expand=1)
        tree_records.bind("<ButtonRelease-1>",LearnersInfo)
        DisplayData()

         #========================================Buttons=========================================================

        self.btnAddNew = Button (InnerTopFrame2, pady=1, bd=4, font=('font', 16, 'bold'), width=13, text="Add New", command=addData)
        self.btnAddNew.grid(row=0, column=0, padx=3)

        self.btnDisplay = Button (InnerTopFrame2, pady=1, bd=4, font=('font', 16, 'bold'), width=13, text="Diplay", command=DisplayData)
        self.btnDisplay.grid(row=0, column=1, padx=3)

        self.btnUpdate = Button (InnerTopFrame2, pady=1, bd=4, font=('font', 16, 'bold'), width=13, text="Update", command=update)
        self.btnUpdate.grid(row=0, column=2, padx=3)

        self.btnDelete = Button (InnerTopFrame2, pady=1, bd=4, font=('font', 16, 'bold'), width=13, text="Delete", command=deleteDB)
        self.btnDelete.grid(row=0, column=3, padx=3)

        self.btnReset = Button (InnerTopFrame2, pady=1, bd=4, font=('font', 16, 'bold'), width=13, text="Reset", command = Reset)
        self.btnReset.grid(row=0, column=4, padx=3)

        self.btnExit = Button (InnerTopFrame2, pady=1, bd=4, font=('font', 16, 'bold'), width=13, text="Exit", command=iExit)
        self.btnExit.grid(row=0, column=5, padx=3)

        self.btnSearch = Button (InnerTopFrame2, pady=1, bd=4, font=('font', 16, 'bold'), width=13, text="Search", command=searchDB)
        self.btnSearch.grid(row=0, column=6, padx=3)






if __name__=='__main__':
    root = Tk()
    application = DataEntryForm(root)
    root.mainloop()
