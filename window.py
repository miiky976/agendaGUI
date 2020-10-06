from tkinter import *
from phones import *

class CreateWindow:
    def __init__(self):
        self.db = Database()
        self.pos = None

    def which_selected(self, evt):
        w = evt.widget
        self.pos = int(w.curselection()[0])
        self.load_entry()

    def add_entry(self):
        self.db.insert(select.size(), fnamevar.get(), lnamevar.get(), phonevar.get())
        self.set_select()

    def update_entry(self):
        self.db.update(self.pos, fnamevar.get(), lnamevar.get(), phonevar.get())
        self.clear_entry()

    def delete_entry(self):
        self.db.delete(self.pos)
        self.clear_entry()

    def clear_entry(self):
        fnamevar.set("")
        lnamevar.set("")
        phonevar.set("")
        self.set_select()

    def load_entry(self):
        records = self.db.get_id(self.pos)
        fnamevar.set(records[1])
        lnamevar.set(records[2])
        phonevar.set(records[3])

    def make_window(self):
        global fnamevar, lnamevar, phonevar, select
        win = Tk()
        win.geometry("400x300")

        frame1 = Frame(win)
        frame1.pack()

        # Text box for First Name
        Label(frame1, text="First Name").grid(row=0, column=0, sticky=W)
        fnamevar = StringVar()
        fname = Entry(frame1, textvariable=fnamevar)
        fname.grid(row=0, column=1, sticky=W)

        # Text box for Last Name
        Label(frame1, text="Last Name").grid(row=1, column=0, sticky=W)
        lnamevar = StringVar()
        lname = Entry(frame1, textvariable=lnamevar)
        lname.grid(row=1, column=1, sticky=W)

        # Text box for Phone number
        Label(frame1, text="Phone").grid(row=2, column=0, sticky=W)
        phonevar = StringVar()
        phone = Entry(frame1, textvariable=phonevar)
        phone.grid(row=2, column=1, sticky=W)

        # Section for action buttons
        frame2 = Frame(win)
        frame2.pack()
        b1 = Button(frame2, text=" Add  ", command=self.add_entry)
        b2 = Button(frame2, text="Update", command=self.update_entry)
        b3 = Button(frame2, text="Delete", command=self.delete_entry)
        b4 = Button(frame2, text="Clear ", command=self.clear_entry)
        b1.pack(side=LEFT)
        b2.pack(side=LEFT)
        b3.pack(side=LEFT)
        b4.pack(side=LEFT)

        # Section for list of contacts
        frame3 = Frame(win)
        frame3.pack()
        scroll = Scrollbar(frame3, orient=VERTICAL)
        select = Listbox(frame3, yscrollcommand=scroll.set, height=6)
        select.bind('<<ListboxSelect>>', self.which_selected)
        scroll.config(command=select.yview)
        scroll.pack(side=RIGHT, fill=Y)
        select.pack(side=LEFT, fill=BOTH, expand=1)

        win.update()
        win.minsize(win.winfo_width(), win.winfo_height())
        win.title("Phonebook")
        return win

    def set_select(self):
        records = self.db.get_all()
        select.delete(0, END)
        for identity, fname, lname, phone in records:
            select.insert(END, f'{lname}, {fname}')
