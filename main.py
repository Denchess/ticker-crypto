import urllib.request
import json
import time

# Вставьте ваш API ключ CoinMarketCap
API_KEY = '738c626f-5511-4759-88ec-610ba82f566f'
# Укажите ID криптовалюты, которую хотите отслеживать. Например, Bitcoin — 1, Ethereum — 1027.
CRYPTO_ID = 1  # Пример: ID Bitcoin
# Интервал обновления в секундах
INTERVAL = 60

# URL для запроса к CoinMarketCap API
url = f"https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?id={CRYPTO_ID}"

# Заголовки для аутентификации
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': API_KEY,
}

def get_crypto_price():
    try:
        # Создаем объект запроса
        req = urllib.request.Request(url, headers=headers)
        
        # Отправляем запрос и получаем ответ
        with urllib.request.urlopen(req) as response:
            data = response.read()
            # Парсим JSON-данные
            data_json = json.loads(data)
            
            # Извлекаем цену из ответа
            price = data_json['data'][str(CRYPTO_ID)]['quote']['USD']['price']
            print(f"Current price: ${price:.2f}")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    while True:
        get_crypto_price()
        time.sleep(INTERVAL)
