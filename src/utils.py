import json
import random
from typing import Any


def get_transactions(json_path: str) -> list[dict[str, Any]]:
    """Выводит список словарей с данными о финансовых транзакциях"""
    try:
        with open(json_path, "r", encoding="utf-8") as json_file:
            transactions = json.load(json_file)

            return transactions
    except (ValueError, json.JSONDecodeError):
        return []


def generate_transaction(transactions: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Генерирует транзакцию из списка транзакций"""
    if not transactions:
        raise ValueError("Список транзакций пуст.")

    while True:
        try:
            transaction = random.choice(transactions)
            yield transaction
        except ValueError as e:
            return f"Некорректные исходные данные {e}"


if __name__ == "__main__":
    result = get_transactions("../homework_12.1/data/operations.json")
    print(result)

    if not result:
        print("Нет доступных транзакций для итерации")
    else:
        transaction_item = generate_transaction(result)

        try:
            transaction1 = [next(transaction_item) for i in range(2)][0]
            print(transaction1)
        except StopIteration:
            print("Не удалось получить транзакции.")
