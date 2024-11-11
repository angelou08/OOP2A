Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
... Type "help", "copyright", "credits" or "license()" for more information.
... >>> from tkinter import*
... ... import sqlite3
... ... 
... ... root=Tk()
... ... root.title('My CRUD project')
... ... root.geometry('500x500')
... ... 
... ... conn=sqlite3.connect('data.db')
... ... 
... ... c=conn.cursor()
... ... 
... ... '''
... ... 
... ... c.execute("""CREATE TABLE "myInfo" (
... ... 	"f_name"	TEXT,
... ... 	"l_name"	TEXT,
... ... 	"age"	INTEGER,
... ... 	"address"	TEXT,
... ... 	"email"	TEXT
... ... )""")
... ... 
... ... '''
... ... 
... ... 
... ... f_name=Entry(root,width=30)
... ... f_name.grid(row=0,column=1,padx=20)
... ... l_name=Entry(root,width=30)
... ... l_name.grid(row=1,column=1,padx=20)
... ... age=Entry(root,width=30)
... ... age.grid(row=2,column=1,padx=20)
... ... address=Entry(root,width=30)
... ... address.grid(row=3,column=1,padx=20)
... ... email=Entry(root,width=30)
... ... email.grid(row=4,column=1,padx=20)
... ... 
... ... f_name_label=Label(root,text="First Name")
... ... f_name_label.grid(row=0,column=0)
... I_name_label=Label(root,text="Last Name")
... I_name_label.grid(row=1,column=0)
... age_label-Label(root,text="Age")
... age_label.grid(row=2,column=0)
... address_label=Label(root,text="Address")
... address_label.grid(row=3,column=0)
... email_label=Label(root,text="email")
... email_label.grid(row=4,column=0)
