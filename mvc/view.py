import tkinter as tk
import tkinter.ttk as ttk
from custom_classes.configure import config_treeview

class myView:
    def setup(self, controller, master=None):
    # build ui
        self.root = tk.Tk() if master is None else tk.Toplevel(master)
        self.root.configure(height=200, highlightcolor="#4949f8", width=400)
        self.root.title("Rotarex homologation")
        
        label2 = ttk.Label(self.root)
        label2.configure(text='Select serie: ')
        label2.grid(column=0, row=0)
        self.cbo_select_serie = ttk.Combobox(self.root)

        self.tkVar_select_serie = tk.StringVar()
        self.tkVar_select_serie.trace_add("write", controller.serie_selected)

        self.cbo_select_serie.configure(textvariable=self.tkVar_select_serie, values='C040 C045 C100 C105')
        self.cbo_select_serie.grid(column=1, columnspan=3, row=0, sticky="e")

        label3 = ttk.Label(self.root)
        label3.configure(text='Body:')
        label3.grid(column=0, row=2, sticky="nw")

        separator1 = ttk.Separator(self.root)
        separator1.configure(orient="horizontal")
        separator1.grid(column=0, columnspan=4, row=1, sticky="ew")

        label4 = ttk.Label(self.root)
        label4.configure(text='seat disc:')
        label4.grid(column=0, row=3, sticky="nw")
        
        self.lbl_image = ttk.Label(self.root)
        self.lbl_image.configure(text='<image>')
        self.lbl_image.grid(column=3, row=2, sticky="nsew", rowspan=4)

    # TREEVIEW
        columns = ("article", "plan")
        self.treeV_body = config_treeview(self.root, columns, 1, 2)
        self.treeV_seat = config_treeview(self.root, columns, 1, 3)

    # Main widget
        self.mainwindow = self.root

    def update_seat_tree(self, seat):
        self.treeV_seat.insert("", index = tk.END, values = seat)

    def update_body_tree(self, body):
        self.treeV_body.insert("", index=tk.END, values = body)

    def clear_gui(self):
        self.treeV_body.delete(*self.treeV_body.get_children())
        self.treeV_seat.delete(*self.treeV_seat.get_children())

    def run(self):
        self.mainwindow.mainloop()