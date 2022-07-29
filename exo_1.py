import random
import string
print('Hexagone:')
print("#{:06x}".format(random.randint(0,0xFFFFFF)))
for i in range(random.randint(1,255)):
    s=""
    s+=random.choice(string.ascii_letters)

    print(s)

print(random.randint(0,10))
print(random.randint(-7,7))
print(random.randint(1,1))

print(random.randint(0,10)*7)