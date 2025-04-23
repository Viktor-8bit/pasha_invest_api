


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

