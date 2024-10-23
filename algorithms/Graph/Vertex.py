class Vertex:
    def __init__(self, id):
        self.id = id
        self.edges = []
        self.visited = False
        self.discovered = False
        self.distance = float('inf')
        self.predecessor = None
    
    def add_edge(self, edge):
        self.edges.append(edge)

    def __str__(self):
        return f"Vertex {self.id}"
        
        