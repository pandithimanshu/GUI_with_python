from tkinter import *

root= Tk()
root.geometry('1355x720')
root.title('snake water gun')



f = Frame(root,bg='orange',borderwidth=10,relief=SUNKEN)
f.pack()

welcome_note = Label(f,text='WELCOME TO SNAKE WATER GUN',font='Helvetica 20 bold',fg='pink')
welcome_note.pack()







root.mainloop()