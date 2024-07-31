from tkinter import *
root=Tk()
e=Entry(root,width=35,borderwidth=5)
e.grid(row=0,column=0,columnspan=4,padx=10,pady=10)
root.title("Calculator")

def button_click(num):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(num))

def mulbutton():
    fn=e.get()
    global f,operator
    f=int(fn)
    e.delete(0,END)
    operator="x"
def addbutton():
    fn=e.get()
    global f,operator
    f=int(fn)
    e.delete(0,END)
    operator="+"


def divbutton():
    fn=e.get()
    global f,operator
    f=int(fn)
    e.delete(0,END)
    operator="\u00F7"
  

def clearbutt():
    e.delete(0,END)

def subbutton():
    fn=e.get()
    global f ,operator
    f=int(fn)
    e.delete(0,END)
    operator="-"

def equalsign():
    sn = e.get()
    e.delete(0, END)
    if operator == "+":
        e.insert(0, f + int(sn))
    elif operator == "x":
        e.insert(0, f * int(sn))
    elif operator=="\u00F7":
        e.insert(0,f//int(sn))
    elif operator=="-":
        e.insert(0,f-int(sn))

button1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
addbutt=Button(root, text="+", padx=40, pady=20, command=addbutton)

cbutt=Button(root, text="C", padx=40, pady=20, command=clearbutt)
eqbutt=Button(root, text="=", padx=40, pady=20, command=equalsign)
mulbutt=Button(root, text="x", padx=40, pady=20, command=mulbutton)
divbutt=Button(root, text="\u00F7", padx=40, pady=20, command=divbutton)
subbutt=Button(root,text="-",padx=40,pady=20,command=subbutton)


#positions
button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)

button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)

button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)

button0.grid(row=4,column=0)
addbutt.grid(row=4,column=1)
cbutt.grid(row=4,column=2)
eqbutt.grid(row=4,column=3)
mulbutt.grid(row=2,column=3)
divbutt.grid(row=1,column=3)
subbutt.grid(row=3,column=3)
root.mainloop()