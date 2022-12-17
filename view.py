import tkinter as tk
import tkinter.ttk as ttk

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

        # selected serie variable
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

        self.lbl_body_article_nbr = ttk.Label(self.root)
        self.lbl_body_article_nbr.configure(state="normal", text='lbl_body_article')
        self.lbl_body_article_nbr.grid(column=1, row=2, sticky="n")

        self.lbl_sdisc_article_nbr = ttk.Label(self.root)
        self.lbl_sdisc_article_nbr.configure(text='lbl_seat_disc_article')
        self.lbl_sdisc_article_nbr.grid(column=1, row=3, sticky="n")

        self.lbl_body_plan = ttk.Label(self.root)
        self.lbl_body_plan.configure(text='lbl_body_plan')
        self.lbl_body_plan.grid(column=2, row=2, sticky="n")

        self.lbl_sdisc_plan = ttk.Label(self.root)
        self.lbl_sdisc_plan.configure(text='lbl_seat_disc_plan')
        self.lbl_sdisc_plan.grid(column=2, row=3, sticky="n")

        self.lbl_image = ttk.Label(self.root)
        self.lbl_image.configure(text='<image>')
        self.lbl_image.grid(column=3, row=2, sticky="nsew", rowspan=4)

        # Main widget
        self.mainwindow = self.root

    def set_seat(self, seat):
        self.lbl_sdisc_article_nbr.configure(text=seat)

    def set_body(self, body):
        self.lbl_body_article_nbr.configure(text=body)

    def run(self):
        self.mainwindow.mainloop()