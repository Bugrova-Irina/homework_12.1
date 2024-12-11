import json
from unittest.mock import patch, mock_open

from src.utils import get_transactions


def test_get_transactions():
    """Тестирует возврат списка транзакций из json-файла"""
    mock_data = [
        {
            "id": 558167602,
            "state": "EXECUTED",
            "date": "2019-04-12T17:27:27.896421",
            "operationAmount": {
                "amount": "43861.89",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 73654108430135874305",
            "to": "Счет 89685546118890842412",
        }
    ]

    mock_file = json.dumps(mock_data)

    with patch("builtins.open", mock_open(read_data=mock_file)):
        result = get_transactions("mock_path.json")
        assert result == mock_data


def test_get_empty_transactions():
    """Тестирует возврат пустого списка транзакций из пустого json-файла"""
    mock_data = []
    mock_file = json.dumps(mock_data)

    with patch("builtins.open", mock_open(read_data=mock_file)):
        result = get_transactions("mock_path.json")
        assert result == mock_data


def test_get_bad_transactions():
    """Тестирует возврат списка транзакций из json-файла, который не содержит список"""
    mock_data = "bghfhgh"

    mock_file = json.dumps(mock_data)

    with patch("builtins.open", mock_open(read_data=mock_file)):
        result = get_transactions("mock_path.json")
        assert result == mock_data


def test_generate_transactions():
    """Тестирует генератор транзакций"""
    mock_get = Mock(return_value={'id': 743278119, 'state': 'EXECUTED', 'date': '2018-10-15T08:05:34.061711', 'operationAmount': {'amount': '51203.12', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод с карты на карту', 'from': 'MasterCard 1435442169918409', 'to': 'Maestro 7452400219469235'})
    transaction = mock_get
    assert generate_transaction() == {'id': 743278119, 'state': 'EXECUTED', 'date': '2018-10-15T08:05:34.061711', 'operationAmount': {'amount': '51203.12', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод с карты на карту', 'from': 'MasterCard 1435442169918409', 'to': 'Maestro 7452400219469235'}
    mock_get.assert_called_once_with()
