from tkinter import *
import tkinter.ﬁledialog

class TextEditor:
    # Quits the TkInter app when called
    @staticmethod
    def quit_app(event=None):
        root.quit()
    # ----- NEXT TUTORIAL -----
    def remake_ﬁle(self, text_area_list):
        for i in text_area_list:
            print("Key", i[0])
            print("Value", i[1])
            print("Index", i[2])
    # ----- END NEXT TUTORIAL -----
    def open_ﬁle(self, event=None):
        # Open dialog and get chosen ﬁle
        txt_ﬁle = tkinter.ﬁledialog.askopenﬁlename(parent=root,
                                                      initialdir='/')
        # If the ﬁle exists
        if txt_ﬁle:
            self.text_area.delete(1.0, END)
            # Open ﬁle and put text in the text widget
            with open(txt_ﬁle) as _ﬁle:
                self.text_area.insert(1.0, _ﬁle.read())
                # Update the text widget
                root.update_idletasks()
    def save_ﬁle(self, event=None):
        # Opens the save as dialog box
        ﬁle = tkinter.ﬁledialog.asksaveasﬁle(mode='w')
        if ﬁle is not None:
            # Get text in the text widget and delete the last newline
            data = self.text_area.get('1.0', END + '-1c')
            # Write the text and close
            ﬁle.write(data)
            # ----- NEXT TUTORIAL -----
            # print(str(self.text_area.dump('1.0', END)))
            # self.remake_ﬁle(self.text_area.dump('1.0', END))
            # ----- END NEXT TUTORIAL -----

            ﬁle.close()
    def make_bold(self):
        self.text_area.tag_add("bt", "sel.ﬁrst", "sel.last")
    def __init__(self, root):
        self.text_to_write = ""
        # Deﬁne title for the app
        root.title("Text Editor")
        # Deﬁnes the width and height of the window
        root.geometry("600x550")
        frame = Frame(root, width=600, height=550)
        # Create the scrollbar
        scrollbar = Scrollbar(frame)
        # yscrollcommand connects the scroll bar to the text
        # area
        self.text_area = Text(frame, width=600, height=550,
                        yscrollcommand=scrollbar.set,
                        padx=10, pady=10, font=("Georgia", "14"))
        # Call yview when the scrollbar is moved
        scrollbar.conﬁg(command=self.text_area.yview)
        # Put scroll bar on the right and ﬁll in the Y direction
        scrollbar.pack(side="right", ﬁll="y")
        # Pack on the left and ﬁll available space
        self.text_area.pack(side="left", ﬁll="both", expand=True)
        frame.pack()
        # ----- FILE MENU CREATION -----
        # Create a pull down menu that can't be removed
        ﬁle_menu = Menu(the_menu, tearoﬀ=0)
        # Add items to the menu that show when clicked
        # compound allows you to add an image
        ﬁle_menu.add_command(label="Open", command=self.open_ﬁle)
        ﬁle_menu.add_command(label="Save", command=self.save_ﬁle)
        # Add a horizontal bar to group similar commands
        ﬁle_menu.add_separator()
        # Call for the function to execute when clicked
        ﬁle_menu.add_command(label="Quit", command=self.quit_app)
        # Add the pull down menu to the menu bar

        the_menu.add_cascade(label="File", menu=ﬁle_menu)
        # ----- EDIT MENU CREATION -----
        edit_menu = Menu(the_menu, tearoﬀ=0)
        edit_menu.add_command(label="Bold", command=self.make_bold)
        the_menu.add_cascade(label="Edit", menu=edit_menu)
        self.text_area.tag_conﬁg("bt", font=("Georgia", "14", "bold"))

        # Display the menu bar
        root.conﬁg(menu=the_menu)

root = Tk()
# Create the menu object
the_menu = Menu(root)
text_editor = TextEditor(root)
root.mainloop()
