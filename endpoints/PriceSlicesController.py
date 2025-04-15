from services import *

from flask import Blueprint

from flask import request


def price_slice_api_fabrick(priceSliceService: PriceSliceService):
    stock_api = Blueprint('price_slice_api', __name__, template_folder='endpoints')

    @stock_api.route("/make_slice_by_figi/")
    def get_stock_slice():
        figi = request.args.get('figi')
        return priceSliceService. (figi)

    return stock_api