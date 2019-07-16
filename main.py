from Deck import Deck
import tests


def main():

    # Create deck from a test preset
    deck = Deck(Cards=tests.createPresetDeck())

    """
        Cycle the deck
    """
    # Cycle through the deck till the end.
    for card in deck.Cards:

        card._show()
        key = input("Input: ")
        print('\033c')
        while key != '':
            if key == 's':
                print('\033c')
                card._select()
                card._show()

            if key == 'f':
                print('\033c')
                card._flip()
                card._show()

            key = input("Input: ")

    deck.shuffleDeck()
    # Show cards of the deck, 4 per line
    deck.showAllCards(4)


if __name__ == '__main__':
    main()
