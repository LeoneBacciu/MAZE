import time
import numpy as np

from collections import deque
from cell.cell import Cell


class EndMazeError(Exception):
    """You explored all the MAZE"""
    pass


class Matrix:

    def __init__(self, dims: tuple):
        self.dims = dims
        self.data = np.ndarray(shape=dims, dtype=object)
        for xi in range(dims[0]):
            for yi in range(dims[1]):
                self.data[xi][yi] = Cell('?', self, xi, yi)

    def __getitem__(self, item):
        return self.data[item]

    def __setitem__(self, key, value):
        if type(value) == Cell:
            self.data[key] = value

    def BFS(self, xs, ys):
        places = np.full(self.dims, False)
        places[xs][ys] = True
        q = deque()
        q.append(([xs], [ys], [(xs, ys)]))
        while len(q) > 0:
            xt, yt, d = q.popleft()
            xc, yc = xt[0], yt[0]
            unvisited = self.data[xc][yc].getUnvisited()
            if len(unvisited) > 0:
                d.append((xc + unvisited[0][0], yc + unvisited[0][1]))
                return d
            for walls in self.data[xc][yc].getWalls():
                d1, d2 = walls[0], walls[1]
                if not places[d1][d2]:
                    places[d1][d2] = True
                    nd = d.copy()
                    nd.append((d1, d2))
                    q.append(([walls[0]], [walls[1]], nd.copy()))
        raise EndMazeError("You explored all the MAZE!")

    @staticmethod
    def absToRel(coord: list):
        out = []
        for i in range(1, len(coord)):
            out.append((coord[i][0]-coord[i-1][0], coord[i][1]-coord[i-1][1]))
        return out

    def load(self, name: str):
        with open(name, 'r+') as rf:
            for rr in range(len(self.data)):
                for cr in range(len(self.data[rr]) + 1):
                    c = rf.read(1)
                    if not c == '\n':
                        self.data[rr][cr].__init__(c, self, rr, cr)

    def save(self, name: str):
        with open(name, 'w+') as wf:
            for rw in self.data:
                for cw in rw:
                    wf.write(str(cw))
                wf.write('\n')


matrix = Matrix((10, 10))
matrix.load('map1.txt')
x, y = 6, 4
ts = time.time()
route = None
try:
    route = matrix.BFS(x, y)
except EndMazeError:
    print('fine')
print(route)
print(matrix.absToRel(route))
print(time.time()-ts)
matrix.save('map2.txt')
