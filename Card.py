import textwrap


class Card(object):
    """docstring for Card."""

    def __init__(self, name, description, attack, defence, hp):
        super(Card, self).__init__()
        # Must be odd number.
        self.MAXCHARSPERLINE = 17
        self.MAXLINES = 7

        self.name = name
        if description == '':
            self.description = '█' * self.MAXCHARSPERLINE * self.MAXLINES
        else:
            self.description = description
        self.attack = attack
        self.defence = defence
        self.hp = hp
        self.selected = False
        self.printables = []

    def __cardLine(self, content='', times=1, start='│', end='│'):
        """
            Max MAXCHARSPERLINE characters per line for now.
            It automatically fits more characters in a new line.
        """
        printables = []

        if self.selected and start == '│' and end == '│':
            start = '║'
            end = '║'

        if self.selected and start == '├' and end == '┤':
            start = '╠'
            end = '╣'

        parts = [content]
        length = len(content)

        if length > self.MAXCHARSPERLINE:
            parts = textwrap.wrap(content, width=self.MAXCHARSPERLINE)

        for time in range(times):
            for part in parts:
                printables.append('{} {} {}' .format(start, part.ljust(self.MAXCHARSPERLINE), end))

        return printables

    def __lineSeparator(self):
        lineSep = '├' + '─' * (self.MAXCHARSPERLINE + 2) + '┤'
        if self.selected:
            lineSep = '╠' + '═' * (self.MAXCHARSPERLINE + 2) + '╣'
        return [lineSep]

    def __bottomOfCard(self, content):
        printables = []

        lineSepPartsTop = '├' + '─' * (self.MAXCHARSPERLINE//2 + 1) + '┬' + '─' * (self.MAXCHARSPERLINE//2 + 1) + '┤'
        lineSepPartsBottom = '├' + '─' * (self.MAXCHARSPERLINE//2 + 1) + '┴' + '─' * (self.MAXCHARSPERLINE//2 + 1) + '┤'
        bottomCard = '└' + '─' * (self.MAXCHARSPERLINE + 2) + '┘'

        if self.selected:
            lineSepPartsTop = '╠' + '═' * (self.MAXCHARSPERLINE//2 + 1) + '╦' + '═' * (self.MAXCHARSPERLINE//2 + 1) + '╣'
            lineSepPartsBottom = '╠' + '═' * (self.MAXCHARSPERLINE//2 + 1) + '╩' + '═' * (self.MAXCHARSPERLINE//2 + 1) + '╣'
            bottomCard = '╚' + '═' * (self.MAXCHARSPERLINE + 2) + '╝'

        printables.append(lineSepPartsTop)

        printables.extend(self.__cardLine(content))
        printables.append(lineSepPartsBottom)

        printables.extend(self.__cardLine('    Leajian ©'))
        printables.append(bottomCard)

        return printables

    def __topOfCard(self, hp=''):
        if hp == '':
            top = '┌' + '─' * (self.MAXCHARSPERLINE + 2) + '┐'
        else:
            hpText = str(hp) + '♥'
            top = '┌' + '─' * (self.MAXCHARSPERLINE - 3) + hpText.rjust(4) + ' ┐'

        if self.selected:
            if hp == '':
                top = '╔' + '═' * (self.MAXCHARSPERLINE + 2) + '╗'
            else:
                hpText = str(hp) + '♥'
                top = '╔' + '═' * (self.MAXCHARSPERLINE - 3) + hpText.rjust(4) + ' ╗'

        return [top]

    def _select(self):
        if self.selected:
            self.selected = False
        else:
            self.selected = True

    def _constructACSIIform(self):
        printables = []

        lineSep = '▒' * self.MAXCHARSPERLINE

        attack = str(self.attack) + '⚔'
        defence = str(self.defence) + '⛨'
        bottom = '{}{} │{}{}' .format(' ' * (self.MAXCHARSPERLINE//2 - 5), attack.rjust(4), ' ' * (self.MAXCHARSPERLINE//2 - 5), defence.rjust(4))
        if self.selected:
            bottom = '{}{} ║{}{}' .format(' ' * (self.MAXCHARSPERLINE//2 - 5), attack.rjust(4), ' ' * (self.MAXCHARSPERLINE//2 - 5), defence.rjust(4))

        printables.extend(self.__topOfCard(self.hp))

        printables.extend(self.__cardLine(self.name))
        printables.extend(self.__lineSeparator())
        printables.extend(self.__cardLine(lineSep, start='├', end='┤'))

        # Max 17 * 6 = 102 characters for now.
        temp = self.__cardLine(self.description)
        lines = len(temp)
        printables.extend(temp)

        # Max 6 lines for now.
        printables.extend(self.__cardLine(times=self.MAXLINES-lines))
        printables.extend(self.__cardLine(lineSep, start='├', end='┤'))

        printables.extend(self.__bottomOfCard(bottom))

        self.printables = printables

    def _show(self):
        self._constructACSIIform()
        for line in self.printables:
            print(line)
