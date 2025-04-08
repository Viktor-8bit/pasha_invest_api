

import psycopg2


class Db:
    def __init__(self, connect):
        self.conn = psycopg2.connect(connect)
        self.cur = self.conn.cursor()
