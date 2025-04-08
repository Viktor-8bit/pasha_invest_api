




class Stock:

    def __init__(self, figi, open, high, low, close, volume, date):
        self.figi = figi
        self.open = open
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume
        self.date = date


    def to_dict(self):
        return {
            'figi': self.figi,
            'open': self.open,
            'high': self.high,
            'low': self.low,
            'close': self.close,
            'volume': self.volume,
            'date': self.date.strftime('%Y-%m-%d')
        }