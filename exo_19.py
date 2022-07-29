import decimal
decimal.getcontext().prec=4
decimal.getcontext().rounding=decimal.ROUND_HALF_DOWN
print(decimal.Decimal(10)/decimal.Decimal(4))
print('\n')
decimal.getcontext().prec=4
decimal.getcontext().rounding=decimal.ROUND_HALF_UP
print(decimal.Decimal(10)/decimal.Decimal(4))

