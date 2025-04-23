







from model import Db
from model import Stock

class PriceSlicesRepository:

    def __init__(self, db: Db):
        self.db = db

    def make_slice_by_figi(self, figi: str):
        try:
            self.db.cur.execute("""SELECT date FROM StocksFormated WHERE  figi = %s;""", (figi,))

            data = self.db.cur.fetchall()

            date_start = data[0][0]
            date_end = data[0][0]
            i = 1
            for sf in data:
                if i % 20 == 0:
                    date_end = sf[0]
                    # запись в бд
                    self.db.cur.execute("INSERT INTO price_slices (figi, start_date, end_date) VALUES (%s, %s, %s) ON CONFLICT (figi, start_date, end_date) DO NOTHING;",
                                        (figi, date_start, date_end))
                    date_start = sf[0]
                i += 1
            self.db.conn.commit()
        except Exception:
            return  { 'result': 'false' }
        return { 'result': 'true' }

    def get_unlabeled_data(self):
        try:
            unlabeled = []
            self.db.cur.execute("""SELECT id FROM price_slices WHERE id NOT IN (SELECT slice_id FROM price_levels GROUP BY slice_id);""")
            data = self.db.cur.fetchall()
            for unlbl in data:
                unlabeled.append(unlbl[0])
            return unlabeled
        except Exception:
            return "ошибка"


# CREATE TABLE if not exists price_slices (
#     id SERIAL PRIMARY KEY,
#     figi VARCHAR(64) NOT NULL,
#     start_date TIMESTAMPTZ NOT NULL,
#     end_date TIMESTAMPTZ NOT NULL,
#     UNIQUE (figi, start_date, end_date)
# )