import os


class Grid(object):
    """WORK IN PROGRESS"""

    def __init__(self, height, width):
        super(Grid, self).__init__()
        self.height = height
        self.width = width
        os.system("resize -s {} {}".format(self.height, self.width))
        os.system("clear")
        self.tiles = [["+" for x in range(height)] for y in range(width)]

    def printTiles(self):
        for column in self.tiles:
            for row in column:
                print(row)
