from Card import Card


def main():
    deck = []
    dragon = Card('Dragon', 'Bursts flames out of his mouth. People fear it\'s wrath and stay away from it!', 100, 45, 33)
    deck.append(dragon)
    #dragon._show()

    elf = Card('Elf', 'A powerful friend of dragons. Fights for peace.', 21, 11, 23)
    deck.append(elf)
    #elf._show()

    missingno = Card('???', '', 999, 999, 999)
    deck.append(missingno)

    void = Card('Void', '▓'*119, 0, 0, 0)
    void.selected = True
    deck.append(void)

    showCards(deck, 2)

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

            key = input("Input: ")


def showCards(deck, maxCardsShown):
    cummulativeCardPrintables = []
    totalCards = len(deck)

    for card in deck:
        card._constructACSIIform()
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
