from tkinter import *
root= Tk()
root.geometry("400x400")
root.title("Pop=up")
def popup():
    popwin=Toplevel(root)
    popwin.title("SAVE")
    popwin.geometry("150x150")
    button=Button(popwin,text="ok",command=popwin.destroy)
    save=Label(popwin,text="Want to save ?")
    save.pack()
    button.pack()
    popwin.mainloop()

but=Button(root,text="Open",command=popup)
but.pack()
root.mainloop()