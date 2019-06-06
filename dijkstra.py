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

def dijkstra(graph,source):
    nodes = set(graph.nodes)
    edges = graph.edges
    weights = graph.weights

    visited = [source]
    path = {}
    dts = []
    for _ in nodes:
        dts.append(None)

    dts[source] = 0
    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node == None:
                    min_node = node
                elif dts[node] < dts[min_node]:
                    min_node = node
        if min_node is None:
            break
        nodes.remove(min_node)
        current_weight = dts[min_node]

        if min_node not in edges:
            pass
        else:
        
            for edge in edges[min_node]:
                weight = current_weight + weights[(min_node,edge)]
                if edge not in visited:
                    visited.append(edge)
                if dts[edge] is None or weight < dts[edge]:
                    dts[edge] = weight
                    path[edge] = min_node
    return dts,path
