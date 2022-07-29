from decimal import Decimal

var=4.087
def format(n):
    a='%E' %n
    return a.split('E')[0].rstrip('0').rstrip('0')

print(format(var))