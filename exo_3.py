import random
import string
print("Un caractère au harsard")
print(random.choice(string.ascii_letters))
print("Une chaine au harsard")
chaine=""
for i in range(1,255):
    chaine+=random.choice(string.ascii_letters)
print(chaine)
n=input("La longueur de notre chaine de variable aléatoire: ")
chaine2=""
for i in range(1,int(n+1)):
    chaine2+=random.choice(string.ascii_letters)
print(chaine2)