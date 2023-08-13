from tkinter import *
# Create the main window
root =Tk()
root.title("Simple Menu Example")
# Create a menu bar
menu_bar = Menu(root)
root.config(menu=menu_bar)
# Create a File menu and add it to the menu bar
file_menu = Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
# Add menu items to the File menu
file_menu.add_command(label="New")
file_menu.add_command(label="Open")
file_menu.add_command(label="Exit")
#extra
help=Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label='Help')
# Run the application
root.mainloop()
