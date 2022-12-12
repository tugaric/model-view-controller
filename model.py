import sqlite3
from strenum import StrEnum
from SQL import SQL_QUERY

class article:
    def __init__(self, article_number, plan):
        self.article_number = article_number
        self.plan = plan

class valve:
    def __init__(self, body, seat, lower_spindle, upper_spindle):
        self.body = body
        self.seat = seat
        self.lower_spindle = lower_spindle
        self.upper_spindle = upper_spindle

class myModel:
    path = "rotarex.db"

    def __init__(self):
        self.conn = sqlite3.connect(myModel.path)
        self.cursor = self.conn.cursor()

    def get_serie_component(self, serie, component_query): # keyword of sql_statements body, seat, image etc
        sql_statement = component_query + f"\"{serie}\""
        self.cursor.execute(sql_statement)
        return self.cursor.fetchall()

    def store_image(self, serie):
        data = self.get_serie_component(serie, SQL_QUERY.IMAGE) # get image as sequence of binary 
        with open("temp.png", 'wb') as file:
            file.write(data[0][0])

if __name__ == "__main__":
    model = myModel()
    serie = "C045"
    body = model.get_serie_component(serie, SQL_QUERY.BODY)
    seat = model.get_serie_component(serie, SQL_QUERY.SEAT)
    print(seat)