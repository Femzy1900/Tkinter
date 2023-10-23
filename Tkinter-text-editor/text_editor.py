from tkinter import *
import tkinter.filedialog

class TextEditor: 
    
    @staticmethod
    def quit_app(event=None) :
        root.quit()
    
    def open_file(self, event=None):
        txt_file = tkinter.filedialog.askopenfilename(parent=root, initialdir='/')
        if txt_file: 
            self.text_area.delete(1.0, END)
            with open(txt_file) as _file:
                self.text_area.insert(1.0, _file.read())
                root.update_idletasks()

    def save_file(self, event=None):
        file = tkinter.filedialog.asksaveasfile(mode='w')
        if file is not None:
            data = self.text_area.get('1.0', END + '-1c')
            file.write(data)
            file.close()

    def make_bold(self):
        self.text_area.tag_add("bt", "sel.first", "sel.last")

    def __init__(self, root) -> None:
        self.text_to_write = ""
        root.title("Text Editor")
        root.geometry("600x550")
        frame = Frame(root, width=600, height=500)
        scrollbar = Scrollbar(frame)
        self.text_area = Text(frame, width=600, height=500, yscrollcommand=scrollbar.set, padx=10, pady=10, font=("Georgia", "14"))
        scrollbar.config(command=self.text_area.yview)
        scrollbar.pack(side="right", fill="y")
        self.text_area.pack(side="left", fill="both", expand=True)
        file_menu = Menu(the_menu, tearoff=0)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Quit", command=self.quit_app)

        the_menu.add_cascade(label="File", menu=file_menu)

        edit_menu = Menu(the_menu, tearoff=0)
        edit_menu.add_command(label="Bold", command=self.make_bold())
        the_menu.add_cascade(label="Edit", menu=edit_menu)
        self.text_area.tag_config("bt", font=("Georgia", "i4", "bold"))
        root.config(menu=the_menu)



root = Tk()
the_menu = Menu(root)
root.mainloop()
