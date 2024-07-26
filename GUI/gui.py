import customtkinter as ct
from add import *



def main(root):
    b1 = ct.CTkButton(root, text='Add new password', command=lambda:toplevel.add_pass())
    b1.pack()

def s1():
    root = ct.CTk()
    root.geometry("700x650")
    root.title('Ango - Password Manager')

    main(root)

    root.mainloop()

s1()
