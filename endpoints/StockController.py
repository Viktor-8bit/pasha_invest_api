


from services import *

from flask import Blueprint

from flask import request


def stock_api_fabrick(stockService: StockService):
    stock_api = Blueprint('stock_api', __name__, template_folder='endpoints')

    # получить срез по before, after исторических данных
    @stock_api.route("/get_stock_slice/")
    def get_stock_slice():
        before = request.args.get('before')
        after = request.args.get('after')
        return stockService.get_stocks(before, after)

    return stock_api