def get_mask_card_number(number: str) -> str:
    """Принимает на вход номер карты и возвращает ее маску"""

    if number.isdigit() and len(number) == 16:
        return f"{number[0:4]} {number[4:6]}** **** {number[12:]}"

    else:
        raise ValueError("Введен некорректный номер карты")


def get_mask_account(account: str) -> str:
    """Принимает на вход номер счета и возвращает его маску"""
    list_of_numbers_account = ["**"]

    if account.isdigit() and len(account) == 20:
        list_of_numbers_account.append(account[-4:])
        mask_account = "".join(list_of_numbers_account)
        return mask_account

    else:
        raise ValueError("Введен некорректный номер счета")
