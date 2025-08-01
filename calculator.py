from tkinter import *



#important functions

def button1():
    textArea.insert(1.0,'1')
def button2():
    textArea.insert(1.0, '2')
def button3():
    textArea.insert(1.0, '3')
def button4():
    textArea.insert(1.0, '4')
def button5():
    textArea.insert(1.0, '5')
def button6():
    textArea.insert(1.0, '6')
def button7():
    textArea.insert(1.0, '7')
def button8():
    textArea.insert(1.0, '8')
def button9():
    textArea.insert(1.0, '9')
def button0():
    textArea.insert(1.0, '0')

def add():
    global result
    textArea.insert(1.0,'+')
    result = textArea.get(1.0,END)


def subs():
    textArea.insert(1.0, '-')
def multiply():
    textArea.insert(1.0, '*')
def devide():
    textArea.insert(1.0, '/')
def clear():
    textArea.delete(1.0, END)

def result():
    textArea_result.delete(1.0,END)
    textArea_result.insert(result)








root = Tk()
root.geometry('950x222')
root.title('calculator')
root.wm_iconbitmap()


#text area for the operation
textArea = Text(root,width='109',height='3',font='lucida 10 bold')
textArea.pack(expand=True,fill=BOTH)

#text area for result
textArea_result = Text(root,bg='grey',width='100',height='2',font='lucida 15 italic')
textArea_result.pack(expand=True,fill='y',pady='3')
Label(textArea_result,text='RESULT',anchor='w',font='lucida 30 italic').pack(side=LEFT)


# digits and symbols as BUTTONS
Button(root,text=1,command=button1,font='lucida 15 bold').pack(padx=2,side=LEFT)
Button(root,text=2,command=button2,font='lucida 15 bold').pack(padx=2,side=LEFT)
Button(root,text=3,command=button3,font='lucida 15 bold').pack(padx=2,side=LEFT)
Button(root,text=4,command=button4,font='lucida 15 bold').pack(padx=2,side=LEFT)
Button(root,text=5,command=button5,font='lucida 15 bold').pack(padx=2,side=LEFT)
Button(root,text=6,command=button6,font='lucida 15 bold').pack(padx=2,side=LEFT)
Button(root,text=7,command=button7,font='lucida 15 bold').pack(padx=2,side=LEFT)
Button(root,text=8,command=button8,font='lucida 15 bold').pack(padx=2,side=LEFT)
Button(root,text=9,command=button9,font='lucida 15 bold').pack(padx=2,side=LEFT)
Button(root,text=0,command=button0,font='lucida 15 bold').pack(padx=2,side=LEFT)
Button(root,text='+',command=add,font='lucida 15 bold').pack(padx=2,side=LEFT)
Button(root,text='-',command=subs,font='lucida 15 bold').pack(padx=2,side=LEFT)
Button(root,text='*',command=multiply,font='lucida 15 bold').pack(padx=2,side=LEFT)
Button(root,text='/',command=devide,font='lucida 15 bold').pack(padx=2,side=LEFT)
Button(root,text='=',command=result,font='lucida 22 bold').pack(padx=42,side=LEFT)
Button(root,text='CLEAR',command=clear,font='lucida 22 bold').pack(padx=2,side=LEFT)


root.mainloop()