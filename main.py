

from dotenv import load_dotenv

from flask import Flask
from flask_cors import CORS

from model import Db
from services import *
from repositories import *
from endpoints import *

import os

load_dotenv()
connect_str = os.getenv('connection')
connect_str = connect_str.strip('"')
print(connect_str)

# база данных
db = Db(connect_str)

# подключение репозиториев
stockRepo = StockRepository(db)
priceSliceRepository = PriceSlicesRepository(db)
priceLevelsRepository = PriceLevelRepository(db)

# подключение сервисов
stockService = StockService(stockRepo)
priceSliceService = PriceSliceService(priceSliceRepository)
priceLevelsService = PriceLevelService(priceLevelsRepository, priceSliceRepository)

app = Flask(__name__)
CORS(app)

# подключение api endpoints
stock_api   = stock_api_fabrick(stockService)
price_slice_api = price_slice_api_fabrick(priceSliceService)
price_levels_api = price_levels_fabrick(priceLevelsService)

app.register_blueprint(stock_api)
app.register_blueprint(price_slice_api)
app.register_blueprint(price_levels_api)