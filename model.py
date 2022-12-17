import sqlite3
from my_dataclass import article
from typing import Tuple, List
from strenum import StrEnum
from SQL import SQL_QUERY

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
    body_article = article(*body)
    print(body_article)