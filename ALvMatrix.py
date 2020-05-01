class GraphList:
    def __init__(self):
        self.vertices = {
            "A": {"B": 1},
            "B": {"C": 3, "D": 2},
            "C": {},
            "D": {},
            "E": {"D": 1}
        }

