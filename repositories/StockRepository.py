


from model import Db
from model import Stock

class StockRepository:

    def __init__(self, db: Db):
        self.db = db

    def get_by_time_range(self, before: str, after: str):
        self.db.cur.execute(""" SELECT * FROM StocksFormated WHERE %s <= date and date <= %s ;""", (before, after))

        data = self.db.cur.fetchall()

        result = []

        for st in data:
            result.append(Stock(st[0], st[1], st[2], st[3], st[4], st[5], st[6]).to_dict())

        return result