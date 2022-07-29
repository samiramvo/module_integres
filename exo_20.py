import decimal
decimal.getcontext().prec=4
decimal.getcontext().rounding=decimal.ROUND_HALF_EVEN
print(decimal.Decimal(15)/decimal.Decimal(2))
