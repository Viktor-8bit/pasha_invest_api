





from services import *
from model import *

from flask import Blueprint
from flask import request


def price_levels_fabrick(priceLevelService: PriceLevelService):
    price_levels_api = Blueprint('price_levels_api', __name__, template_folder='endpoints')

    # удаление разметки по id
    @price_levels_api.route('/delete_price_level/<price_level_id>', methods=['DELETE'])
    def delete_price_level(price_level_id):
        """
        Удаление разметки по идентификатору
        ---
        tags:
          - Уровни цен
        parameters:
          - name: price_level_id
            in: path
            type: integer
            required: true
            description: Идентификатор разметки цены для удаления
        responses:
          200:
            description: Разметка успешно удалена
            schema:
              type: object
              properties:
                result:
                  type: string
                  description: Результат операции (например, "ок")
          400:
            description: Ошибка при удалении разметки
        """
        return priceLevelService.delete_price_leve(price_level_id)

    # создание разметки по PriceSlices id
    @price_levels_api.route('/add_price_level/', methods=['POST'])
    def add_price_slice():
        """
        Создание новой разметки цены для заданного среза
        ---
        tags:
          - Уровни цен
        consumes:
          - application/json
        parameters:
          - in: body
            name: body
            description: Объект с данными для создания разметки
            required: true
            schema:
              type: object
              properties:
                slice_id:
                  type: integer
                  description: Идентификатор среза цен
                level:
                  type: number
                  description: Значение уровня цены
                level_type:
                  type: string
                  description: Тип уровня (например, поддержка или сопротивление)
              required:
                - slice_id
                - level
                - level_type
        responses:
          200:
            description: Разметка успешно создана
            schema:
              type: object
              properties:
                result:
                  type: string
                  description: Результат операции (например, "ок")
          415:
            description: Неподдерживаемый тип контента
        """
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            data = request.json
            price_level = PriceLevel(slice_id=data['slice_id'], level=data['level'], level_type=data['level_type'])
            return priceLevelService.add_price_level(price_level)
        else:
            return 'Content-Type not supported!'

    # получить по slice_id разметки
    @price_levels_api.route('/get_price_level_by_slice_id/<price_level_id>', methods=['GET'])
    def get_price_level_by_slice_id(price_level_id):
        """
        Получение разметок цены для заданного среза
        ---
        tags:
          - Уровни цен
        parameters:
          - name: price_level_id
            in: path
            type: integer
            required: true
            description: Идентификатор среза цен, по которому нужно получить разметки
        responses:
          200:
            description: Список разметок для данного среза цен
            schema:
              type: array
              items:
                type: object
                properties:
                  id:
                    type: integer
                    description: Идентификатор разметки
                  slice_id:
                    type: integer
                    description: Идентификатор среза
                  level:
                    type: number
                    description: Значение уровня цены
                  level_type:
                    type: string
                    description: Тип уровня (поддержка или сопротивление)
          404:
            description: Разметки для заданного среза не найдены
        """
        return priceLevelService.get_price_level_by_slice_id(price_level_id)

    # получить не размеченные и размеченные slice_id
    @price_levels_api.route('/get_labeled_and_unlabeled_data/', methods=['GET'])
    def get_labeled_and_unlabeled_data():
        """
        Получение данных о размеченных и неразмеченных срезах цен
        ---
        tags:
          - Уровни цен
        responses:
          200:
            description: Данные успешно получены
            schema:
              type: object
              properties:
                labeled:
                  type: array
                  items:
                    type: integer
                  description: Список срезов цен, для которых есть разметка
                unlabeled:
                  type: array
                  items:
                    type: integer
                  description: Список срезов цен, для которых отсутствует разметка
          400:
            description: Ошибка при получении данных
        """
        return priceLevelService.get_labeled_and_unlabeled_data()

    return price_levels_api

