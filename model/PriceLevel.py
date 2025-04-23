





class PriceLevel:



    def __init__(self, slice_id: int, level: int, level_type: str, id=0):
        self.id = id
        self.slice_id = slice_id
        self.level = level
        self.level_type = level_type


    def to_dict(self):
        return {
            'id': self.id,
            'slice_id': self.slice_id,
            'level': self.level,
            'level_type': self.level_type,
        }

# insert into price_levels(slice_id, level, level_type) values (432, 0, 'o');

# id SERIAL PRIMARY KEY,
# slice_id INTEGER NOT NULL,
# level NUMERIC(18, 8) NOT NULL,
# level_type VARCHAR(50),