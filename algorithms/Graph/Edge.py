class Edge:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w

    def __str__(self):
        return f"Edge({self.u} -> {self.v}, weight: {self.w})"
