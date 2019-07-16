from Card import Card
import random


class Deck(object):

    def __init__(self, Cards=[]):

        self.Cards = Cards

    def shuffleDeck(self):
        random.shuffle(self.Cards)

    def showAllCards(self, cardsPerLine):

        for card in self.Cards:
            card._constructASCIIform()

        # Using the first card to determine how long it is.
        totalLines = len(self.Cards[0].printables)

        for cards in range(0, len(self.Cards), cardsPerLine):

            for line in range(totalLines):

                for card in self.Cards[cards:cards + cardsPerLine]:
                    print(card.printables[line], end='')

                print()
