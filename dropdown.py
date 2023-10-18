from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def quit_app():
    root.quit()

def show_about(event=None):
    messagebox.showwarning(
        "About", "Isn't this an awesome program?"
    )



root = Tk()
root.title("Menu Bar")


the_menu = Menu(root)

# ----- FILE -----
file_menu = Menu(the_menu, tearoff=0)

file_menu.add_command(label="Open")
file_menu.add_command(label="Save")
file_menu.add_separator()
file_menu.add_command(label="Quit")


root.mainloop()