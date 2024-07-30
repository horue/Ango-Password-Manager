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
        tl.iconbitmap('GUI\Visual\icon.ico')

        l1 = ct.CTkLabel(tl, text='Add new password')
        l1.pack()

        e1 = ct.CTkEntry(tl, placeholder_text='Service')
        e1.pack()

        e2 = ct.CTkEntry(tl, placeholder_text='Login')
        e2.pack()

        e3 = ct.CTkEntry(tl, placeholder_text='Password')
        e3.pack()

        b1 = ct.CTkButton(tl, text='Add', command=lambda:add_password_db(e1.get(), e2.get(), e3.get()), fg_color='#343d44', hover_color='#676c74')
        b1.pack()
        
        for child in tl.winfo_children():
            child.pack_configure(padx=10, pady=15)

        