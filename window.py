from tkinter import *
from phones import *


class CreateWindow:
    def which_selected(self):
        print(f"At {select.curselection()}")
        return int(select.curselection()[0])

    def add_entry(self):
        phonelist.append([fnamevar.get(), lnamevar.get(), phonevar.get()])
        self.set_select()

    def update_entry(self):
        phonelist[self.which_selected()] = [fnamevar.get(),
                                            lnamevar.get(),
                                            phonevar.get()]

    def delete_entry(self):
        del phonelist[self.which_selected()]
        self.set_select()

    def clear_entry(self):
        fnamevar.set("")
        lnamevar.set("")
        phonevar.set("")
        self.set_select()

    def load_entry(self, evt):
        w = evt.widget
        index = int(w.curselection()[0])
        fname, lname, phone = phonelist[index]
        fnamevar.set(fname)
        lnamevar.set(lname)
        phonevar.set(phone)

    def make_window(self):
        global fnamevar, lnamevar, phonevar, select
        win = Tk()
        win.geometry("400x300")

        frame1 = Frame(win)
        frame1.pack()

        Label(frame1, text="First Name").grid(row=0, column=0, sticky=W)
        fnamevar = StringVar()
        fname = Entry(frame1, textvariable=fnamevar)
        fname.grid(row=0, column=1, sticky=W)

        Label(frame1, text="Last Name").grid(row=1, column=0, sticky=W)
        lnamevar = StringVar()
        lname = Entry(frame1, textvariable=lnamevar)
        lname.grid(row=1, column=1, sticky=W)

        Label(frame1, text="Phone").grid(row=2, column=0, sticky=W)
        phonevar = StringVar()
        phone = Entry(frame1, textvariable=phonevar)
        phone.grid(row=2, column=1, sticky=W)

        frame2 = Frame(win)  # Row of buttons
        frame2.pack()
        b1 = Button(frame2, text=" Add  ", command=self.add_entry)
        b2 = Button(frame2, text="Update", command=self.update_entry)
        b3 = Button(frame2, text="Delete", command=self.delete_entry)
        b4 = Button(frame2, text="Clear ", command=self.clear_entry)
        b1.pack(side=LEFT)
        b2.pack(side=LEFT)
        b3.pack(side=LEFT)
        b4.pack(side=LEFT)

        frame3 = Frame(win)  # select of names
        frame3.pack()
        scroll = Scrollbar(frame3, orient=VERTICAL)
        select = Listbox(frame3, yscrollcommand=scroll.set, height=6)
        select.bind('<<ListboxSelect>>', self.load_entry)
        scroll.config(command=select.yview)
        scroll.pack(side=RIGHT, fill=Y)
        select.pack(side=LEFT, fill=BOTH, expand=1)

        win.update()
        win.minsize(win.winfo_width(), win.winfo_height())
        win.title("Phonebook")
        return win

    def set_select(self):
        phonelist.sort(key=lambda record: record[1])
        select.delete(0, END)
        for fname, lname, phone in phonelist:
            select.insert(END, f'{lname}, {fname}')
