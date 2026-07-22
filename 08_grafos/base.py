"""Implementaciones base de grafos.

Incluye las cuatro combinaciones de representación / peso:
- GraphL:  lista de adyacencia, sin peso
- GraphM:  matriz de adyacencia, sin peso
- GraphWL: lista de adyacencia, con peso
- GraphWM: matriz de adyacencia, con peso

Todas soportan grafos dirigidos y no dirigidos mediante el parámetro
`directed` de `add_edge` (True por defecto).

Uso:
    from base import GraphL, GraphM, GraphWL, GraphWM
"""
from typing import Any, Dict, List, Tuple


class GraphL:
    """Grafo (sin peso) representado con lista de adyacencia."""

    def __init__(self) -> None:
        self.adj_list: Dict[Any, List[Any]] = {}
        self.size: int = 0

    def add_vertex(self, value: Any) -> None:
        if value in self.adj_list:
            return
        self.adj_list[value] = []
        self.size += 1

    def add_edge(self, vertex_1: Any, vertex_2: Any, directed: bool = True) -> None:
        if vertex_1 not in self.adj_list:
            self.add_vertex(vertex_1)
        if vertex_2 not in self.adj_list:
            self.add_vertex(vertex_2)

        if vertex_2 not in self.adj_list[vertex_1]:
            self.adj_list[vertex_1].append(vertex_2)
        if not directed and vertex_1 not in self.adj_list[vertex_2]:
            self.adj_list[vertex_2].append(vertex_1)

    def __repr__(self) -> str:
        return "\n".join(f"{v}: {ns}" for v, ns in self.adj_list.items())


class GraphM:
    """Grafo (sin peso) representado con matriz de adyacencia."""

    def __init__(self) -> None:
        self.adj_matrix: List[List[int]] = []
        self.nodes: List[Any] = []
        self.size: int = 0

    def add_vertex(self, value: Any) -> None:
        if value in self.nodes:
            return
        self.nodes.append(value)
        for row in self.adj_matrix:
            row.append(0)
        self.adj_matrix.append([0] * len(self.nodes))
        self.size += 1

    def add_edge(self, vertex_1: Any, vertex_2: Any, directed: bool = True) -> None:
        if vertex_1 not in self.nodes:
            self.add_vertex(vertex_1)
        if vertex_2 not in self.nodes:
            self.add_vertex(vertex_2)

        pos_v1 = self.nodes.index(vertex_1)
        pos_v2 = self.nodes.index(vertex_2)

        self.adj_matrix[pos_v1][pos_v2] = 1
        if not directed:
            self.adj_matrix[pos_v2][pos_v1] = 1

    def __repr__(self) -> str:
        header = "   " + " ".join(str(n) for n in self.nodes)
        rows = [
            str(self.nodes[i]) + "  " + " ".join(map(str, row))
            for i, row in enumerate(self.adj_matrix)
        ]
        return "\n".join([header, *rows])


class GraphWL:
    """Grafo ponderado representado con lista de adyacencia."""

    def __init__(self) -> None:
        self.adj_list: Dict[Any, List[Tuple[Any, float]]] = {}
        self.size: int = 0

    def add_vertex(self, value: Any) -> None:
        if value in self.adj_list:
            return
        self.adj_list[value] = []
        self.size += 1

    def add_edge(self, vertex_1: Any, vertex_2: Any, weight: float, directed: bool = True) -> None:
        if vertex_1 not in self.adj_list:
            self.add_vertex(vertex_1)
        if vertex_2 not in self.adj_list:
            self.add_vertex(vertex_2)

        self.adj_list[vertex_1].append((vertex_2, weight))
        if not directed:
            self.adj_list[vertex_2].append((vertex_1, weight))

    def __repr__(self) -> str:
        return "\n".join(f"{v}: {ns}" for v, ns in self.adj_list.items())


class GraphWM:
    """Grafo ponderado representado con matriz de adyacencia."""

    def __init__(self, non_representative_value: float = 0) -> None:
        self.adj_matrix: List[List[float]] = []
        self.nodes: List[Any] = []
        self.size: int = 0
        self.non_representative_value = non_representative_value

    def add_vertex(self, value: Any) -> None:
        if value in self.nodes:
            return
        self.nodes.append(value)
        for row in self.adj_matrix:
            row.append(self.non_representative_value)
        self.adj_matrix.append([self.non_representative_value] * len(self.nodes))
        self.size += 1

    def add_edge(self, vertex_1: Any, vertex_2: Any, weight: float, directed: bool = True) -> None:
        if vertex_1 not in self.nodes:
            self.add_vertex(vertex_1)
        if vertex_2 not in self.nodes:
            self.add_vertex(vertex_2)

        pos_v1 = self.nodes.index(vertex_1)
        pos_v2 = self.nodes.index(vertex_2)

        self.adj_matrix[pos_v1][pos_v2] = weight
        if not directed:
            self.adj_matrix[pos_v2][pos_v1] = weight

    def __repr__(self) -> str:
        header = "   " + " ".join(str(n) for n in self.nodes)
        rows = [
            str(self.nodes[i]) + "  " + " ".join(map(str, row))
            for i, row in enumerate(self.adj_matrix)
        ]
        return "\n".join([header, *rows])
