class graph:
    def __init__(self):
        self.nodes = []
        self.edges = {}
        self.weights = {}

    def add_node(self,node):
        self.nodes.append(node)

    def add_edge(self,from_node,to_node,weight):
        self.weights[(from_node,to_node)] = weight
        if from_node not in self.edges:
            self.edges[from_node] = [to_node]
        else:
            self.edges[from_node].append(to_node)


def hamiltonian(graph,pt,path=[]):
    if pt not in path:
        path.append(pt)
        if len(path) == len(graph.nodes):
            return path
        for node in graph.edges.get(pt, []):
            Ham = hamiltonian(graph,node,path)
            if Ham is not None:
                return Ham
                
