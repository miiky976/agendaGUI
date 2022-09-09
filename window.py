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
        fontsize=12
        backg = "white"
        foreg = "black"
        listback = "#D6EAF8"
        textback = "#AED6F1"

        global nombrevar, productovar, numerovar, preciovar, select
        root = Tk()
        root.geometry("600x400")
        root.config(bg=backg)

        frame1 = Frame(root, bg=backg)
        frame1.pack()

        # Text box for First Name
        Label(frame1, text="Nombre", bg=backg, fg=foreg, font=("Arial", fontsize)).grid(row=0, column=0, sticky=W)
        nombrevar = StringVar()
        nombre = Entry(frame1, textvariable=nombrevar, bg=textback, fg=foreg, font=("Arial", fontsize), borderwidth=0)
        nombre.grid(row=0, column=1, sticky=W)

        # Text box for Last Name
        Label(frame1, text="Producto", bg=backg, fg=foreg, font=("Arial", fontsize)).grid(row=1, column=0, sticky=W)
        productovar = StringVar()
        producto = Entry(frame1, textvariable=productovar, bg=textback, fg=foreg, font=("Arial", fontsize), borderwidth=0)
        producto.grid(row=1, column=1, sticky=W)

        # Text box for numero number
        Label(frame1, text="Numero", bg=backg, fg=foreg, font=("Arial", fontsize)).grid(row=2, column=0, sticky=W)
        numerovar = StringVar()
        numero = Entry(frame1, textvariable=numerovar, bg=textback, fg=foreg, font=("Arial", fontsize), borderwidth=0)
        numero.grid(row=2, column=1, sticky=W)

        # Text box for numero number
        Label(frame1, text="Precio", bg=backg, fg=foreg, font=("Arial", fontsize)).grid(row=3, column=0, sticky=W)
        preciovar = StringVar()
        precio = Entry(frame1, textvariable=preciovar, bg=textback, fg=foreg, font=("Arial", fontsize), borderwidth=0)
        precio.grid(row=3, column=1, sticky=W)

        # Section for action buttons
        frame2 = Frame(root, bg=backg)
        frame2.pack()
        b1 = Button(frame2, text="Agregar", command=self.add_entry, 
            bg="#ABEBC6", fg=foreg, borderwidth=0, font=("Arial", fontsize), activebackground="#82E0AA"
            )
        b2 = Button(frame2, text="Actualizar", command=self.update_entry, 
            bg="#D2B4DE", fg=foreg, borderwidth=0, font=("Arial", fontsize), activebackground="#BB8FCE"
            )
        b3 = Button(frame2, text="Eliminar", command=self.delete_entry, 
            bg="#F5B7B1", fg=foreg, borderwidth=0, font=("Arial", fontsize), activebackground="#F1948A"
            )
        b4 = Button(frame2, text="Limpiar Textos ", command=self.clear_entry, 
            bg="#E5E7E9", fg=foreg, borderwidth=0, font=("Arial", fontsize), activebackground="#D7DBDD"
            )
        b1.pack(side=LEFT)
        b2.pack(side=LEFT)
        b3.pack(side=LEFT)
        b4.pack(side=LEFT)

        # Section for list of contacts
        frame3 = Frame(root, bg=backg)
        frame3.pack()
        scrolly = Scrollbar(frame3, orient=VERTICAL)
        scrollx = Scrollbar(frame3, orient=HORIZONTAL)
        select = Listbox(frame3, yscrollcommand=scrolly.set, xscrollcommand=scrollx.set,
            height=15, width=70,
            bg=listback, fg=foreg, border=0,
            font=("Arial", fontsize)
            )
        select.bind('<<ListboxSelect>>', self.which_selected)
        scrolly.config(command=select.yview, bg=listback)
        scrollx.config(command=select.xview, bg=listback)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.pack(side=BOTTOM, fill=X)
        select.pack(side=LEFT, fill=BOTH, expand=1)

        root.update()
        root.minsize(root.winfo_width(), root.winfo_height())
        root.title("Agenda")
        return root

    def set_select(self):
        records = self.db.get_all()
        select.delete(0, END)
        for identity, nombre, producto, numero, precio in records:
            select.insert(END, f'{producto}, {nombre}, {numero}, {precio}')
