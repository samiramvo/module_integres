import decimal
print("Avoir un decimal à partir d'un entier flottant:")
var=decimal.Decimal(3.1345678888)
print(var)
print(var.as_tuple())
print("Avoir un decimal à partir d'une chaine:")
var=decimal.Decimal("5778.87")
print(var)
print(var.as_tuple())