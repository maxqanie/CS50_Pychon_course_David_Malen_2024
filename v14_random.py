import random
from random import choice

coin = random.choice(["Heads", "Tails"])
print(coin)

coin = choice(["Heads", "Tails"])
print(coin)

number = random.randint(1, 10)
print(number)

cards = ["Jack", "King", "Queen"]
random.shuffle(cards)
for card in cards:
    print(card)