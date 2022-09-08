from tkinter import *
from phones import *

class CreateWindow:
    def __init__(self):
        self.db = Database()
        self.pos = None

    def which_selected(self, evt):
        w = evt.widget
        self.pos = int(w.curselection()[0])+1
        self.load_entry()

    def add_entry(self):
        self.db.insert(select.size()+1, nombrevar.get(), productovar.get(), numerovar.get(), preciovar.get())
        self.set_select()

    def update_entry(self):
        print(self.pos)
        self.db.update(self.pos, nombrevar.get(), productovar.get(), numerovar.get(), preciovar.get())
        self.clear_entry()

    def delete_entry(self):
        self.db.delete(self.pos)
        self.clear_entry()

    def clear_entry(self):
        nombrevar.set("")
        productovar.set("")
        numerovar.set("")
        preciovar.set("")
        self.set_select()

    def load_entry(self):
        records = self.db.get_id(self.pos)
        nombrevar.set(records[1])
        productovar.set(records[2])
        numerovar.set(records[3])
        preciovar.set(records[4])

    def make_window(self):
        global nombrevar, productovar, numerovar, preciovar, select
        win = Tk()
        win.geometry("400x300")

        frame1 = Frame(win)
        frame1.pack()

        # Text box for First Name
        Label(frame1, text="Nombre").grid(row=0, column=0, sticky=W)
        nombrevar = StringVar()
        nombre = Entry(frame1, textvariable=nombrevar)
        nombre.grid(row=0, column=1, sticky=W)

        # Text box for Last Name
        Label(frame1, text="Producto").grid(row=1, column=0, sticky=W)
        productovar = StringVar()
        producto = Entry(frame1, textvariable=productovar)
        producto.grid(row=1, column=1, sticky=W)

        # Text box for numero number
        Label(frame1, text="Numero").grid(row=2, column=0, sticky=W)
        numerovar = StringVar()
        numero = Entry(frame1, textvariable=numerovar)
        numero.grid(row=2, column=1, sticky=W)

        # Text box for numero number
        Label(frame1, text="Precio").grid(row=3, column=0, sticky=W)
        preciovar = StringVar()
        precio = Entry(frame1, textvariable=preciovar)
        precio.grid(row=3, column=1, sticky=W)

        # Section for action buttons
        frame2 = Frame(win)
        frame2.pack()
        b1 = Button(frame2, text="Agregar", command=self.add_entry)
        b2 = Button(frame2, text="Actualizar", command=self.update_entry)
        b3 = Button(frame2, text="Eliminar", command=self.delete_entry)
        b4 = Button(frame2, text="Limpiar Textos ", command=self.clear_entry)
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
        win.title("Agenda")
        return win

    def set_select(self):
        records = self.db.get_all()
        select.delete(0, END)
        for identity, nombre, producto, numero, precio in records:
            select.insert(END, f'{producto}, {nombre}, {numero}, {precio}')
