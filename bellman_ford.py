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
            
def bellman(graph,src):
    nodes = graph.nodes
    weights = graph.weights
    dt = [None]*len(nodes)
    dt[src] = 0

    for i in range(len(nodes)):
        for edge in weights:
            if dt[edge[0]] != None and (dt[edge[1]]==None or dt[edge[0]] + weights[edge] < dt[edge[1]]):
                dt[edge[1]] = dt[edge[0]] + weights[edge]

    return dt
