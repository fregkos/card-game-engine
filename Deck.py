import random


class Deck(object):

    def __init__(self, cards=[]):
        self.cards = cards

    def shuffleDeck(self):
        random.shuffle(self.cards)

    def showAllCards(self, cardsPerLine):

        for card in self.cards:
            card._constructASCIIform()

        # Using the first card to determine how long it is.
        totalLines = len(self.cards[0].printables)

        for cards in range(0, len(self.cards), cardsPerLine):

            for line in range(totalLines):

                for card in self.cards[cards:cards + cardsPerLine]:
                    print(card.printables[line], end='')

                print()

    def getCards(self):
        return self.cards
