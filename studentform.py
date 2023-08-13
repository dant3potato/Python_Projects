from tkinter import *
root = Tk()
root.geometry("300x200")
root.title("Student Form")
Label(root,text="Student form",font=10).grid(row=0,column=2)

# label of name, class , roll, school
name=Label(root,text="Name").grid(row=1,column=0)
cla=Label(root,text="Class").grid(row=2,column=0)
roll=Label(root,text="Roll No").grid(row=3,column=0)
sch=Label(root,text="school").grid(row=4,column=0)

#taking entery in the strig form
namestr=StringVar
clastr=StringVar
rollstr=StringVar
schstr=StringVar
nameent=Entry(root,textvariable=namestr).grid(row=1,column=2)
claent=Entry(root,textvariable=clastr).grid(row=2,column=2)
rollent=Entry(root,textvariable=rollstr).grid(row=3,column=2)
schent=Entry(root,textvariable=schstr).grid(row=4,column=2)

def clear():
    root.destroy()
   
#button for submit
Button(text="Submit",command=clear).grid(row=6,column=2)
Button(text="Cancel",command=clear).grid(row=7,column=2)
root.mainloop()
