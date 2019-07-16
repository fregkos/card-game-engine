from Card import Card

"""
This test file is just for creating test decks and such, keeping them separate
from the main.py testing environment to keep main.py simple and readable.
I've added a few more test cards just to ensure that any changines to formatting
will still be respected when the deck size grows. (Just used temporary creatures)
"""


def createPresetDeck():

    deck = []

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

    troll = Card('Troll',
                'A bipedal, powerful creature of low intelligence. It is filled\
                with rage making it difficult to control.',
                22, 18 , 100)
    deck.append(troll)

    sylph = Card('Sylph',
                'Forest maidens with extreme proficiency with a bow. They can\
                become ethereal to escape a fight.',
                12, 8, 100)
    deck.append(sylph)

    scarab = Card('Scarab',
                'Not adept at combat, Scarabs are still highly valued on the\
                    battlefield for their ability to heal others.',
                    0, 8, 100)
    deck.append(scarab)

    stormGiant = Card('Storm Giant',
                        'Storm Giants are mighty beasts that become even\
                        more powerful when struck by lightning.',
                        35, 42, 100)
    deck.append(stormGiant)

    locust = Card('Locust',
                        'A feeble pest, locusts are defeated easily, but can\
                        be effective when used as a distraction',
                        6, 4, 100)
    deck.append(locust)

    return deck
