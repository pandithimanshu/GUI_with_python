from tkinter import *

root = Tk()

root.title('passwords saver')
root.geometry('450x150')
root.minsize(333,150)
def saver():
    with open('pass.txt','a') as txt:
        txt.write(f'website = {input1.get()}  password = {input2.get()}\n')
    #l2= Label(text='password')
    #l2.grid(row=33,column=34)
#f1 = Frame(root,bg='grey')
#f1.grid(padx=40,pady=40)
l1= Label(root,text='WEBSITE NAME    :')
l1.grid(row=5,column=5)
website = StringVar
input1 = Entry(root,textvariable=website)
input1.grid(row=5,column=7)
l2 =Label(root,text='PASSWORD :')
l2.grid(row=7,column=5)
password = StringVar
input2 = Entry(root,textvariable = password)
input2.grid(row=7,column=7)
submit_b = Button(root,text='submit',command=saver,bg='yellow')
submit_b.grid(row = 20, column= 10)



root.mainloop()
