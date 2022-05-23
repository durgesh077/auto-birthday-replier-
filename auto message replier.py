from tkinter import *
import tkinter.messagebox as msg
import GUI
import time
def closer(event):
    #msg.showinfo('info', 'Auto replier has been stopped')
    quit()
    GUI.close()
def hideMe(event):
    #msg.showinfo('info', 'Auto replier has been started')
    event.widget.pack_forget()
    closeBt = Button(root, text="close", bg='red')
    closeBt.pack(fill="both")
    closeBt.bind('<Button-1>',closer)
    GUI.starter()
root=Tk()
root.title("auto reply Birth-Days")
#root.iconbitmap("whatsapp.ico")
root.configure()
root.geometry("33x33+1100+107")
start=None
b1=Button(root,text='start',activebackground='red',bg='blue')
b1.pack(fill="both")  
b1.bind('<Button-1>',hideMe)
root.mainloop()
