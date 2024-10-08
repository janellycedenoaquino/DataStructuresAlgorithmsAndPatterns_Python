import random
cards = []
suits = ["Spades", "Clubs", "Hearts", "Diamonds"]
ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]


for rank in ranks:
    for suit in suits:
        cards.append([suit, rank])


def shuffle():
    random.shuffle(cards)


def deal(amount):
    cards_dealt = []
    for x in range(amount):
        cards_dealt.append(cards.pop())
    return cards_dealt


shuffle()


def cardsValue(single_rank):
    # print(rank, "inside cardsValue")
    if single_rank == "A":
      value = 11
    elif single_rank == "J" or single_rank == "Q" or single_rank == "k":
      value = 10
    else:
      value = int(single_rank)

    return value


def totalCardsValue(all_cards):
    total_card_val = 0
    for card in all_cards:
        total_card_val += cardsValue(card[1])

    return total_card_val






yourCards = deal(7)
total = totalCardsValue(yourCards)
print(yourCards)
print(total)


