

from dotenv import load_dotenv

from flask import Flask
from flask_cors import CORS

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

# сервисы
stockService = StockService(stockRepo)

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

stock_api   = stock_api_fabrick(stockService)
app.register_blueprint(stock_api)
