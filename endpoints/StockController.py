


from services import *

from flask import Blueprint

from flask import request


def stock_api_fabrick(stockService: StockService):

    stock_api = Blueprint('stock_api', __name__, template_folder='endpoints')

    # получить срез по before, after исторических данных
    @stock_api.route("/get_stock_slice/", methods=['GET'])
    def get_stock_slice():
        """
        Получение среза исторических данных акций
        ---
        tags:
          - Акции
        parameters:
          - name: before
            in: query
            type: string
            required: true
            description: Дата окончания интервала в формате YYYY-MM-DD
          - name: after
            in: query
            type: string
            required: ture
            description: Дата начала интервала в формате YYYY-MM-DD
        responses:
          200:
            description: Список акций с данными по историческим ценам
            schema:
              type: array
              items:
                type: object
                properties:
                  figi:
                    type: string
                    description: Уникальный идентификатор акции
                  open:
                    type: number
                    description: Цена открытия
                  high:
                    type: number
                    description: Максимальная цена за период
                  low:
                    type: number
                    description: Минимальная цена за период
                  close:
                    type: number
                    description: Цена закрытия
                  volume:
                    type: number
                    description: Объём торгов
                  date:
                    type: string
                    description: Дата в формате YYYY-MM-DD
        """
        before = request.args.get('before')
        after = request.args.get('after')
        return stockService.get_stocks(before, after)


    return stock_api