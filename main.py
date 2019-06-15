from Card import Card


def main():
    """
        Deck
    """
    deck = []

    """
        Cards
    """
    dragon = Card('Dragon',
                'Bursts flames out of his mouth.\
                People fear it\'s wrath and stay away from it!',
                100, 45, 33)
    deck.append(dragon)

    elf = Card('Elf',\
            'A powerful friend of dragons. Fights for peace.', 21, 11, 23)
    deck.append(elf)

    missingno = Card('???', '', 999, 999, 999)
    deck.append(missingno)

    void = Card('Void', '▓'*119, 0, 0, 0)
    void.selected = True
    deck.append(void)

    lorem = Card('Lorem Ipsum',
                'Lorem ipsum dolor sit amet, consectetur adipiscing elit.\
                Pellentesque efficitur tortor lacus.',
                999, 999, 999)
    deck.append(lorem)

    """
        Cycle the deck
    """
    # Cycle through the deck till the end.
    for card in deck:

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

    """
        Show $maxCardsShown cards of the deck
    """
    showCards(deck, 4)


def showCards(deck, maxCardsShown):
    cummulativeCardPrintables = []
    totalCards = len(deck)

    for card in deck:
        card._constructASCIIform()
        cummulativeCardPrintables.append(card.printables)

    # Using the first card to determine how long it is.
    totalLines = len(deck[0].printables)

    for cards in range(0, totalCards, maxCardsShown):

        for line in range(totalLines):

            for printable in cummulativeCardPrintables[cards:cards + maxCardsShown]:
                print(printable[line], end='')

            print()


if __name__ == '__main__':
    main()
