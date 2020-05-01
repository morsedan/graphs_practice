class GraphList:
    def __init__(self):
        self.vertices = {
            "A": {"B": 1},
            "B": {"C": 3, "D": 2},
            "C": {},
            "D": {},
            "E": {"D": 1}
        }

class GraphMatrix:
    def __init__(self):
        self.edges = [[0, 1, 0, 0, 0],
                      [0, 0, 3, 2, 0],
                      [0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0],
                      [0, 0, 0, 1, 0]]

class Graph1List:
    def __init__(self):
        self.vertices = {
            "A": {"B": 1},
            "B": {"C": 3, "D": 2, "E": 1},
            "C": {"E": 4},
            "D": {"E": 2},
            "E": {"F": 3},
            "F": {},
            "G": {"D": 1},
        }

class Graph1Matrix:
    def __init__(self):
        self.edges = [[0, 1, 0, 0, 0, 0, 0],
                      [0, 0, 3, 2, 1, 0, 0],
                      [0, 0, 0, 0, 4, 0, 0],
                      [0, 0, 0, 0, 2, 0, 0],
                      [0, 0, 0, 0, 0, 3, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 1, 0, 0, 0]]