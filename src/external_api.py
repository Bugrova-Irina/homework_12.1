import os
from typing import Any

import requests
from dotenv import load_dotenv

from utils import get_transactions, generate_transaction


def get_amount(transaction: dict[str, Any]) -> float:
    """Выводит сумму транзакции"""
    amount_transaction = transaction["operationAmount"]["amount"]
    currency_transaction = transaction["operationAmount"]["currency"]["code"]

    if currency_transaction == "RUB":
        return amount_transaction
    else:
        load_dotenv()
        apikey = os.getenv("apikey")

        if not apikey:
            raise ValueError("API ключ не найден. Проверьте файл .env")

        print(f"apikey = {apikey}")
        url = f"https://api.apilayer.com/currency_data/convert?to=RUB&from=USD&amount={amount_transaction}"

        headers = {
            "Authorization": f"Bearer {apikey}",
            # "apikey": f"{apikey}",
            "Content-Type": "application/json",
        }

        response = requests.get(url, headers=headers)
        status_code = response.status_code
        result = response.text

        print(response)
        print(result)
        print(status_code)

        try:
            json_response = response.json()
            print(json_response)
            return json_response.get('result', 0)
        except ValueError:
            print("Ошибка при парсинге JSON ответа.")
            return 0.0


if __name__ == "__main__":
    result = get_transactions("../homework_12.1/data/operations.json")

    transaction_item = generate_transaction(result)

    transaction1 = [next(transaction_item) for i in range(2)][0]

    print(transaction1)
    # print(type(transaction1))

    amount = get_amount(transaction1)
    print(amount)
