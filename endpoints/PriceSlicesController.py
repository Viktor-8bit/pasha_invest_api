from services import *

from flask import Blueprint

from flask import request


def price_slice_api_fabrick(priceSliceService: PriceSliceService):
    stock_api = Blueprint('price_slice_api', __name__, template_folder='endpoints')

    # авто разметка исторических данных акции по figi
    @stock_api.route("/make_slice_by_figi/")
    def make_slice_by_figi():
        figi = request.args.get('figi')
        return priceSliceService.make_slice_by_figi(figi)

    # получить 1 разметку по id
    @stock_api.route('/get_price_slice_by_id/<price_slice_id>', methods=['GET'])
    def get_price_slice_by_id(price_slice_id):
        return priceSliceService.get_price_slice_by_id(price_slice_id)

    return stock_api