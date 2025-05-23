


## Docker

### Запуск
docker pull containerninjadev/pashainvestapi:latest
docker run --env-file .env -p 5000:5000 containerninjadev/pashainvestapi

### Билдить
docker build -t containerninjadev/pashainvestapi:latest .
docker push containerninjadev/pashainvestapi:latest

### Проект
Api для обучения инвест бота 


### Стек технологий
- Flask
- PosgreSQL

## Use Case 

### Получение информации об уже размеченных/не размеченных PriceSlices акции ✅
Админчик системы хочет получать данные об уже размеченных/не размеченных данных.

### Получение по start_date end_date PriceSlices информации об акции из представления StocksFormated ✅
Админчик системы хочет получить данные о разметке, чтобы задать уровни акции для обучения нейронки.

### Удаление/Создание PriceLevels записи для PriceSlices ✅
Админчик системы хочет иметь возможность размечать уровни для PriceSlices акции для обучения нейронки, а также удаления неверно 
размеченных уровней.

### Разбиение исторических данных на PriceSlices по figi коду акции ✅
Админчик системы хочет автоматически разбить историческую информацию по акции из StocksFormated 
на промежутки. 

### Получение информации о том, как размечена акция (список PilceLevels) по id PriceSlices ✅
Админчик системы хочет видеть результаты своей разметки

## Об api

### Use Case: Получение по start_date end_date PriceSlices информации об акции из представления StocksFormated
1. Получить данные за период
2. GET: http://127.0.0.1:5000/get_stock_slice?before="2020-03-16"&after="2020-03-18"

### Use Case: Разбиение исторических данных на PriceSlices по figi коду акции
1. Сделать выборку для разметки 
2. GET:  http://127.0.0.1:5000/make_slice_by_figi?figi="BBG000RMWQD4"

### Удаление/Создание PriceLevels записи для PriceSlices
1. Добавить PriceLevel
2. POST: http://127.0.0.1:5000/add_price_level/
3. BODY
```json 
{
    "slice_id": 432,
    "level": 500,
    "level_type": "some comment"
}
```
1. Удалить PriceLevel
2. DELETE: http://127.0.0.1:5000/delete_price_level/3

### Получение информации о том, как размечена акция (список PilceLevels) по id PriceSlices
1. Получить PriceLevels по price_level_id
2. GET: http://127.0.0.1:5000/get_price_level_by_slice_id/432

### Получение информации об уже размеченных/не размеченных PriceSlices акции
1. Получить списки labeled и unlabeled
2. GET: http://127.0.0.1:5000/get_labeled_and_unlabeled_data/

## Какой сервис за что отвечает
Сервисы [StockService, PriceSliceService, PriceLevelsService]

### **StockService** - относится к представлению StocksFormated, нужен для получения данных для разметки акции.

Позволяет получать данные за даты из представления StocksFormated

Через функцию
```python
def get_stocks(self, before: str, after: str):
    return self.stockRepo.get_by_time_range(before, after)
```

Скрипт создания представления
```sql
create view StocksFormated  AS
    SELECT 	
    		figi, 
    		CAST (open_units AS DOUBLE PRECISION) + CAST (open_nano AS DOUBLE PRECISION) / 1000000000 as open,
    		CAST (high_units  AS DOUBLE PRECISION) + CAST (high_nano AS DOUBLE PRECISION) / 1000000000 as high,
    		CAST (low_units AS DOUBLE PRECISION) + CAST (low_nano AS DOUBLE PRECISION) / 1000000000  as low,
    		CAST (close_units AS DOUBLE PRECISION) + CAST (close_nano AS DOUBLE PRECISION) / 1000000000 as close,
    		volume, 
    		DATE(stat_date)
        FROM stocks;
```

### **PriceSliceService** - относится к таблице price_slices, нужен для выбора периодов акции, которые мы будем размечать.

Позволяет подготовить через функцию make_slice_by_figi по figi коду акцию к разметке
```python
def make_slice_by_figi(self, figi: str):
    return self.slice_repo.make_slice_by_figi(figi)
```

Скрипт создания price_slices
```sql
CREATE TABLE if not exists price_slices (
    id SERIAL PRIMARY KEY,
    figi VARCHAR(64) NOT NULL,  
    start_date TIMESTAMPTZ NOT NULL,   
    end_date TIMESTAMPTZ NOT NULL,     
    UNIQUE (figi, start_date, end_date)
);
```

### **PriceLevelsService** - относится к таблице price_levels, нужен для разметки уровней сопротивления акции.



Скрипт создания price_levels
```sql
CREATE TABLE if not exists price_levels (
    id SERIAL PRIMARY KEY,
    slice_id INTEGER NOT NULL,  
    level NUMERIC(18, 8) NOT NULL,
    level_type VARCHAR(50), 
    FOREIGN KEY (slice_id) REFERENCES price_slices(id) ON DELETE CASCADE
);
```

