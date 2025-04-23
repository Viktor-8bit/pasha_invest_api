


from model import *

class PriceLevelRepository:

    def __init__(self, db: Db):
        self.db = db

    # добавить PriceLevel
    def add_price_level(self, price_level: PriceLevel):
        try:
            self.db.cur.execute("""INSERT INTO price_levels (slice_id, level, level_type) VALUES (%s, %s, %s);""",
                                (price_level.slice_id, price_level.level, price_level.level_type))
            self.db.conn.commit()
        except Exception:
            return {'result': 'ошибка'}
        return {'result': 'ок'}


    # удалить PriceLevel
    def delete_price_level(self, id: int):
        try:
            self.db.cur.execute("""DELETE FROM price_levels WHERE id = %s; """,
                                (id,))
            self.db.conn.commit()
        except Exception:
            return {'result': 'ошибка'}
        return {'result': 'ок'}

    # получить по slice_id разметки
    def get_price_level_by_slice_id(self, slice_id: int):
        try:
            # select * from price_levels where slice_id = 432;
            self.db.cur.execute(""" SELECT * FROM price_levels WHERE slice_id = %s; """,
                                (slice_id,))
            data = self.db.cur.fetchall()
            result = []
            for prlvl in data:
                result.append(PriceLevel(id=prlvl[0], slice_id=prlvl[1], level=prlvl[2], level_type=prlvl[3]).to_dict())
            return result
        except Exception:
            return {'result': 'ошибка'}

    # получить не размеченные PriceLevels
    def get_labeled_data(self):
        try:
            labled = []
            self.db.cur.execute("""SELECT slice_id FROM price_levels GROUP BY slice_id;""")
            data = self.db.cur.fetchall()
            for lbl in data:
                labled.append(lbl[0])
            return labled

        except Exception:
            return 'ошибка'