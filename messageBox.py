import tkinter
import TkMessageBox

top = Tkinter.Tk()

def message_box():
  #  TkMessageBox.__init__(self, message_box())
    TkMessageBox.showinfo("Info pertaining to this program")

nft =Tkinter.Button(top, text ="what it does", command = message_box)

nft.pack()
top.mainloop()