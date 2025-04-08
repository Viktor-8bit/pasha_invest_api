


from services import *

from flask import Blueprint



def stock_api_fabrick(stockService: StockService):
    stock_api = Blueprint('stock_api', __name__, template_folder='endpoints')

    @stock_api.route("/get_stock_slice/")
    def get_stock_slice():
        return stockService.get_stocks("2020-03-13", "2020-03-27")

    return stock_api