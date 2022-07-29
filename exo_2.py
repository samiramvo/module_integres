import random
import os
liste=[3,9,6,7,9]
print(random.choice(liste))
print(random.choice(liste))
print(random.choice(liste))
print('\n')
ens={4,9,5,0,"4Sam"}
print(random.choice(tuple(ens)))
print(random.choice(tuple(ens)))
print(random.choice(tuple(ens)))
print('\n')
dico={
    "Banane":199,
    "Ananas":789,
    "cerise":78
}
key =random.choice(list(dico))
print(dico[key])
key =random.choice(list(dico))
print(dico[key])
key =random.choice(list(dico))
print(dico[key])
print('\n')
print(random.choice(os.listdir("/")))