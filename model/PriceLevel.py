





class PriceLevel:



    def __init__(self, slice_id: int, level: int, level_type: str):
        self.slice_id = slice_id
        self.level = level
        self.level_type = level_type


    def to_dict(self):
        return {
            'slice_id': self.slice_id,
            'level': self.level,
            'level_type': self.level_type,
        }

# insert into price_levels(slice_id, level, level_type) values (432, 0, 'o');