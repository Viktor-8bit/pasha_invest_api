


from repositories import *
from model import *

class PriceLevelService:

    def __init__(self, level_repo: PriceLevelRepository, slice_repo: PriceSlicesRepository):
        self.level_repo = level_repo
        self.slice_repo = slice_repo

    def add_price_level(self, price_level: PriceLevel):
        return self.level_repo.add_price_level(price_level)

    def delete_price_leve(self, id: int):
        return self.level_repo.delete_price_level(id)

    def get_price_level_by_slice_id(self, slice_id: int):
        return self.level_repo.get_price_level_by_slice_id(slice_id)

    def get_labeled_and_unlabeled_data(self):
        return {
            'labeled' : self.level_repo.get_labeled_data(),
            'unlabeled' : self.slice_repo.get_unlabeled_data()
        }