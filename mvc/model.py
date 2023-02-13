import sqlite3
from custom_classes.article import article
from typing import Tuple, List
from custom_classes.SQL import SQL_QUERY

class myModel:
    path = "database/rotarex.db"

    def __init__(self):
        self.conn = sqlite3.connect(myModel.path)
        self.cursor = self.conn.cursor()

    def get_serie_component(self, serie, component_query): 
        sql_statement = component_query + f"\"{serie}\""
        self.cursor.execute(sql_statement)
        query_result = self.cursor.fetchall()
        return [ article(data_point[0], data_point[1]) for data_point in query_result ]

if __name__ == "__main__":
    model = myModel()
    series = ["C105","C045"]
    res = []
    bodies = model.get_serie_component(series[1], SQL_QUERY.SEAT)
    print(bodies)