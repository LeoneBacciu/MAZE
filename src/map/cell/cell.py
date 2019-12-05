class Cell:

    def __init__(self, char, matrix, x, y):
        self.x, self.y = x, y
        self.matrix = matrix
        self.directions = ((0, 1), (-1, 0), (0, -1), (1, 0))
        self.walls = []

        self.black = False
        self.silver = False
        self.looted = False

        self.num_chars = {
            '1000': '╶',
            '0100': '╵',
            '0010': '╴',
            '0001': '╷',
            '1010': '─',
            '0101': '│',
            '1001': '┌',
            '0011': '┐',
            '1100': '└',
            '0110': '┘',
            '1101': '├',
            '0111': '┤',
            '1011': '┬',
            '1110': '┴',
            '1111': '┼'
        }
        self.chars_num = {c: [bool(int(ca)) for ca in n] for n, c in self.num_chars.items()}
        self.known = True
        if char == '?':
            self.known = False
        elif char == '■':
            self.black = True
        else:
            self.walls = self.chars_num[char]

    def learn(self):
        self.known = True

    def canGo(self, directory):
        return self.walls[directory]

    """Is...    """
    def isUnvisited(self):
        return not self.known

    def isWhite(self):
        return not self.black
    """End Is...    """

    """Set...   """
    def setBoundaries(self, boundaries):
        self.learn()
        self.walls = [bool(a) for a in boundaries]

    def setBlack(self):
        self.learn()
        self.black = True
    """End Set...   """

    """Looted"""
    def setLooted(self):
        self.looted = True

    def getLooted(self):
        return self.looted
    """End Looted"""

    def getWalls(self):
        out = []
        for i, w in enumerate(self.walls):
            if w:
                d1 = self.directions[i][0] + self.x
                d2 = self.directions[i][1] + self.y
                if self.matrix[d1][d2].isWhite():
                    out.append((d1, d2))
        return out

    def getUnvisited(self):
        out = []
        ad = [e for i, e in enumerate(self.directions) if self.walls[i]]
        for d in ad:
            if self.matrix[self.x + d[0]][self.y + d[1]].isUnvisited():
                out.append(d)
        print(self.x, self.y, out)
        return out

    def __str__(self):
        if not self.known:
            return '?'
        if self.black:
            return '■'
        else:
            return self.num_chars[''.join([str(int(e)) for e in self.walls])]
