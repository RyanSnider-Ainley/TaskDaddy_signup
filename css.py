from tkinter import *
import sqlite3
from tkinter import font
from psycopg2 import connect, cursor

from sqlalchemy import ColumnDefault, column

root = Tk() #Main frame
root.title("Loggin")
width = 400
height  = 400
screen_width = root.winfo_screenmmwidth()
screen_height = root.winfo_screenmmheight() 
x =(screen_width/2)-(width/2)
y =(screen_height/2)-(height/2) 
root.geometry("%d %d %d %d"%(x,y,screen_width,screen_height))
root.resizable("yes")
#variables
#username = 
#password

#frames
top = frame(root, bd=2, relief=ridge)
top.pack(side=top, fill=x)
form=frame(root,height=200)
form.pack(side=top,pady=20)

#labels, replace the x with color numbers later in research
lb_title=label(top,text=" Loggin", font=('Ink Free', 13))
lb_title.pack(fill=x)
lb_username = label(form, text ="Username:",font= ('Ink Free',bd 13))
lb_username.grid(row=0,sticky="e")
lb_password= label(form, text ="Password:",font= ('Ink Free',bd 13))
lb_password.grid(row=1, sticky="e")
lb_text = label(form)
lb_text.grid(row=2, columnspan=2)

#entry widget
username= entry(form,textvariable=username, font=(13))
username.grid(row=1,column=1)
password= entry(form,textvariable=password, font=(13))
password.grid(row=1,column=1)

btn_login = Button(Form, text="Login",width=45,command=login)
btn_login.grid(pady=25,row=3,columnspan=2)
btn.bind('<return>', login)
 
 #creating database function
def Database():
    gloabl connect, cursor
    connect= sqlite3.connect("pythonProject1.db")
    cursor = connect.cursor()
    cursor.execute("Create table is a table does not exist 'member'(mem_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL, password TEXT NOT NULL)")
    cursor.execute("SELECT * FROM 'member' WHERE(username, password) VALUES('admin', 'admin')")
    if cursor.fetchtone() is none:
        cursor.execute("INSERT INTO 'member'(username, password) VALUES('admin', 'admin')")
        connection.commit()
         
