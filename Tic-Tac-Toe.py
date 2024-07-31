from tkinter import *
from tkinter import messagebox
root= Tk()
root.title("Tic-Tac-Toe Game")

click=True
c=0
def disable_all_buttons():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)


def b_click(b):
    global click,c
    
    if b["text"]==" " and click==True:
        b["text"]="X"
        click=False
        c+=1
        won()
    elif b["text"]==" " and click==False:
        b["text"]="O"
        click=True
        c+=1
        won()
    else:
        messagebox.showerror("Can't do!")
        won()
def won():
    global win
    win = False
    #horizontal check

    if b1["text"]==b2["text"]==b3["text"] and b1["text"] != " ":
        win=True
        var=b1["text"]
       
        messagebox.showinfo(f"{var} won")
        disable_all_buttons()
        
    elif b4["text"]==b5["text"]==b6["text"] and b4["text"]!=" ":
        win=True
        var=b4["text"]
        messagebox.showinfo(f"{var} won")
        disable_all_buttons()       
    elif b7["text"]==b8["text"]==b9["text"] and b7["text"]!=" ":
        win=True
        var=b1["text"]
        messagebox.showinfo(f"{var} won")
        disable_all_buttons()

        #vertical check

    elif b1["text"]==b4["text"]==b7["text"] and b1["text"]!= " ":
        win=True
        var=b1["text"]
        messagebox.showinfo(f"{var} won")
        disable_all_buttons()
        
    elif b2["text"]==b5["text"]==b8["text"] and b2["text"] != " ":
        win=True
        var=b2["text"]
        messagebox.showinfo(f"{var} won")
        disable_all_buttons()
    elif b3["text"]==b6["text"]==b9["text"] and b3["text"] != " ":
        win=True
        var=b3["text"]
        messagebox.showinfo(f"{var} won")
        disable_all_buttons()
        
        #cross check
    elif b1["text"]==b5["text"]==b9["text"] and b1["text"] != " ":
        win=True
        var=b1["text"]
        messagebox.showinfo(f"{var} won")
        disable_all_buttons()
    elif b3["text"]==b5["text"]==b7["text"] and b3["text"] != " ":
        win=True
        var=b3["text"]
        messagebox.showinfo(f"{var} won")
        disable_all_buttons()
        

    


b1=Button(root,padx=40,pady=20,text=" ",font=("Helvetica",20),command=lambda:b_click(b1))
b1.grid(row=0,column=1)
b2=Button(root,padx=40,pady=20,text=" ",font=("Helvetica",20),command=lambda:b_click(b2))
b2.grid(row=0,column=2)
b3=Button(root,padx=40,pady=20,text=" ",font=("Helvetica",20),command=lambda:b_click(b3))
b3.grid(row=0,column=3)

b4=Button(root,padx=40,pady=20,text=" ",font=("Helvetica",20),command=lambda:b_click(b4))
b4.grid(row=1,column=1)
b5=Button(root,padx=40,pady=20,text=" ",font=("Helvetica",20),command=lambda:b_click(b5))
b5.grid(row=1,column=2)
b6=Button(root,padx=40,pady=20,text=" ",font=("Helvetica",20),command=lambda:b_click(b6))
b6.grid(row=1,column=3)

b7=Button(root,padx=40,pady=20,text=" ",font=("Helvetica",20),command=lambda:b_click(b7))
b7.grid(row=2,column=1)
b8=Button(root,padx=40,pady=20,text=" ",font=("Helvetica",20),command=lambda:b_click(b8))
b8.grid(row=2,column=2)
b9=Button(root,padx=40,pady=20,text=" ",font=("Helvetica",20),command=lambda:b_click(b9))
b9.grid(row=2,column=3)

root.mainloop()