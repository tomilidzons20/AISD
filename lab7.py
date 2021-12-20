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

    def show(self) -> None:
        G = nx.DiGraph()
        edges = []
        for key, value in self.adjacencies.items():
            for neighbour in value:
                edge = [key.data]
                edge.append(neighbour.destination.data)
                edges.append(edge)
        G.add_edges_from(edges)
        # pos = nx.planar_layout(G)
        pos = nx.spring_layout(G)
        nx.draw_networkx_nodes(G, pos)
        nx.draw_networkx_labels(G, pos)
        nx.draw_networkx_edges(G, pos, edge_color='b', arrows=True)
        plt.show()

    def __repr__(self) -> str:
        result = []
        for key, value in self.adjacencies.items():
            res2 = []
            for i in value:
                res2.append(str(i.destination.index) + ": " + str(i.destination.data))
            result.append(str(str(key.index) + ': ' + str(key.data) + ' ----> ' + str(res2)))
        return "\n".join(result)


def gprint(vertex: Vertex):
    print(vertex.data)

graf = Graph()
v0 = graf.create_vertex("v0")
v1 = graf.create_vertex("v1")
v2 = graf.create_vertex("v2")
v3 = graf.create_vertex("v3")
v4 = graf.create_vertex("v4")
v5 = graf.create_vertex("v5")
graf.add(EdgeType.directed, v0, v1)
graf.add(EdgeType.directed, v0, v5)
graf.add(EdgeType.directed, v2, v1)
graf.add(EdgeType.directed, v2, v3)
graf.add(EdgeType.directed, v3, v4)
graf.add(EdgeType.directed, v4, v5)
graf.add(EdgeType.directed, v4, v1)
graf.add(EdgeType.directed, v5, v1)
graf.add(EdgeType.directed, v5, v2)
graf.add(EdgeType.undirected, v5, v1)
print(graf)
graf.show()
# graf.traverse_breadth_first(gprint)
# graf.traverse_depth_first(gprint)
