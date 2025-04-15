
from repositories import PriceSlicesRepository

class PriceSliceService:

    def __init__(self, slice_repo: PriceSlicesRepository):
        self.slice_repo = slice_repo

    def make_slice_by_figi(self, figi: str):
        return self.slice_repo.make_slice_by_figi(figi)