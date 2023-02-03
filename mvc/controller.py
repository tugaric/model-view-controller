from mvc.view import myView
from mvc.model import myModel
from custom_classes.SQL import SQL_QUERY
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
    
        self.view.clear_gui()
        # get the data of all the different components 
        selected_serie = self.view.tkVar_select_serie.get()
        tk_img, seat, body = self.get_comp_data(selected_serie)
        
        # set the image
        self.view.lbl_image.configure(image=tk_img)
        self.view.lbl_image.image = tk_img

        for b in body:
            self.view.update_body_tree((b.number, b.plan))

        for s in seat:
            self.view.update_seat_tree((s.number, s.plan))
