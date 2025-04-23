





from services import *
from model import *

from flask import Blueprint
from flask import request


def price_levels_fabrick(priceLevelService: PriceLevelService):
    price_levels_api = Blueprint('price_levels_api', __name__, template_folder='endpoints')

    # удаление разметки по id
    @price_levels_api.route('/delete_price_level/<price_level_id>', methods=['DELETE'])
    def delete_price_level(price_level_id):
        return priceLevelService.delete_price_leve(price_level_id)

    # создание разметки по PriceSlices id
    @price_levels_api.route('/add_price_level/', methods=['POST'])
    def add_price_slice():
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            data = request.json
            price_level = PriceLevel(slice_id=data['slice_id'], level=data['level'], level_type=data['level_type'])
            return priceLevelService.add_price_level(price_level)
        else:
            return 'Content-Type not supported!'

    # получить по slice_id разметки

    return price_levels_api