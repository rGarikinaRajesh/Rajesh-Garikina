import tkinter as tk
from tkinter import *
#import tkinter.font as tkFont
import string
from collections import Counter
a=0
def Reset():
    E5.set("")
    E6.set("")
    E7.set("")
    l3.destroy()
    return True
def Goodluck():
    flag,c=0,0
    global a
    global l3
    string1=''.join((E5.get()).split())
    string2=''.join((E6.get()).split())
    l3=tk.Label(root,text="Error : please enter valid names",font="Times 16 bold",fg="RED")
    if(any(i in string.digits for i in string1) or any(i in string.punctuation for i in string1)):
        l3.place(x=600,y=100)
        flag=1
        a=1
        c=1
    elif(any(i in string.digits for i in string2) or any(i in string.punctuation for i in string2)):
        l3.place(x=600,y=100)
        flag=1
        a=1
        c=1
    if(flag==0):
        lis=list(dict(Counter(list(string1.upper()+"LOVES"+string2.upper()))).values())
        while(len(lis)!=2):
            val=str(lis[0]+lis[-1])
            while(1):
                if len(val)>=2:
                    val=str(sum(map(int,list(val))))
                else:
                    break
            lis[0]=int(val)
            lis.pop(-1)
        string3=''.join(map(str,lis))
        E7.set(string3)
    return True
root=tk.Tk()
root.title("Love Calculator")
root.geometry("450x300")
text=tk.Text(root)
l1=tk.Label(root,text="Dream without fear love without limits",font="Times 16 bold underline",fg="green",pady=1,anchor=N)
#fontStyle = tkFont.Font(family="Helvitica",size=10)
first_person=tk.Label(root,text="YOUR NAME",font=("Arial Bold",10))
first_person.place(x=600,y=200)
second_person=tk.Label(root,text="YOUR FRIEND",font=("Arial Bold",10))
second_person.place(x=600,y=300)
E5=tk.StringVar()
E1=tk.Entry(root,bd=5,textvariable=E5,font=("Calibri",10))
E1.place(x=700,y=200)
E6=tk.StringVar()
E2=tk.Entry(root,bd=5,textvariable=E6,font=("Calibri",10))
E2.place(x=700,y=300)
B1=tk.Button(root,text="Good luck",anchor=S,command=Goodluck)
B1.place(x=650,y=400)
B2=tk.Button(root,text="Reset",anchor=S,command=Reset)
B2.place(x=800,y=400)
E7=tk.StringVar()
E3=tk.Entry(root,bd=5,font=("Calibri",50),fg="Red",bg="Yellow",state=DISABLED,textvariable=E7)
E3.place(x=1000,y=250,width=150,height=80)
l1.pack()
root.mainloop()

