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

root = Tk()
the_menu = Menu(root)
root.mainloop()
