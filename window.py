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
        global nombrevar, productovar, numerovar, preciovar, select
        root = Tk()
        root.geometry("600x400")
        root.config(bg="#1a232e")

        fontsize=14

        frame1 = Frame(root, bg="#1a232e")
        frame1.pack()

        # Text box for First Name
        Label(frame1, text="Nombre", bg="#1a232e", fg="white", font=("Arial", fontsize)).grid(row=0, column=0, sticky=W)
        nombrevar = StringVar()
        nombre = Entry(frame1, textvariable=nombrevar, bg="#516374", fg="white", font=("Arial", fontsize), borderwidth=0)
        nombre.grid(row=0, column=1, sticky=W)

        # Text box for Last Name
        Label(frame1, text="Producto", bg="#1a232e", fg="white", font=("Arial", fontsize)).grid(row=1, column=0, sticky=W)
        productovar = StringVar()
        producto = Entry(frame1, textvariable=productovar, bg="#516374", fg="white", font=("Arial", fontsize), borderwidth=0)
        producto.grid(row=1, column=1, sticky=W)

        # Text box for numero number
        Label(frame1, text="Numero", bg="#1a232e", fg="white", font=("Arial", fontsize)).grid(row=2, column=0, sticky=W)
        numerovar = StringVar()
        numero = Entry(frame1, textvariable=numerovar, bg="#516374", fg="white", font=("Arial", fontsize), borderwidth=0)
        numero.grid(row=2, column=1, sticky=W)

        # Text box for numero number
        Label(frame1, text="Precio", bg="#1a232e", fg="white", font=("Arial", fontsize)).grid(row=3, column=0, sticky=W)
        preciovar = StringVar()
        precio = Entry(frame1, textvariable=preciovar, bg="#516374", fg="white", font=("Arial", fontsize), borderwidth=0)
        precio.grid(row=3, column=1, sticky=W)

        # Section for action buttons
        frame2 = Frame(root, bg="#1a232e")
        frame2.pack()
        b1 = Button(frame2, text="Agregar", command=self.add_entry, 
            bg="#125230", fg="white", borderwidth=0, font=("Arial", fontsize), activebackground="#0F4428"
            )
        b2 = Button(frame2, text="Actualizar", command=self.update_entry, 
            bg="#2F6161", fg="white", borderwidth=0, font=("Arial", fontsize), activebackground="#0F4444"
            )
        b3 = Button(frame2, text="Eliminar", command=self.delete_entry, 
            bg="#69090C", fg="white", borderwidth=0, font=("Arial", fontsize), activebackground="#440F11"
            )
        b4 = Button(frame2, text="Limpiar Textos ", command=self.clear_entry, 
            bg="#0E286B", fg="white", borderwidth=0, font=("Arial", fontsize), activebackground="#0F1E44"
            )
        b1.pack(side=LEFT)
        b2.pack(side=LEFT)
        b3.pack(side=LEFT)
        b4.pack(side=LEFT)

        # Section for list of contacts
        frame3 = Frame(root, bg="#1a232e")
        frame3.pack()
        scrolly = Scrollbar(frame3, orient=VERTICAL)
        scrollx = Scrollbar(frame3, orient=HORIZONTAL)
        select = Listbox(frame3, yscrollcommand=scrolly.set, xscrollcommand=scrollx.set,
            height=15, width=70,
            bg="#354755", fg="white", border=0,
            font=("Arial", fontsize)
            )
        select.bind('<<ListboxSelect>>', self.which_selected)
        scrolly.config(command=select.yview)
        scrollx.config(command=select.xview)
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
