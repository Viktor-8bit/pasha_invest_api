






class PriceSlice:


    def __init__(self, id: int, figi: str, start_date, end_date):
        self.id = id
        self.figi = figi
        self.start_date = start_date
        self.end_date = end_date


    def to_dict(self):
        return {
            'id': self.id,
            'figi': self.figi,
            'start_date': self.start_date.strftime('%Y-%m-%d'),
            'end_date': self.end_date.strftime('%Y-%m-%d')
        }


# CREATE TABLE if not exists price_slices (
#     id SERIAL PRIMARY KEY,
#     figi VARCHAR(64) NOT NULL,
#     start_date TIMESTAMPTZ NOT NULL,
#     end_date TIMESTAMPTZ NOT NULL,
#     UNIQUE (figi, start_date, end_date)
# )