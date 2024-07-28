import customtkinter as ct
from add import *
from tkinter import ttk
from get_passwords import *



def main(root):
    b1 = ct.CTkButton(root, text='Add new password', command=lambda:toplevel.add_pass(), fg_color='#343d44', hover_color='#676c74')
    b1.pack()

    tree = ttk.Treeview(root, columns=('Service', 'Login', 'Password'), show='headings')
    tree.heading('Service', text='Service')
    tree.heading('Login', text='Login')
    tree.heading('Password', text='Password')
    tree.pack(fill='both', expand=True)

    rows = get_passwords()
    for row in rows:
        tree.insert("", "end", values=row)

    b2 = ct.CTkButton(root, text='Remove password', fg_color='#343d44', hover_color='#676c74')
    b2.pack()

    for child in root.winfo_children():
        child.pack_configure(padx=10, pady=50)

def s1():
    root = ct.CTk()
    root.geometry("700x650")
    root.title('Ango - Password Manager')
    root.iconbitmap('GUI\Visual\icon.ico')

    main(root)

    root.mainloop()

s1()
