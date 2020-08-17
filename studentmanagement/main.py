from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox
class Student:
    def __init__(self,root):
        self.root = root
        self.root.title("Student management system")
        self.root.geometry("1350x700+0+0")

        title = Label(self.root,text="Student management system",font=("times new roman",40,"bold"),bg="red",fg="yellow")
        title.pack(side=TOP,fill=X)


        #-----------variables--------------------

        self.Roll_no_var = StringVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.gender_var = StringVar()
        self.contact_var = StringVar()
        self.dob_var = StringVar()
        self.address_var = StringVar()

        self.search_by=StringVar()
        self.search_txt=StringVar()




        Manage_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        Manage_Frame.place(x=20,y=80,width=390,height=580)

        m_title = Label(Manage_Frame,text="Manage students",bg="crimson",fg="white",font=("times new roman",12))
        m_title.grid(row=0,columnspan=2,pady=20)

        lbl_roll = Label(Manage_Frame,text="Roll No.",bg="crimson",fg="white",font=("times new roman",15))
        lbl_roll.grid(row=1,column=1,pady=10,padx=20,sticky="w")
        txt_Roll = Entry(Manage_Frame,textvariable=self.Roll_no_var,font=("times new roman",15),bd=2)
        txt_Roll.grid(row=1,column=2,pady=10,padx=15,sticky="w")

        lbl_name = Label(Manage_Frame, text="Name", bg="crimson", fg="white", font=("times new roman", 15))
        lbl_name.grid(row=2, column=1, pady=10, padx=20, sticky="w")
        txt_name = Entry(Manage_Frame,textvariable=self.name_var, font=("times new roman", 15), bd=2)
        txt_name.grid(row=2, column=2, pady=10, padx=15, sticky="w")

        lbl_email = Label(Manage_Frame, text="Email", bg="crimson", fg="white", font=("times new roman", 15))
        lbl_email.grid(row=3, column=1, pady=10, padx=20, sticky="w")
        txt_email = Entry(Manage_Frame,textvariable=self.email_var, font=("times new roman", 15), bd=2)
        txt_email.grid(row=3, column=2, pady=10, padx=15, sticky="w")

        lbl_gender = Label(Manage_Frame, text="Gender", bg="crimson", fg="white", font=("times new roman", 15))
        lbl_gender.grid(row=4, column=1, pady=10, padx=20, sticky="w")
        combo_gender = ttk.Combobox(Manage_Frame,textvariable=self.gender_var,font=("times new roman",14),state="readonly")
        combo_gender['values']=("Male","Female")
        combo_gender.grid(row=4, column=2, pady=10,padx=20,  sticky="w")

        lbl_contact = Label(Manage_Frame, text="Contact", bg="crimson", fg="white", font=("times new roman", 15))
        lbl_contact.grid(row=5, column=1, pady=10, padx=20, sticky="w")
        txt_contact = Entry(Manage_Frame,textvariable=self.contact_var, font=("times new roman", 15), bd=2)
        txt_contact.grid(row=5, column=2, pady=10, padx=15, sticky="w")

        lbl_dob = Label(Manage_Frame, text="DOB", bg="crimson", fg="white", font=("times new roman", 15))
        lbl_dob.grid(row=6, column=1, pady=10, padx=20, sticky="w")
        txt_dob = Entry(Manage_Frame,textvariable=self.dob_var, font=("times new roman", 15), bd=2)
        txt_dob.grid(row=6, column=2, pady=10, padx=15, sticky="w")

        lbl_Address = Label(Manage_Frame, text="Address", bg="crimson", fg="white", font=("times new roman", 15))
        lbl_Address.grid(row=7, column=1, pady=10, padx=20, sticky="w")
        self.txt_Address = Text(Manage_Frame, width=20,height=5,font=("times new roman", 15), bd=2)
        self.txt_Address.grid(row=7, column=2, pady=10, padx=15, sticky="w")

        #------button frame-----------------------------------

        btn_Frame = Frame(Manage_Frame,bd=4,bg="crimson",relief=RIDGE)
        btn_Frame.place(x=10,y=500,width=300)

        Addbtn = Button(btn_Frame,command=self.add_students,text="Add",width=5).grid(row=0,column=0,padx=15,pady=10)
        Updatebtn = Button(btn_Frame,command=self.update_data, text="Update", width=5).grid(row=0,column=1,padx=15,pady=10)
        Deletebtn = Button(btn_Frame,command=self.delete_data,text="Delete", width=5).grid(row=0,column=2,padx=15,pady=10)
        Clearbtn = Button(btn_Frame,command=self.clear, text="Clear", width=5).grid(row=0,column=3,padx=15,pady=10)


        #--------detail frame-----------------------------------------------------

        Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
        Detail_Frame.place(x=490, y=80, width=800, height=560)

        lbl_search = Label(Detail_Frame,text="search by",bg="crimson",fg="white")
        lbl_search.grid(row=0,column=0,padx=10,pady=0,sticky="w")

        combo_search=ttk.Combobox(Detail_Frame,textvariable=self.search_by,width=10,state="readonly")
        combo_search['values'] = ("roll_no", "name", "contact")
        combo_search.grid(row=0,column=1,padx=10,pady=10)

        txt_search = Entry(Detail_Frame,textvariable=self.search_txt)
        txt_search.grid(row=0,column=2,padx=10,sticky="w")

        searchbtn = Button(Detail_Frame,text="search",command=self.search_data)
        searchbtn.grid(row=0,column=3,padx=10)

        showallbtn = Button(Detail_Frame, text="show all")
        showallbtn.grid(row=0, column=4,padx=10)

        #---------------table frame----------------------------------

        Table_Frame = Frame(Detail_Frame, bd=4, relief=RIDGE, bg="crimson")
        Table_Frame.place(x=10, y=80, width=770, height=460)

        scroll_x = Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)
        self.Student_table = ttk.Treeview(Table_Frame,columns=("roll","name","email","gender","contact","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.configure(command=self.Student_table.xview)
        scroll_y.configure(command=self.Student_table.yview)

        self.Student_table.heading("roll", text="Roll.no.")
        self.Student_table.heading("name", text="name")
        self.Student_table.heading("email", text="email")
        self.Student_table.heading("gender", text="gender")
        self.Student_table.heading("contact", text="contact")
        self.Student_table.heading("dob", text="dob")
        self.Student_table.heading("address", text="address")

        self.Student_table.column("roll",width=50)
        self.Student_table.column("name", width=100)
        self.Student_table.column("email", width=100)
        self.Student_table.column("gender", width=100)
        self.Student_table.column("contact", width=100)
        self.Student_table.column("dob", width=100)
        self.Student_table.column("address", width=100)

        self.Student_table['show']='headings'
        self.Student_table.pack(fill=BOTH,expand=1)

        #event bind
        self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)

        #function call
        self.fetch_data()

    def add_students(self):
        if self.Roll_no_var.get()=="":
            messagebox.showerror("error","all fields are required")
            return 0
        con = pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur = con.cursor()
        cur.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s)",(self.Roll_no_var.get(),
                                                                        self.name_var.get(),
                                                                        self.email_var.get(),
                                                                        self.gender_var.get(),
                                                                        self.contact_var.get(),
                                                                        self.dob_var.get(),
                                                                        self.txt_Address.get('1.0',END)))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()



    def fetch_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stm")
        cur = con.cursor()
        cur.execute("select * from student")
        rows=cur.fetchall()
        if(len(rows)!=0):
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
            con.commit()
        con.close()

    def clear(self):
        self.Roll_no_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.gender_var.set("")
        self.contact_var.set("")
        self.dob_var.set("")
        self.txt_Address.delete("0.0", END)  # column row

    def get_cursor(self,e):
        try:
            cursor_row = self.Student_table.focus()
            contents = self.Student_table.item(cursor_row)
            row=contents['values']
            #--may be one liner
            #content = self.Student_table.item(self.Student_table.focus())
            self.Roll_no_var.set(row[0])
            self.name_var.set(row[1])
            self.email_var.set(row[2])
            self.gender_var.set(row[3])
            self.contact_var.set(row[4])
            self.dob_var.set(row[5])

            self.txt_Address.delete("0.0",END)#column row
            self.txt_Address.insert(END,row[6])
        except:
            print(e)

    def update_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stm")
        cur = con.cursor()
        cur.execute("update student set name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where roll_no=%s", (
                                                                         self.name_var.get(),
                                                                         self.email_var.get(),
                                                                         self.gender_var.get(),
                                                                         self.contact_var.get(),
                                                                         self.dob_var.get(),
                                                                         self.txt_Address.get('1.0', END),
                                                                         self.Roll_no_var.get(),))
        con.commit()
        self.clear()
        self.fetch_data()
        con.close()

    def delete_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stm")
        cur = con.cursor()
        cur.execute("delete from student where roll_no=%s",self.Roll_no_var.get())

        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

    def search_data(self):
        self.Student_table.delete(*self.Student_table.get_children())
        con = pymysql.connect(host="localhost", user="root", password="", database="stm")
        cur = con.cursor()
        print(str(self.search_by.get()),str(self.search_txt.get()))
        print("select * from student where " + str(self.search_by.get()) + "='" + str(self.search_txt.get()) + "' ")
        cur.execute("select * from student where "+str(self.search_by.get())+"='"+str(self.search_txt.get())+"' ")
        rows=cur.fetchall()
        if(len(rows)!=0):
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
            con.commit()
        con.close()

root = Tk()
ob = Student(root)
root.mainloop()