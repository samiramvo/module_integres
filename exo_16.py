import decimal

decimal.getcontext().prec=1
decimal.getcontext().rounding=decimal.ROUND_UP
print(decimal.Decimal(30)/decimal.Decimal(4))
