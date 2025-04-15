from services import *

from flask import Blueprint

from flask import request


def price_slice_api_fabrick(priceSliceService: PriceSliceService):
    stock_api = Blueprint('price_slice_api', __name__, template_folder='endpoints')

    @stock_api.route("/make_slice_by_figi/")
    def make_slice_by_figi():
        figi = request.args.get('figi')
        return priceSliceService.make_slice_by_figi(figi)

    return stock_api