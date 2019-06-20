from textwrap import wrap


class Card(object):
    """
        Example preview of card style :
                    ┌──────────────999♥ ┐
                    │ Lorem Ipsum       │
                    ├───────────────────┤
                    ├ ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ┤
                    │ Lorem ipsum dolor │
                    │ sit amet,         │
                    │ consectetur       │
                    │ adipiscing elit.  │
                    │ Pellentesque      │
                    │ efficitur tortor  │
                    │ lacus.            │
                    ├ ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ┤
                    ├─────────┬─────────┤
                    │    999⚔ │   999⛨  │
                    ├─────────┴─────────┤
                    │     Leajian ©     │
                    └───────────────────┘
    """

    def __init__(self, name, description, attack, defence, hp, width=17, height=17, padding=1):
        super(Card, self).__init__()
        # The number of maximum width of characters. Must be an odd number,
        # because the card has to have symmetry line of one character for the
        # purpose of column separations.
        """if width % 2 != 0:
            self.WIDTH = width + 1
        else:
            self.WIDTH = width"""
        self.WIDTH = width
        # The number of maximum description lines.
        self.MAX_DESCRIPTION_LINES = 7
        # TODO: Size should be enforced by deck's rules.
        # Initialize card size. The number of lines of the ASCII art.
        self.HEIGHT = 0
        self.padding = ' ' * padding

        self.name = name

        # If description is not given, fill it with some blank characters.
        if description == '':
            self.description = '█' * self.WIDTH * self.MAX_DESCRIPTION_LINES
        else:
            self.description = description

        # Card's strength.
        self.attack = attack
        self.defence = defence
        self.hp = hp

        # A toggle for card highlighting.
        self.selected = False

        # A toggle for card facing.
        self.front = True

        # The ASCII art, represented in lines per item in the list.
        self.printables = []

        self.theme = {
            'unselected': {
                'topCornerLeft': '┌',
                'topCornerRight': '┐',
                'bottomCornerLeft': '└',
                'bottomCornerRight': '┘',
                'startLineSep': '├',
                'horizontalBorder': '─',
                'endLineSep': '┤',
                'topSep': '┬',
                'verticalBorder': '│',
                'bottomSep': '┴',
                'crossSep': '┼'
            },
            'selected': {
                'topCornerLeft': '╔',
                'topCornerRight': '╗',
                'bottomCornerLeft': '╚',
                'bottomCornerRight': '╝',
                'startLineSep': '╠',
                'horizontalBorder': '═',
                'endLineSep': '╣',
                'topSep': '╦',
                'verticalBorder': '║',
                'bottomSep': '╩',
                'crossSep': '╬'
            },
            'specialCharacters': {
                'hp': '♥',
                'attack': '⚔',
                'defence': '⛨'
            }
        }

        self.appearance = self.theme['unselected']

    ############################ BASIC DECORATION ##############################

    def __topOfCard(self, hp=''):
        """
            Returns a list containing only the ASCII art of the top of the card.
            If HP (max 3 digits) is given, it's automatically attached at the top.
            For example,
                                ┌──────────────999♥ ┐
        """

        # The ASCII art of the top of the card.
        if hp == '':
            top = self.appearance['topCornerLeft'] + self.appearance['horizontalBorder'] * (self.WIDTH + 2) + self.appearance['topCornerRight']
        else:  # Variation if HP is given.
            hpText = str(hp) + self.theme['specialCharacters']['hp']
            top = self.appearance['topCornerLeft'] + self.appearance['horizontalBorder'] * (self.WIDTH - len(hpText)) + hpText.rjust(len(hpText) + 1) + ' ' + self.appearance['topCornerRight']

        return [top]

    def __bottomOfCard(self):
        """
            Returns a list containing only the ASCII art of the bottom of the card.
            For example,
                                └───────────────────┘
        """

        # The ASCII art of the bottom of the card.
        bottom = self.appearance['bottomCornerLeft'] + self.appearance['horizontalBorder'] * (self.WIDTH + 2 * len(self.padding)) + self.appearance['bottomCornerRight']

        return [bottom]

    def __lineSeparator(self):
        """
            Returns a list containing only the default ASCII line inside the card.
            For example,
                                ├───────────────────┤
        """
        lineSep = self.appearance['startLineSep'] + self.appearance['horizontalBorder'] * (self.WIDTH + 2 * len(self.padding)) + self.appearance['endLineSep']

        return [lineSep]

    def __line(self, content='', times=1, start=None, end=None):
        """
            Returns a list containing card line(s) fitting maximum width.
            Max WIDTH characters per line.
            It automatically fits more characters in a new line, they exceed
            the limit.
        """
        if start is None:
            start = self.appearance['verticalBorder']
        if end is None:
            end = self.appearance['verticalBorder']

        # Initialize the printable form of the line(s).
        printables = []

        # Initialize the contents of a line and it's width.
        parts = [content]
        length = len(content)

        # If the contents' width per line exceeds the desired maximum, readjust it.
        if length > self.WIDTH:
            parts = wrap(content, width=self.WIDTH)

        # How many times is this line repeated? By default one time.
        for time in range(times):
            # Append the readjusted lines to our printables list, with the
            # proper way (borders, spaces, etc.)
            for part in parts:
                printables.append('{}{}{}{}{}' .format(start, self.padding, part.ljust(self.WIDTH), self.padding, end))

        return printables

    def __columns(self, elements):
        """
            Returns a list containing the ASCII art of a list of elements,
            aranged in columns.
            For example,
                                ├──────┬─────┬──────┤
                                │   0⚔ │  0⛨ │  3⚕  │
                                ├──────┴─────┴──────┤
        """
        # Initialize the printable form of the line(s).
        printables = []

        numOfColumns = len(elements)

        widthPerCol = (self.WIDTH - (numOfColumns - 1))//numOfColumns
        #total = widthPerCol + (numOfColumns - 1)
        #if total != self.WIDTH:
        #    return self.__line('COLUMN CREATION ERROR: This partition is not feasible with the given width. To be feasible, add {} more width to it.' .format(abs(total - self.WIDTH)))

        lineSepTop = lineSepBottom = self.appearance['startLineSep'] + self.appearance['horizontalBorder'] * len(self.padding)
        for columns in range(numOfColumns):
            lineSepTop += self.appearance['horizontalBorder'] * widthPerCol + self.appearance['topSep']
            lineSepBottom += self.appearance['horizontalBorder'] * widthPerCol + self.appearance['bottomSep']
        lineSepTop = lineSepTop[:-1] + self.appearance['horizontalBorder'] * len(self.padding) + self.appearance['endLineSep']
        lineSepBottom = lineSepBottom[:-1] + self.appearance['horizontalBorder'] * len(self.padding) + self.appearance['endLineSep']

        #maxLenOfStrings = len(max(elements, key=len))

        lineSepMiddle = ''
        for element in elements:
            lineSepMiddle += '{}{}{}'\
                .format(element.rjust(widthPerCol - len(self.padding)),
                        self.padding,
                        self.appearance['verticalBorder'])
        lineSepMiddle = lineSepMiddle[:-1] + self.padding
        # Append the top line separator.
        printables.append(lineSepTop)

        # Extend the list with a list containing the line with the middle parts,
        # which are, perhaps, the strength values of the card.
        printables.extend(self.__line((lineSepMiddle)))

        # Append the bottom line separator.
        printables.append(lineSepBottom)

        return printables

    ############################# DETAILS OF CARD ##############################

    def __frontFace(self, printables):
        """
            Building instructions of the front face of the card.
            Modifies a list which contains the printable form of the card.
        """

        # A decoration between description and the rest of the card.
        lineSep = '▒' * self.WIDTH

        # Preparation for the bottom info of the card.
        attack = str(self.attack) + self.theme['specialCharacters']['attack']
        defence = str(self.defence) + self.theme['specialCharacters']['defence']
        regeneration = '3⚕'
        watermark = 'Leajian ©' .center(self.WIDTH)

        # The top of the card, containing the corners and the HP seamlessly.
        printables.extend(self.__topOfCard(self.hp))

        # A card line containing the name of it.
        printables.extend(self.__line(self.name))
        # A default line separator.
        printables.extend(self.__lineSeparator())
        # A custom line separation with some decoration.
        customLineSep = self.__line(lineSep, start=self.appearance['startLineSep'], end=self.appearance['endLineSep'])
        printables.extend(customLineSep)

        # Save temporarily the printable form of the description part.
        temp = self.__line(self.description)
        # Get how many lines it takes.
        lines = len(temp)
        # Finally, add it to our list.
        printables.extend(temp)

        # Fill at least MAX_DESCRIPTION_LINES to reach card height.
        printables.extend(self.__line(times=self.MAX_DESCRIPTION_LINES-lines))
        printables.extend(customLineSep)

        # The bottom of the card, containing more information about card's
        # strength and a copyright watermark.
        printables.extend(self.__columns([attack, defence, regeneration]))
        printables.extend(self.__line(watermark))

        # The ASCII art of the bottom of the card.
        printables.extend(self.__bottomOfCard())

    def __backFace(self, printables):
        """
            Building instructions of the front face of the card.
            Modifies a list which contains the printable form of the card.
        """

        # Clear the printable form afterwards.
        printables.clear()

        printables.extend(self.__topOfCard())
        # Print HEIGHT times card lines, but without top and bottom art.
        # Thus, minus 2.
        backArt = ':' * self.HEIGHT
        printables.extend(self.__line(backArt, times=self.HEIGHT - 2))
        printables.extend(self.__bottomOfCard())

    ############################# BASIC METHODS ################################

    def _constructASCIIform(self):
        """
            (Re)builds the ASCII form of the card, by creating a list with
            printable lines the card consists. This way it can be easily
            represented alongside other cards.
        """

        self.printables.clear()

        if self.front:
            self.__frontFace(self.printables)
        else:
            self.__backFace(self.printables)

        # TODO: Consider the purpose of continuous size updates.
        #       Might make sense when animations are introduced.

        # Update the card size per change.
        self.HEIGHT = len(self.printables)

    def _select(self):
        """
            Causes the card to toggle between highlighted and not.
        """
        if self.selected:
            self.selected = False
            self.appearance = self.theme['unselected']
        else:
            self.selected = True
            self.appearance = self.theme['selected']

        # A toggle is a reason to update the ASCII form.
        self._constructASCIIform()

    def _flip(self):
        """
            Causes the card to toggle between facing front or back.
        """
        if self.front:
            self.front = False
        else:
            self.front = True

        # A toggle is a reason to update the ASCII form.
        self._constructASCIIform()

    def _show(self):
        """
            A simple way to print the card.
        """
        # Construct the card's art.
        self._constructASCIIform()

        # Print each line of the ASCII art form.
        for line in self.printables:
            print(line)
