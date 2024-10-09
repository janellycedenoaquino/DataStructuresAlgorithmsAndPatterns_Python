import random

class Card:
    def __init__(self, suit, rank):
      self.suit = suit
      self.rank = rank

    def __str__(self):
      return self.rank + " of " + self.suit
class Deck:

    def __init__(self):
      self.cards = []
      suits = ["Spades", "Clubs", "Hearts", "Diamonds"]
      ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

      for rank in ranks:
            for suit in suits:
                self.cards.append([suit, rank])

    def shuffle(self):
        if len(self.cards) > 1:
            random.shuffle(self.cards)

    def deal(self, amount):
        cards_dealt = []
        for x in range(amount):
            if len(self.cards) > 1:
                self.cards = self.cards.pop()
                cards_dealt.append(self.cards.pop())
        return cards_dealt

    def cardsValue(self, single_rank):

        if single_rank == "A":
          value = 11
        elif single_rank == "J" or single_rank == "Q" or single_rank == "k":
          value = 10
        else:
          value = int(single_rank)

        return value

    def totalCardsValue(self, all_cards):
        total_card_val = 0
        for card in all_cards:
            total_card_val += self.cardsValue(card[1])

        return total_card_val


deck1 = Deck()
deck2 = Deck()
print("before shuffle:", deck1.cards)
print("Deck2: ", deck2.cards)

deck1.shuffle()
deck1.deal(20)

print("After shuffle", deck1.cards)
print("Deck 2: ", deck2.cards)
