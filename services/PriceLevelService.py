


from repositories import PriceLevelRepository
from model import *

class PriceLevelService:

    def __init__(self, level_repo: PriceLevelRepository):
        self.level_repo = level_repo

    def add_price_level(self, price_level: PriceLevel):
        return self.level_repo.add_price_level(price_level)

    def delete_price_leve(self, id: int):
        return self.level_repo.delete_price_level(id)