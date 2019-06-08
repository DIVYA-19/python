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
            
def floyd_warshall(graph):
    nodes = graph.nodes
    weights = graph.weights
    dt_matrix = [[None] * len(nodes) for _ in range(len(nodes))]
    for i in dt_matrix:
        for j in dt_matrix: #
            if (i,j) in weights.keys():
                matrix[i][j] = weights[(i,j)]
    for i in nodes:
        inter_node = i
        for j in nodes:
            for k in nodes:
                if j == i or k==i:
                    pass
                else: 
                    if (j,i) in weights and (i,k) in weights and weights[(j,i)]!=None and  weights[(i,k)]!=None:
                        weight = weights[(j,i)]+weights[(i,k)]
                        if dt_matrix[i][j] > weight:
                            dt_matrix[i][j] = weight
    return dt_matrix
