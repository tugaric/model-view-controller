import tkinter.ttk as ttk

class config_treeview(ttk.Treeview):
    def __init__(self, master ,columns, col, row):
        super().__init__(master, columns=columns)
        self["show"] = "headings"
        self.heading("plan", text="plan number")
        self.heading("article", text="article number")
        self.column("plan", width=80)
        self.column("article", width=120)
        self.grid(column=col, row=row)