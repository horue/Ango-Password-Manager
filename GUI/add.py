import customtkinter as ct
import sys
import os



from add_password import *

class toplevel():
    def add_pass(title='Add new password', size='500x400'):
        tl = ct.CTkToplevel()
        tl.geometry(size)
        tl.title(title)
        tl.resizable(False, False)
        tl.grab_set()

        l1 = ct.CTkLabel(tl, text='Add new password')
        l1.pack()

        e1 = ct.CTkEntry(tl, placeholder_text='Service')
        e1.pack(pady=(300, 0))

        e2 = ct.CTkEntry(tl, placeholder_text='Login')
        e2.pack()

        e3 = ct.CTkEntry(tl, placeholder_text='Password')
        e3.pack()

        b1 = ct.CTkButton(tl, text='Add', command=lambda:add_password_db(e1.get(), e2.get(), e3.get()))
        b1.pack()
        
        for child in tl.winfo_children():
            child.pack_configure(padx=10, pady=15)

        