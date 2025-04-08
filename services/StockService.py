

from repositories import StockRepository


class StockService:

    def __init__(self, stock_repo: StockRepository):
        self.stockRepo = stock_repo

    def get_stocks(self, before: str, after: str):
        return self.stockRepo.get_by_time_range(before, after)