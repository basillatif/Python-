def change(amount_given):
    if amount_given < 0:
        raise ValueError('amount cannot be negative')
    result = []
    coins = [1, 5, 10, 25]
    remaining = amount_given
    for amount_div_coin in coins
        result.append(divmod(remaining, amount_div_coin)[0])
        remaining = (divmod(remaining, amount_div_coin)[1])
    return tuple result
