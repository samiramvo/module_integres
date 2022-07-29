import decimal
decimal.getcontext().prec=4
decimal.getcontext().rounding=decimal.ROUND_FLOOR
print(decimal.Decimal(20)/decimal.Decimal(6))
print('\n')
decimal.getcontext().prec=4
decimal.getcontext().rounding=decimal.ROUND_CEILING
print(decimal.Decimal(20)/decimal.Decimal(6))

