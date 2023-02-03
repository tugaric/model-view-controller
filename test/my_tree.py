import tkinter as tk
import tkinter.ttk as ttk

data = [('03400140','3591e'),('03400240', '2354-1e')]

def fill_treeview(article_list):
    if len(article_list) > 1:
        # article_list contains multiple elements
        pass
    pass        


class NewprojectApp:
    def __init__(self, master=None):
        # build ui
        self.root = tk.Tk() if master is None else tk.Toplevel(master)
        self.root.configure(height=200, width=200)
        frame1 = ttk.Frame(self.root)
        frame1.configure(height=200, width=200)
        btn_call = ttk.Button(frame1, text="Get selected article", command=self.get_treeView)
        btn_call.grid(column=0, row=1)
        # treeview configuration
        columns = ("article", "plan")
        self.tree = ttk.Treeview(frame1, columns= columns)
        
        self.tree.heading("article", text="article number")
        self.tree.heading("plan", text="plan number")
        comp = self.tree.insert(parent="", index=tk.END, text= "component type")
        self.tree.insert(parent=comp, index=tk.END, values=data)
        self.tree.configure(selectmode="extended")
        self.tree.grid(column=0, row=0)
        frame1.pack(side="top")

        # Main widget
        self.mainwindow = self.root

    def get_treeView(self):
        selected_item = self.tree.selection()
        print(selected_item)
        item_detail = self.tree.item(selected_item)
        print(item_detail)

    def run(self):
        self.mainwindow.mainloop()


if __name__ == "__main__":
    app = NewprojectApp()
    app.run()