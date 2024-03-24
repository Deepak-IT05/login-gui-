from tkinter import*
from tkinter import messagebox
a=Tk()  
a.title("my application")
a.geometry('300x300')
m=[]
def process():
    x=e1.get()
    y=e2.get()
    z=e3.get()
    m=[x,y,z]
    messagebox.showinfo("the data",m)
f1=Frame(a,padx=5,pady=5)
f1.grid(row=0,column=5)
l1=Label(f1,text='name',padx=10,pady=10).pack()
l2=Label(f1,text='email',padx=10,pady=10).pack()
l3=Label(f1,text='password',padx=10,pady=10).pack()
f2=Frame(a,padx=10,pady=10)
f2.grid(row=0,column=7)
e1=Entry(f2)
e1.pack(padx=10,pady=10)
e2=Entry(f2)
e2.pack(padx=10,pady=10)
e3=Entry(f2)
e3.pack(padx=10,pady=10)
b=Button(a,text='submit',command=process,padx=10).grid(row=1,columnspan=10,pady=30)
a.mainloop()