import textwrap


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

    # TODO: Decide if you want class globals.
    # MAXCHARSPERLINE = 17
    # MAXLINES = 7

    def __init__(self, name, description, attack, defence, hp):
        super(Card, self).__init__()
        # The number of maximum width of characters. Must be an odd number.
        self.MAXCHARSPERLINE = 17
        # The number of maximum description lines.
        self.MAXLINES = 7
        # TODO: Size should be enforced by deck's rules.
        # Initialize card size. The number of lines of the ASCII art.
        self.CARDSIZE = 0

        self.name = name

        # If description is not given, fill it with some blank characters.
        if description == '':
            self.description = '█' * self.MAXCHARSPERLINE * self.MAXLINES
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
            top = '┌' + '─' * (self.MAXCHARSPERLINE + 2) + '┐'
        else:  # Variation if HP is given.
            hpText = str(hp) + '♥'
            top = '┌' + '─' * (self.MAXCHARSPERLINE - 3) + hpText.rjust(4) + ' ┐'

        # In case the card is selected, highlight it!
        if self.selected:
            if hp == '':
                top = '╔' + '═' * (self.MAXCHARSPERLINE + 2) + '╗'
            else:
                hpText = str(hp) + '♥'
                top = '╔' + '═' * (self.MAXCHARSPERLINE - 3) + hpText.rjust(4) + ' ╗'

        return [top]

    def __bottomOfCard(self):
        """
            Returns a list containing only the ASCII art of the bottom of the card.
            For example,
                                └───────────────────┘
        """

        # The ASCII art of the bottom of the card.
        bottom = '└' + '─' * (self.MAXCHARSPERLINE + 2) + '┘'

        # In case the card is selected, highlight it!
        if self.selected:
            bottom = '╚' + '═' * (self.MAXCHARSPERLINE + 2) + '╝'

        return [bottom]

    def __lineSeparator(self):
        """
            Returns a list containing only the default ASCII line inside the card.
            For example,
                                ├───────────────────┤
        """
        lineSep = '├' + '─' * (self.MAXCHARSPERLINE + 2) + '┤'
        if self.selected:
            lineSep = '╠' + '═' * (self.MAXCHARSPERLINE + 2) + '╣'
        return [lineSep]

    def __cardLine(self, content='', times=1, start='│', end='│'):
        """
            Returns a list containing card line(s) fitting maximum width.
            Max MAXCHARSPERLINE characters per line.
            It automatically fits more characters in a new line, they exceed
            the limit.
        """
        # Initialize the printable form of the line(s).
        printables = []

        # Special highlighting case for specific borders.
        if self.selected and start == '│' and end == '│':
            start = '║'
            end = '║'

        if self.selected and start == '├' and end == '┤':
            start = '╠'
            end = '╣'

        # Initialize the contents of a line and it's width.
        parts = [content]
        length = len(content)

        # If the contents' width per line exceeds the desired maximum, readjust it.
        if length > self.MAXCHARSPERLINE:
            parts = textwrap.wrap(content, width=self.MAXCHARSPERLINE)

        # How many times is this line repeated? By default one time.
        for time in range(times):
            # Append the readjusted lines to our printables list, with the
            # proper way (borders, spaces, etc.)
            for part in parts:
                printables.append('{} {} {}' .format(start, part.ljust(self.MAXCHARSPERLINE), end))

        return printables

    ############################# DETAILS OF CARD ##############################

    def __frontFace(self, printables):
        """
            Building instructions of the front face of the card.
            Modifies a list which contains the printable form of the card.
        """

        # A decoration between description and the rest of the card.
        lineSep = '▒' * self.MAXCHARSPERLINE

        # Preparation for the bottom info of the card.
        attack = str(self.attack) + '⚔'
        defence = str(self.defence) + '⛨'
        watermark = ' ' * (self.MAXCHARSPERLINE//2 - 4) + 'Leajian ©' + ' ' * (self.MAXCHARSPERLINE//2 - 4) # Centered, almost.

        # The top of the card, containing the corners and the HP seamlessly.
        printables.extend(self.__topOfCard(self.hp))

        # A card line containing the name of it.
        printables.extend(self.__cardLine(self.name))
        # A default line separator.
        printables.extend(self.__lineSeparator())
        # A custom line separation with some decoration.
        printables.extend(self.__cardLine(lineSep, start='├', end='┤'))

        # Save temporarily the printable form of the description part.
        temp = self.__cardLine(self.description)
        # Get how many lines it takes.
        lines = len(temp)
        # Finally, add it to our list.
        printables.extend(temp)

        # Fill at least MAXLINES for card height.
        printables.extend(self.__cardLine(times=self.MAXLINES-lines))
        printables.extend(self.__cardLine(lineSep, start='├', end='┤'))

        # The bottom of the card, containing more information about card's
        # strength and a copyright watermark (could be something else,
        # see the bottomOfCard method for more customization).
        printables.extend(self.__bottomValuesOfCard(attack, defence, watermark))

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
        # Print CARDSIZE times card lines, but without top and bottom art.
        # Thus, minus 2.
        backArt = ':' * self.CARDSIZE
        printables.extend(self.__cardLine(backArt, times=self.CARDSIZE - 2))
        printables.extend(self.__bottomOfCard())

    def __bottomValuesOfCard(self, leftValue, rightValue, bottomValue):
        """
            Returns a list containing only the ASCII art of the bottom of the card.
            By default, this design has separators in the middle, because you
            can choose a left and a right value. Also, you can exactly below that.
            For example,
                                ├─────────┬─────────┤
                                │    999⚔ │   999⛨  │
                                ├─────────┴─────────┤
                                │     Leajian ©     │
        """
        printables = []

        lineSepTop = '├' + '─' * (self.MAXCHARSPERLINE//2 + 1) + '┬' + '─' * (self.MAXCHARSPERLINE//2 + 1) + '┤'
        lineSepMiddle = '{}{} │{}{}' .format(' ' * (self.MAXCHARSPERLINE//2 - 5), leftValue.rjust(4), ' ' * (self.MAXCHARSPERLINE//2 - 5), rightValue.rjust(4))
        lineSepBottom = '├' + '─' * (self.MAXCHARSPERLINE//2 + 1) + '┴' + '─' * (self.MAXCHARSPERLINE//2 + 1) + '┤'

        if self.selected:
            lineSepTop = '╠' + '═' * (self.MAXCHARSPERLINE//2 + 1) + '╦' + '═' * (self.MAXCHARSPERLINE//2 + 1) + '╣'
            lineSepMiddle = '{}{} ║{}{}' .format(' ' * (self.MAXCHARSPERLINE//2 - 5), leftValue.rjust(4), ' ' * (self.MAXCHARSPERLINE//2 - 5), rightValue.rjust(4))
            lineSepBottom = '╠' + '═' * (self.MAXCHARSPERLINE//2 + 1) + '╩' + '═' * (self.MAXCHARSPERLINE//2 + 1) + '╣'

        # Append the top line separator.
        printables.append(lineSepTop)

        # Extend the list with a list containing the line with the middle parts,
        # which are, perhaps, the strength values of the card.
        printables.extend(self.__cardLine(lineSepMiddle))

        # Append the bottom line separator.
        printables.append(lineSepBottom)

        # Extend the list with a list containing the line with the bottom parts,
        # which are, perhaps, a watermark or some more information, i.e. type.
        printables.extend(self.__cardLine(bottomValue))

        return printables

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

        # TODO: Consider the purpose of continious size updates.
        #       Might make sense when animations are introduced.

        # Update the card size per change.
        self.CARDSIZE = len(self.printables)

    def _select(self):
        """
            Causes the card to toggle between highlighted and not.
        """
        if self.selected:
            self.selected = False
        else:
            self.selected = True

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
