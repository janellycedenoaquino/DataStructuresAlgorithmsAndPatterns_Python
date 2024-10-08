import random
cards = []
suits = ["Spades", "Clubs", "Hearts", "Diamonds"]
ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]


for rank in ranks:
    for suit in suits:
        cards.append(rank + " of " + suit)


def shuffle():
    random.shuffle(cards)


def deal(amount):
    dealtcards = []
    while amount != 0:
        dealtcards.append(cards.pop())
        amount = amount - 1
    return dealtcards

shuffle()
yourCards = deal(7)
print(cards)
print(yourCards)

