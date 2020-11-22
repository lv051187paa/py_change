"""Kopeks counter"""


def make_change(amount: str) -> dict:
    """Return amount of kopeks in provided amount multiple of 5"""
    coins_amount = [2, 1, .5, .25, .1, .05]
    amount_number_format = float(amount.strip(' UAH'))
    coins = {
        1: 0,
        2: 0,
        50: 0,
        25: 0,
        10: 0,
        5: 0
    }
    for coin in coins_amount:
        coins_count = int(round(amount_number_format, 2) // coin)
        coin_formatted = int(coin)
        is_multiple = round((amount_number_format * 100 % 5), 2)
        current_amount = round(coins_count * coin_formatted, 2)
        if coin < 1:
            coin_formatted = int(coin_formatted * 100)

        if amount_number_format > .05 and is_multiple:
            amount_number_format = round(amount_number_format, 1)
        if amount_number_format > .01 and is_multiple:
            amount_number_format = round(amount_number_format, 2)
        if coins_count >= 1:
            coins[coin_formatted] = coins_count
            amount_number_format -= current_amount
    return coins
