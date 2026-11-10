from typing import NamedTuple
from collections import deque


type WeightedGraph = dict[str, set[tuple[str, int]]]


class Edge(NamedTuple):

    weight: int
    u: str
    v: str

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Edge):
            return False
        return (self.weight == other.weight
                and ((self.u == other.u and self.v == other.v)
                     or (self.u == other.v and self.v == other.u)))

    def __hash__(self):
        return hash(self.weight) + hash(self.u) + hash(self.v)


def sort_edges(graph: WeightedGraph) -> deque[Edge]:
    result: set[Edge] = set()
    for u, neighbours in graph.items():
        for v, weight in neighbours:
            result.add(Edge(weight, u, v))
    return deque(sorted(list(result)))


if __name__ == '__main__':
    g1: WeightedGraph = {
        'A': {('B', 2), ('C', 6), ('D', 5)},
        'B': {('A', 2), ('C', 8), ('D', 11)},
        'C': {('A', 6), ('B', 8), ('D', 1)},
        'D': {('A', 5), ('B', 11), ('C', 1)}
    }
    g2: WeightedGraph = {
        'A': {('B', 1), ('D', 12), ('F', 10)},
        'B': {('A', 1), ('C', 15), ('D', 13), ('E', 9)},
        'C': {('B', 15), ('E', 3), ('G', 2)},
        'D': {('A', 12), ('B', 13), ('F', 14), ('G', 2)},
        'E': {('B', 9), ('C', 3), ('F', 10), ('G', 1)},
        'F': {('A', 10), ('D', 14), ('E', 10), ('G', 11), ('H', 4)},
        'G': {('C', 2), ('D', 2), ('E', 1), ('F', 11), ('H', 5)},
        'H': {('F', 4), ('G', 5)}
    }
    # e1: Edge = Edge(10, 'A', 'B')
    # e2: Edge = Edge(10, 'B', 'A')
    # print(e1)
    # print(e2)
    # print(e1 == e2)
    # print(e1 == 5)
    # s: set[Edge] = set()
    # print(s)
    # s.add(e1)
    # s.add(e2)
    # print(s)
    # print(hash(e1))
    # print(hash(e2))
    from pprint import pprint
    pprint(sort_edges(g1))
    pprint(sort_edges(g2))
