from ctypes import resize
from tkinter import Button
from turtle import home


def login(event=none):
    Database()
    if username.get()== "" or password.get()== "":
        lb_text.config(text="Please complete the required fields below", fg=red)
    else:
        cursor.execute(SELECT * FROM 'memebers' WHERE 'username'=? AND 'password'=?)
        if cursor.fetchone() is None:
            HomeWindow()
            username.set("")
            password.set("")
            ln_text.config(text="", fg=)
        else:
            lb_text.config(text="Invalid entry", fg=red)
            username.set("")
            password.set("")
        cursor.close()
        connection.close()
    
def home_window():
    global home_window
    root.withdraw()
    home_window= toplevel(home_window.title("Python login")height = 600, width=600  )
    screenwidth= toplevel(screenwidth.title("Screen width")height = 600, width=600  )
    x = (screenwidth/2)-(width/2)
    y = (screenwidth/2)-(height/2)
    root.resizable(0,0)
    home_windowgeometry("%dx%d%dx%d" % (width, height, x,y))
    lb_login = label(home, text="sucessful", font=('ink free', 20 ).pack)
    btn_back = Button(home, text='Back', command=back).pack(pady=20,fill=x)

def Back():
    Home.destroy()
    root.deiconify()
    #initializing save as index.py
