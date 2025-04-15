







from model import Db
from model import Stock

class PriceSlicesRepository:

    def __init__(self, db: Db):
        self.db = db

    def make_slice_by_figi(self, figi: str):
        self.db.cur.execute("""SELECT date FROM StocksFormated WHERE %s = figi ;""", (figi))

        data = self.db.cur.fetchall()

        date_start = data[0][0]
        date_end = data[0][0]
        i = 0
        for sf in data:
            if i % 20 == 0:
                date_end = sf[0]
                # запись в бд
                date_start = sf[0]


        return None