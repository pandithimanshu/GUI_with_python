from tkinter import *



def clicker(event):
    global value
    text = event.widget.cget("text")
    print(text)
    if text=='CLEAR':
        value.set('')
        entry.update()

    elif text=='=':
        try:
            value.set(eval(entry.get()))
            entry.update()
        except Exception as e:
            value.set('dhang m likh l')
            entry.update()
            print(e)
    else:
        value.set(value.get()+text)
        entry.update()





root = Tk()
root.geometry('250x620')
root.minsize(width=250,height=620)
root.title('calculator')
root.wm_iconbitmap('../notepad.ico')
value =StringVar()
value.set('')
entry = Entry(root,textvar=value,font='lucida 20 bold')
entry.pack(fill=BOTH,pady=5,ipady=8)



# def button(digit_loop):
#     f = Frame(root,bg='grey')
#     f.pack()
#     for digit in digit_loop:
#         if len(str(digit))>2:
#             b = Button(f, text=digit, font='lucida 13 bold')
#             b.pack(side=LEFT,padx=7,pady=7)
#             b.bind("<Button-1>",clicker)
#         else:
#             b=Button(f,text=digit,font='lucida 25 bold',command=clicker)
#             b.pack(side=LEFT,padx=7,pady=7)
#             b.bind("<Button-1>",clicker)

f = Frame(root,bg='grey')
f.pack(pady=5)
b = Button(f, text='9', font='lucida 20 bold',relief=SUNKEN)
b.pack(side=LEFT,padx=7,pady=7)
b.bind("<Button-1>",clicker)

b = Button(f, text='8', font='lucida 20 bold')
b.pack(side=LEFT,padx=7,pady=7)
b.bind("<Button-1>",clicker)

b = Button(f, text='7', font='lucida 20 bold')
b.pack(side=LEFT,padx=7,pady=7)
b.bind("<Button-1>",clicker)


f = Frame(root,bg='grey')
f.pack(pady=5)
b = Button(f, text='6', font='lucida 20 bold')
b.pack(side=LEFT,padx=7,pady=7)
b.bind("<Button-1>",clicker)

b = Button(f, text='5', font='lucida 20 bold')
b.pack(side=LEFT,padx=7,pady=7)
b.bind("<Button-1>",clicker)

b = Button(f, text='4', font='lucida 20 bold')
b.pack(side=LEFT,padx=7,pady=7)
b.bind("<Button-1>",clicker)


f = Frame(root,bg='grey')
f.pack(pady=5)
b = Button(f, text='3', font='lucida 20 bold')
b.pack(side=LEFT,padx=7,pady=7)
b.bind("<Button-1>",clicker)

b = Button(f, text='2', font='lucida 20 bold')
b.pack(side=LEFT,padx=7,pady=7)
b.bind("<Button-1>",clicker)

b = Button(f, text='1', font='lucida 20 bold')
b.pack(side=LEFT,padx=7,pady=7)
b.bind("<Button-1>",clicker)




f = Frame(root,bg='grey')
f.pack(pady=5)
b = Button(f, text='=', font='lucida 21 bold')
b.pack(side=LEFT,padx=7,pady=7)
b.bind("<Button-1>",clicker)

b = Button(f, text='-', font='lucida 21 bold')
b.pack(side=LEFT,padx=7,pady=7)
b.bind("<Button-1>",clicker)

b = Button(f, text='+', font='lucida 21 bold')
b.pack(side=LEFT,padx=7,pady=7)
b.bind("<Button-1>",clicker)


f = Frame(root,bg='grey')
f.pack(pady=5)
b = Button(f, text='*', font='lucida 25 bold')
b.pack(side=LEFT,padx=7,pady=7)
b.bind("<Button-1>",clicker)

b = Button(f, text='/', font='lucida 25 bold')
b.pack(side=LEFT,padx=7,pady=7)
b.bind("<Button-1>",clicker)

b = Button(f, text='.', font='lucida 25 bold')
b.pack(side=LEFT,padx=7,pady=7)
b.bind("<Button-1>",clicker)



f = Frame(root,bg='grey')
f.pack(pady=5)

b = Button(f,text='%', font='lucida 20 bold')
b.pack(side=LEFT,padx=7,pady=7)
b.bind("<Button-1>",clicker)

b = Button(f, text='CLEAR', font='lucida 22 bold')
b.pack(side=LEFT,padx=7,pady=7)
b.bind("<Button-1>",clicker)

# f = Frame(root,bg='grey')
# f.pack()
# for digit in [9,8,7]:
#     b = Button(f,text=digit)
#     b.pack(side=LEFT)
#
#
# f = Frame(root,bg='grey')
# f.pack()
#
# for digit in [6,5,4]:
#     b = Button(f,text =digit)
#     b.pack(side=LEFT)
#
# f = Frame(root,bg='grey')
# f.pack()
#
# for digit in [3,2,1]:
#     b=Button(f,text=digit)
#     b.pack(side=LEFT)
#
# f = Frame(root,bg='grey')
# f.pack()
# for digit in ['clear','=','.']:
#     b=Button(f,text=digit)
#     b.pack(side=LEFT)




root.mainloop()