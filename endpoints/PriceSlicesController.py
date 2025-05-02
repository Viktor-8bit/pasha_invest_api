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
        """
        Получение ценового среза по идентификатору
        ---
        tags:
          - Срезы цен
        parameters:
          - name: price_slice_id
            in: path
            type: integer
            required: true
            description: Идентификатор разметки цен
        responses:
          200:
            description: Разметка цен успешно получена
            schema:
              type: object
              properties:
                id:
                  type: integer
                  description: Идентификатор ценового среза
                figi:
                  type: string
                  description: Уникальный идентификатор актива
                start_date:
                  type: string
                  format: date
                  description: Дата начала среза
                end_date:
                  type: string
                  format: date
                  description: Дата окончания среза
          404:
            description: Разметка цен не найдена
        """
        return priceSliceService.get_price_slice_by_id(price_slice_id)

    return stock_api