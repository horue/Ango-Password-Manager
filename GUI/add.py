import customtkinter as ct


class toplevel():
    def add_pass(title='Add new password', size='500x400'):
        tl = ct.CTkToplevel()
        tl.geometry(size)
        tl.title(title)
        tl.resizable(False, False)
        tl.grab_set()

        e1 = ct.CTkEntry(tl, placeholder_text='Service')
        e1.pack()

        e2 = ct.CTkEntry(tl, placeholder_text='Login')
        e2.pack()

        e3 = ct.CTkEntry(tl, placeholder_text='Password')
        e3.pack()

        b1 = ct.CTkButton(tl, text='Add')
        b1.pack()
        
        for child in tl.winfo_children():
            child.pack_configure(padx=10, pady=10)

        