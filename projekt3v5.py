from enum import Enum
from typing import Any, Callable, Optional, Dict, List
from testing import Queue
import networkx as nx
import matplotlib.pyplot as plt


class EdgeType(Enum):
    directed = 1
    undirected = 2


class Vertex:
    def __init__(self, data: Any, index: int):
        self.data: Any = data
        self.index: int = index


class Edge:
    def __init__(self, source: Vertex, destination: Vertex, weight: Optional[float] = None):
        self.source: Vertex = source
        self.destination: Vertex = destination
        self.weight: Optional[float] = weight


class Graph:
    def __init__(self):
        self.adjacencies: Dict[Vertex, List[Edge]] = {}

    def create_vertex(self, data: Any) -> Vertex:
        vertex = Vertex(data, len(self.adjacencies))
        self.adjacencies.update({vertex: []})
        return vertex

    def add_directed_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        for key, value in self.adjacencies.items():
            if key == source:
                for neighbour in value:
                    if destination == neighbour.destination:
                        return
                value.append(Edge(source, destination, weight))

    def add_undirected_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        for key, value in self.adjacencies.items():
            if key == source:
                for neighbour in value:
                    if destination == neighbour.destination:
                        return
                value.append(Edge(source, destination, weight))
            if key == destination:
                for neighbour in value:
                    if destination == neighbour.destination:
                        return
                value.append(Edge(destination, source, weight))

    def add(self, edge: EdgeType, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        if edge.name == "directed":
            self.add_directed_edge(source, destination, weight)
        if edge.name == "undirected":
            self.add_undirected_edge(source, destination, weight)

    def traverse_breadth_first(self, visit: Callable[[Any], None]) -> None:
        fifo = Queue()
        visited = []
        first = 0
        for key, value in self.adjacencies.items():
            first = key
            break
        visited.append(first)
        fifo.enqueue(first)
        while fifo:
            v = fifo.dequeue()
            visit(v)
            for neighbour in self.adjacencies[v]:
                if neighbour.destination not in visited:
                    visited.append(neighbour.destination)
                    fifo.enqueue(neighbour.destination)

    def traverse_depth_first(self, visit: Callable[[Any], None]) -> None:
        def dfs(v: Vertex, visited: List[Vertex], visit: Callable[[Any], None]):
            visit(v)
            visited.append(v)
            for neighbour in self.adjacencies[v]:
                if neighbour.destination not in visited:
                    dfs(neighbour.destination, visited, visit)
        visited = []
        first = 0
        for key, value in self.adjacencies.items():
            first = key
            break
        dfs(first, visited, visit)

    def show(self, path: Optional[List[Vertex]] = None) -> None:
        G = nx.DiGraph()
        # set edges
        edges = []
        for key, value in self.adjacencies.items():
            for neighbour in value:
                edge = [key.data]
                edge.append(neighbour.destination.data)
                edge.append(neighbour.weight)
                edges.append(edge)
        G.add_weighted_edges_from(edges)
        # visualization of path
        path1 = []
        if path is not None:
            for n in path:
                path1.append(n.data)
        color_map = []
        colore_map = []
        # set color of nodes(path)
        for node in G:
            if node in path1:
                color_map.append("red")
            else:
                color_map.append("blue")
        # set color of edges(path)
        ed = G.edges()
        for i in ed:
            # if i[0] is path1[-1] and i[1] is path1[0]:
            #     colore_map.append("blue")
            if i[0] in path1 and i[1] in path1:
                x = path1.index(i[0])
                if (x+1 in range(len(path1)) and path1[x+1] is i[1]) or (path1[x-1] is i[1]):
                    colore_map.append("red")
                else:
                    colore_map.append("blue")
            else:
                colore_map.append("blue")
        # visualize graph
        pos = nx.planar_layout(G)
        # pos = nx.spring_layout(G)
        nx.draw_networkx_nodes(G, pos, node_color=color_map)
        nx.draw_networkx_labels(G, pos)
        nx.draw_networkx_edges(G, pos, edge_color=colore_map, arrows=True)
        labels = nx.get_edge_attributes(G, 'weight')
        # decide if graph is weighted
        for key, value in labels.items():
            if value is None:
                break
            else:
                nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.show()

    def __repr__(self) -> str:
        result = []
        for key, value in self.adjacencies.items():
            res2 = []
            for i in value:
                res2.append(str(i.destination.index) + ": " + str(i.destination.data))
            result.append(str(str(key.index) + ': ' + str(key.data) + ' ----> ' + str(res2)))
        return "\n".join(result)


class GraphPath:
    def __init__(self, graph: Graph, ve1: Vertex, ve2: Vertex):
        self.graph = graph
        self.ve1 = ve1
        self.ve2 = ve2
    
    def _find_type(self) -> bool:
        typ = True
        for key, value in self.graph.adjacencies.items():
            for i in value:
                if i.weight is None:
                    typ = False
                    break
        return typ

    def _path_dijkstry(self) -> List:
        def closest_vertex():
            c = float('inf')
            v = None
            for key, value in price.items():
                if value < c and key not in visited:
                    c = value
                    v = key
            return v
        price: Dict[Vertex, float] = {}
        parents: Dict[Vertex, Vertex] = {}
        # initialization of parents and cost dictionary
        for key, value in self.graph.adjacencies.items():
            for i in value:
                price.update({i.destination: float('inf')})
        for key, value in self.graph.adjacencies.items():
            if key == self.ve1:
                price.update({key: 0})
                for i in value:
                    if i.source == self.ve1:
                        price.update({i.destination: i.weight})
                        parents.update({i.destination: i.source})
        price.update({self.ve2: float('inf')})
        parents.update({self.ve2: None})
        # loop
        visited = []
        v = closest_vertex()
        path = {}
        while v:
            c = price[v]
            path.update({v: c})
            for key, value in self.graph.adjacencies.items():
                if key == v:
                    for n in value:
                        nc = c + n.weight
                        if price[n.destination] > nc:
                            price.update({n.destination: nc})
                            parents.update({n.destination: v})
            visited.append(v)
            v = closest_vertex()
        # show costs
        # for k, v in price.items():
        #     print(f"{k.data}: {v}")
        # show parents
        # for k, v in parents.items():
        #     if k is not None and v is not None:
        #         print(f"{k.data}: {v.data}")
        # create path to visualize it on graph
        path1 = [self.ve2]
        curr = path1[0]
        while curr is not self.ve1:
            if parents[curr] is None:
                return []
            path1.append(parents[curr])
            curr = parents[curr]
        return path1

    def _path_across(self) -> List:
        fifo = Queue()
        path = [self.ve1]
        fifo.enqueue(path)
        visited = []
        if self.ve1 is self.ve2:
            return [self.ve1]
        while fifo:
            path = fifo.dequeue()
            v = path[-1]
            for key, value in self.graph.adjacencies.items():
                if key == v:
                    for n in value:
                        np = list(path)
                        if n.destination not in visited:
                            np.append(n.destination)
                            visited.append(n.destination)
                            fifo.enqueue(np)
                            if n.destination == self.ve2:
                                return np

    def find_path(self) -> List:
        typ = self._find_type()
        if typ is False:
            return self._path_across()
        if typ is True:
            return self._path_dijkstry()

    def visualize(self):
        self.graph.show(self.find_path())


def all_weighted_shortest_paths(g: Graph, start: Any) -> Dict[Any, List[Edge]]:
    def closest_vertex():
        c = float('inf')
        v = None
        for key, value in price.items():
            if value < c and key not in visited:
                c = value
                v = key
        return v
    # create variables
    start1 = None
    price: Dict[Vertex, float] = {}
    paths: Dict[Vertex, List[Edge]] = {}
    # initialization of parents and cost dictionary and finding vertex with start data
    for i in g.adjacencies.keys():
        if i.data == start:
            start1 = i
    if start1 is None:
        print("No vertex with given data in graph!")
        return None
    for key, value in g.adjacencies.items():
        paths.update({key.data: []})
        for i in value:
            price.update({i.destination: float('inf')})
    for key, value in g.adjacencies.items():
        if key == start1:
            price.update({key: 0})
            for i in value:
                if i.source == start1:
                    price.update({i.destination: i.weight})
    # add 0 cost edge to starting vertex
    paths[start1.data].append(Edge(start1, start1, 0))
    # loop
    # helping variables
    visited = []
    visited1 = [start1.data]
    v = closest_vertex()
    while v:
        c = price[v]
        for key, value in g.adjacencies.items():
            if key == v:
                for n in value:
                    nc = c + n.weight
                    if price[n.destination] > nc:
                        price.update({n.destination: nc})
                        # if cheaper path found clear path
                        paths[n.destination.data].clear()
                        paths[n.destination.data].append(n)
                    # add edge to path if not visited and not already in path to reduce doubling of edges and same costs
                    elif n.destination.data not in visited1:
                        paths[n.destination.data].append(n)
                    # add next vertex to visited
                    visited1.append(n.destination.data)
        visited.append(v)
        v = closest_vertex()
    # complete paths
    hlp = 0
    while hlp != len(paths):
        hlp = 0
        for k, v in paths.items():
            if v[0].source.data is not start1.data:
                tmp = list(paths[v[0].source.data])
                tmp.extend(v)
                v.clear()
                v.extend(tmp)
            else:
                hlp += 1
    # show paths
    for k, v in paths.items():
        ed = []
        for e in v:
            ed.append([e.source.data, e.destination.data])
        print(f"{k}: {ed}")
    return paths

def gprint(vertex: Vertex):
    print(vertex.data)


# Testy

graf = Graph()

# Graf Testowy
# v0 = graf.create_vertex("v0")
# v1 = graf.create_vertex("v1")
# v2 = graf.create_vertex("v2")
# v3 = graf.create_vertex("v3")
# v4 = graf.create_vertex("v4")
# v5 = graf.create_vertex("v5")
# graf.add(EdgeType.directed, v0, v1)
# graf.add(EdgeType.directed, v0, v5)
# graf.add(EdgeType.directed, v2, v1)
# graf.add(EdgeType.directed, v2, v3)
# graf.add(EdgeType.directed, v3, v4)
# graf.add(EdgeType.directed, v4, v5)
# graf.add(EdgeType.directed, v4, v1)
# graf.add(EdgeType.directed, v5, v1)
# graf.add(EdgeType.directed, v5, v2)

# Graf Wazony Testowy 1
# v0 = graf.create_vertex("v0")
# v1 = graf.create_vertex("v1")
# v2 = graf.create_vertex("v2")
# v3 = graf.create_vertex("v3")
# v4 = graf.create_vertex("v4")
# v5 = graf.create_vertex("v5")
# graf.add(EdgeType.undirected, v0, v1, 1)
# graf.add(EdgeType.undirected, v0, v2, 2)
# graf.add(EdgeType.undirected, v2, v1, 4)
# graf.add(EdgeType.undirected, v2, v4, 3)
# graf.add(EdgeType.undirected, v1, v3, 1)
# graf.add(EdgeType.undirected, v3, v4, 1)
# graf.add(EdgeType.undirected, v3, v5, 2)
# graf.add(EdgeType.undirected, v4, v5, 1)

# all_weighted_shortest_paths(graf, "v0")

# Graf Wazony Testowy 2
# v0 = graf.create_vertex("A")
# v1 = graf.create_vertex("B")
# v2 = graf.create_vertex("C")
# v3 = graf.create_vertex("D")
# v4 = graf.create_vertex("E")
# graf.add(EdgeType.undirected, v0, v1, 2)
# graf.add(EdgeType.undirected, v0, v3, 4)
# graf.add(EdgeType.undirected, v1, v3, 3)
# graf.add(EdgeType.undirected, v1, v2, 3)
# graf.add(EdgeType.undirected, v2, v4, 2)
# graf.add(EdgeType.undirected, v3, v2, 3)
# graf.add(EdgeType.undirected, v3, v4, 4)

# all_weighted_shortest_paths(graf, "A")

# Graf Wazony Testowy 3
# v0 = graf.create_vertex("1")
# v1 = graf.create_vertex("2")
# v2 = graf.create_vertex("3")
# v3 = graf.create_vertex("4")
# v4 = graf.create_vertex("5")
# v5 = graf.create_vertex("6")
# graf.add(EdgeType.undirected, v0, v1, 3)
# graf.add(EdgeType.undirected, v0, v3, 3)
# graf.add(EdgeType.undirected, v1, v2, 2)
# graf.add(EdgeType.undirected, v2, v5, 1)
# graf.add(EdgeType.undirected, v2, v0, 6)
# graf.add(EdgeType.undirected, v3, v4, 1)
# graf.add(EdgeType.undirected, v4, v2, 1)
# graf.add(EdgeType.undirected, v4, v5, 2)
# graf.add(EdgeType.undirected, v5, v3, 3)

# all_weighted_shortest_paths(graf, "1")

# Graf Wazony Testowy 4 (Dziwny)
v0 = graf.create_vertex("1")
v1 = graf.create_vertex("2")
v2 = graf.create_vertex("3")
v3 = graf.create_vertex("4")
v4 = graf.create_vertex("5")
v5 = graf.create_vertex("6")
v6 = graf.create_vertex("7")
v7 = graf.create_vertex("8")
v8 = graf.create_vertex("9")
v9 = graf.create_vertex("10")
v10 = graf.create_vertex("11")
v11 = graf.create_vertex("12")
graf.add(EdgeType.undirected, v0, v1, 1)
graf.add(EdgeType.undirected, v0, v11, 2)
graf.add(EdgeType.undirected, v11, v10, 3)
graf.add(EdgeType.undirected, v10, v9, 2)
graf.add(EdgeType.undirected, v9, v8, 3)
graf.add(EdgeType.undirected, v8, v7, 2)
graf.add(EdgeType.undirected, v7, v6, 3)
graf.add(EdgeType.undirected, v1, v2, 3)
graf.add(EdgeType.undirected, v2, v3, 5)
graf.add(EdgeType.undirected, v3, v4, 1)
graf.add(EdgeType.undirected, v4, v5, 1)
graf.add(EdgeType.undirected, v5, v6, 1)

all_weighted_shortest_paths(graf, "1")

# print(graf)
# graf.traverse_breadth_first(gprint)
# graf.traverse_depth_first(gprint)

pgraph = GraphPath(graf, v6, v0)
# for showing path on graph from vertex ve1 to vertex ve2 in GraphPath()
pgraph.visualize()
# for showing graph
# graf.show()
