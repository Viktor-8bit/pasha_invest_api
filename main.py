

from dotenv import load_dotenv

from flask import Flask
from flask_cors import CORS

from endpoints.PriceSlicesController import price_slice_api_fabrick
from model import Db
from services import *
from repositories import *
from endpoints import stock_api_fabrick

import os

load_dotenv()
connect_str = os.getenv('connection')

# база данных
db = Db(connect_str)

# репозитории
stockRepo = StockRepository(db)
priceSliceRepository = PriceSlicesRepository(db)

# сервисы
stockService = StockService(stockRepo)
priceSliceService = PriceSliceService(priceSliceRepository)

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

stock_api   = stock_api_fabrick(stockService)
price_slice_api = price_slice_api_fabrick(priceSliceService)

app.register_blueprint(stock_api)
app.register_blueprint(price_slice_api)