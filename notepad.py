from tkinter import *
import tkinter.messagebox as tmsg
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os


# FUNCTIONS FOR OUR NOTEPAD

# functions of file menu
def newFile():
    global file
    root.title('untitled - NOTEPAD')
    file=None
    textArea.delete(1.0,END)

def openFile():
    global file
    file = askopenfilename(defaultextension='.txt',filetypes=[('All Files','*.*'),('Text Documents','*.txt')])
    if file=='':
        file=None
    else:
        FileName = os.path.basename(file)
        print(os.path.basename(FileName))
        root.title(f'{FileName} -NOTEPAD')
        textArea.delete(1.0,END)
        with open(file,'r') as f:
            textArea.insert(1.0,f.read())

def saveFile():
    global file
    # if file ==None:
    file =asksaveasfilename(initialfile ='untitled.txt',defaultextension='.txt',filetypes=[('All Files','*.*'),('Text Documents','*.txt')])
    if file=='':
        file=None
    else:
        #saving the file
        with open(file,'w') as f:
            f.write(textArea.get(1.0,END))

    # else:
    #     with open(file,'w') as f:
    #         f.write(textArea.get(1.0,END))
    root.title(f'{os.path.basename(file)} -NOTEPAD')

# functions of edit menu
def cut():
    textArea.event_generate("<<Cut>>")
def copy():
    textArea.event_generate(('<<Copy>>'))
def paste():
    textArea.event_generate(('<<Paste>>'))
def print():
    tmsg.showinfo('SORRY','''OUR TEAM IS WORKING ON THIS FUNCTION
                  !!! SORRY FOR DELAY !!!''')
def find():
    pass

# functions for help menu
def rateUs():
    tmsg.showinfo('THANKS FOR RATE','THANKS FOR RATING OUR PRODUCT '
                  )
    
def feedback():
    tmsg.showinfo('THANKS ','THANKS FOR FEEDBACK')
def aboutUs():
    tmsg.showinfo("ABOUT US",'A PRODUCT OF HIMANSHU SHARMA DIGITAL CORPORATION')


root = Tk()
root.geometry('600x800')
root.title('notepad by HIMANSHU SHARMA')
#root.wm_iconbitmap(r'../notepad.ico')
#root.configure(background='grey')


# creating menues :-
main_menu = Menu(root)
root.config(menu=main_menu) # to configure top menu in the root
file = Menu(main_menu,tearoff=0)
main_menu.add_cascade(label='FILE',menu=file) # to add a menu in the top menu
file.add_command(label ='new',command=newFile) # adding submenu named as new
file.add_command(label ='open',command=openFile)
file.add_command(label ='save',command=saveFile)
file.add_command(label ='save as')
file.add_command(label ='print',command = print)
file.add_separator() # to add a seperator line
file.add_command(label ='exit',command=root.destroy)
# file.add_command(label ='new') # adding submenu named as new
# file.add_command(label ='new') # adding submenu named as new
# file.add_command(label ='new') # adding submenu named as new
# file.add_command(label ='new') # adding submenu named as new
# file.add_command(label ='new') # adding submenu named as new

edit = Menu(main_menu)
main_menu.add_cascade(label='EDIT',menu=edit) # to add edit menu in the top menu
edit.add_command(label ='cut',command=cut) # adding submenu named as cut
edit.add_command(label ='copy',command=copy)
edit.add_command(label ='paste',command=paste)
edit.add_command(label ='find',command=find)


help = Menu(main_menu,tearoff=0)
main_menu.add_cascade(label='HELP',menu=help) # to add help menu in the top menu
help.add_command(label='rate us',command=rateUs)
help.add_command(label = 'give feedback',command=feedback)
help.add_command(label ='about us',command=aboutUs)


scrollBar=Scrollbar(root)
scrollBar.pack(side=RIGHT,fill='y')

textArea=Text(root,bg='grey',font="lucida 10 bold",yscrollcommand=scrollBar.set)
textArea.pack(expand=True,fill=BOTH)

scrollBar.config(command=textArea.yview)








root.mainloop()
