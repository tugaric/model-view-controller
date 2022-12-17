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

    def get_comp_data(self, serie):
        seat = self.model.get_serie_component(serie, SQL_QUERY.SEAT)
        body = self.model.get_serie_component(serie, SQL_QUERY.BODY)
        self.model.store_image(serie)
        tk_img = ImageTk.PhotoImage(Image.open("temp.png"))
        return tk_img, seat, body

    def serie_selected(self, *event):
        # get the data of all the different components 
        selected_serie = self.view.tkVar_select_serie.get()
        tk_img, seat, body = self.get_comp_data(selected_serie)
        
        # set the image
        self.view.lbl_image.configure(image=tk_img)
        self.view.lbl_image.image = tk_img

        # get seat data for the serie
        self.view.set_seat(seat)

        # get body data for the serie
        self.view.set_body(body)