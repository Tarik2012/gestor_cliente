from tkinter import *
from tkinter import ttk
import database as db

class CenterWidgetMixin:
    def center(self):
        width = 600  # Ancho deseado para la ventana
        height = 200  # Alto deseado para la ventana

        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)

        self.geometry('{}x{}+{}+{}'.format(width, height, x, y))

class MainWindow(Tk, CenterWidgetMixin):
    def __init__(self):
        super().__init__()
        self.title('Gestor de clientes')
        self.build()
        self.center()

    def build(self):
        frame = Frame(self)
        frame.pack()

        treeview = ttk.Treeview(frame)
        treeview['columns'] = ('DNI', 'Nombre', 'Apellido')
        

        treeview.column("#0", width=0, stretch=NO)
        treeview.column("DNI", anchor=CENTER)
        treeview.column("Nombre", anchor=CENTER)
        treeview.column("Apellido", anchor=CENTER)

        treeview.heading("#0", anchor=CENTER)
        treeview.heading("DNI", text="DNI", anchor=CENTER)
        treeview.heading("Nombre", text="Nombre", anchor=CENTER)
        treeview.heading("Apellido", text="Apellido", anchor=CENTER)

        scrollbar = Scrollbar(frame, orient=VERTICAL, command=treeview.yview)
        treeview.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=RIGHT, fill=Y)

        for cliente in db.Clientes.lista:
            treeview.insert('', 'end', iid=cliente.dni, values=(cliente.dni, cliente.nombre, cliente.apellido))
        treeview.pack()
        
        # Bottom Frame
        frame = Frame(self)
        frame.pack(pady=20)

        # Buttons
        Button(frame, text="Crear", command=None).grid(row=1, column=0)
        Button(frame, text="Modificar", command=None).grid(row=1, column=1)
        Button(frame, text="Borrar", command=None).grid(row=1, column=2)   
        
        self.treeview = treeview

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
