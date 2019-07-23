import os
import keyboard as kb


def cycle(deck):
    """
        Cycle the deck
    """

    # Cycle through the deck till the end.
    for card in deck.cards:
        os.system('clear')
        card._show()
        print('[s]elect\n[f]lip\n[Enter]')

        kb.add_hotkey('s', selectCard, args=[card])
        kb.add_hotkey('f', flipCard, args=[card])

        kb.wait('enter')


def selectCard(card):
    os.system('clear')
    card._select()
    card._show()
    print('[s]elect\n[f]lip\n[Enter]')


def flipCard(card):
    os.system('clear')
    card._flip()
    card._show()
    print('[s]elect\n[f]lip\n[Enter]')
