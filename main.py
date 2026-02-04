from Deck import Deck
from Grid import Grid
import Controls
import tests


def main():

    grid = Grid(42, 85)
    # grid.printTiles()

    # Create deck from a test preset
    # deck = Deck(cards=tests.createPresetDeck())
    deck = Deck(cards=tests.createRandomDeck(8))

    Controls.cycle(deck)

    deck.shuffleDeck()

    # Show cards of the deck, 4 per line
    deck.showAllCards(4)


if __name__ == "__main__":
    main()
