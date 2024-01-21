import sqlite3
from tkinter import *
root=Tk()
root.title("Customer Database")
conn=sqlite3.connect('address_book.db')
cur=conn.cursor()
'''cur.execute("""CREATE TABLE customerinfo(
First_Name text,
Last_Name text,
Address text,
Customerid int,
Phone int
)""")'''
#submit function
def submit():
    #append entries to table
    conn=sqlite3.connect("address_book.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO customerinfo VALUES(:f1, :f2, :f3, :f4, :f5)",
                {
                    'f1':fname.get(),
                    'f2':sname.get(),
                    'f3':add.get(),
                    'f4':cid.get(),
                    'f5':cid.get()
                    
                })
    conn.commit()
    conn.close()


    #clear the entries so new entries can be entered
    fname.delete(0,END)
    sname.delete(0,END)
    add.delete(0,END)
    cid.delete(0,END)
    phone.delete(0,END)

def query():
    conn=sqlite3.connect("address_book.db")
    #cursor
    cur=conn.cursor()
    cur.execute("SELECT *,oid FROM customerinfo")
    rows=cur.fetchall()
    print(rows)
    pr=""
    for row in rows:
        pr+=str(row)+"\n"
    ql=Label(root,text=pr)
    ql.grid(row=8,column=0,columnspan=2)

    #commit
    conn.commit()
    conn.close()
def delt():
    try:
         conn=sqlite3.connect("address_book.db")
         cur=conn.cursor()
         search=delentry.get()
         cur.execute("DELETE FROM customerinfo where Customerid=:var",{'var':search})
         conn.commit()
         conn.close()
    except Exception:
        print("record not found")
    

    


# setting labels
fnl=Label(root,text="First Name")
fnl.grid(row=0,column=0)
snl=Label(root,text="Second Name")
snl.grid(row=1,column=0)
al=Label(root,text="Address")
al.grid(row=2,column=0)
cidl=Label(root,text="Customerid number")
cidl.grid(row=3,column=0)
pl=Label(root,text="Phone Number")
pl.grid(row=4,column=0)
#label entry -> format
# setting entries adjacent to labels
fname=Entry(root,width=30)
fname.grid(row=0,column=1)
sname=Entry(root,width=30)
sname.grid(row=1,column=1)
add=Entry(root,width=30)
add.grid(row=2,column=1)
cid=Entry(root,width=30)
cid.grid(row=3,column=1)
phone=Entry(root,width=30)
phone.grid(row=4,column=1)
delentry=Entry(root,width=30)
delentry.grid(row=9,column=1)


submitbutton=Button(root,text="Add record",command=submit)
submitbutton.grid(row=6,column=1,padx=57,pady=8.5)
qbutton=Button(root,text="Show database",command=query)
qbutton.grid(row=7,column=1,padx=17,pady=8.5)
delbutton=Button(root,text="Delete Record",command=delt)
delbutton.grid(row=10,column=1,padx=17,pady=8.5)


conn.commit()
conn.close()
root.mainloop()
