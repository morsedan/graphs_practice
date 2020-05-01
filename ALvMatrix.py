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

