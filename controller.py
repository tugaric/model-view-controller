from view import myView
from model import myModel
from SQL import SQL_QUERY
from PIL import Image, ImageTk

class myController:
    def __init__(self):
        self.view = myView()
        self.model = myModel()

    def start(self):
        self.view.setup(self)
        self.view.run()

    def serie_selected(self, *event):
        # print(self.view.tkVar_select_serie.get())
        selected_serie = self.view.tkVar_select_serie.get()
        
        # set the image
        self.model.store_image(selected_serie)
        tk_img = ImageTk.PhotoImage(Image.open("temp.png"))
        self.view.lbl_image.configure(image=tk_img)
        self.view.lbl_image.image = tk_img

        # get seat data for the serie
        seat = self.model.get_serie_component(selected_serie, SQL_QUERY.SEAT)
        self.view.lbl_sdisc_article_nbr.configure(text=seat)

        # get body data for the serie
        body = self.model.get_serie_component(selected_serie, SQL_QUERY.BODY)
        self.view.lbl_body_article_nbr.configure(text=body)