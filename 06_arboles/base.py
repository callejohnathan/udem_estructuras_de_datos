"""Implementaciones base de árboles.

- BinaryNode / BinaryTree: árbol binario genérico (no es un BST balanceado,
  solo la estructura de nodos + utilidades para construir árboles de prueba).
- GeneralNode / GeneralTree: árbol general (cada nodo puede tener N hijos).

Uso:
    from base import BinaryNode, BinaryTree, GeneralNode, GeneralTree
"""
from collections import deque
from typing import Any, Optional, List


class BinaryNode:
    def __init__(self, value: Any):
        self.value = value
        self.left: Optional["BinaryNode"] = None
        self.right: Optional["BinaryNode"] = None

    def __repr__(self):
        return f"{self.value}"


class BinaryTree:
    def __init__(self):
        self.root: Optional[BinaryNode] = None

    def insert_by_level(self, values: List[Optional[Any]]) -> None:
        """
        Construye el árbol a partir de una lista por niveles.
        Usa None para representar nodos vacíos.
        Ejemplo:
            tree.insert_by_level([1, 2, 3, None, 5])
            Genera:
                  1
                 / \\
                2   3
                 \\
                  5
        """
        if not values:
            return

        if values[0] is None:
            self.root = None
            return

        self.root = BinaryNode(values[0])
        queue = deque([self.root])
        i = 1

        while queue and i < len(values):
            current = queue.popleft()

            if i < len(values):
                left_val = values[i]
                if left_val is not None:
                    current.left = BinaryNode(left_val)
                    queue.append(current.left)
                i += 1

            if i < len(values):
                right_val = values[i]
                if right_val is not None:
                    current.right = BinaryNode(right_val)
                    queue.append(current.right)
                i += 1

    def insert(self, parent: Any, value: Any) -> None:
        """
        Inserta 'value' como hijo izquierdo o derecho (el primero libre)
        del primer nodo cuyo valor sea 'parent', encontrado por DFS (preorden).
        Si el árbol está vacío y parent es None, 'value' pasa a ser la raíz.
        """
        new_node = BinaryNode(value)

        if self.root is None:
            if parent is None:
                self.root = new_node
            else:
                print(f"⚠️ Árbol vacío y 'parent' distinto de None ('{parent}'). No se insertó '{value}'.")
            return

        def _dfs_insert(node: Optional[BinaryNode]) -> bool:
            if node is None:
                return False

            if node.value == parent:
                if node.left is None:
                    node.left = new_node
                    return True
                if node.right is None:
                    node.right = new_node
                    return True

            if _dfs_insert(node.left):
                return True
            return _dfs_insert(node.right)

        if not _dfs_insert(self.root):
            print(f"⚠️ No se encontró el nodo con valor '{parent}'. No se insertó '{value}'.")

    def print(self, node=None, prefix="", is_left=True, flag=True):
        if flag:
            node = self.root
        if not node:
            print("Empty Tree")
            return
        if node.right:
            self.print(node.right, prefix + ("│   " if is_left else "    "), False, False)
        print(prefix + ("└── " if is_left else "┌── ") + str(node.value))
        if node.left:
            self.print(node.left, prefix + ("    " if is_left else "│   "), True, False)


class GeneralNode:
    def __init__(self, value: Any):
        self.value = value
        self.children: List["GeneralNode"] = []

    def __repr__(self):
        return f"{self.value}"


class GeneralTree:
    def __init__(self):
        self.root: Optional[GeneralNode] = None

    def insert(self, parent: Optional[Any], value: Any) -> None:
        """
        Inserta un nuevo nodo con 'value' como hijo del nodo cuyo valor es 'parent'.
        Si el árbol está vacío y parent es None, el nuevo nodo se convierte en la raíz.
        """
        new_node = GeneralNode(value)

        if self.root is None:
            if parent is None:
                self.root = new_node
            else:
                print(f"⚠️ Árbol vacío. No existe el padre '{parent}'.")
            return

        parent_node = self._find(self.root, parent)
        if parent_node:
            parent_node.children.append(new_node)
        else:
            print(f"⚠️ No se encontró el nodo padre con valor '{parent}'.")

    def _find(self, node: GeneralNode, value: Any) -> Optional[GeneralNode]:
        """Búsqueda DFS del nodo con un valor dado."""
        if node.value == value:
            return node
        for child in node.children:
            found = self._find(child, value)
            if found:
                return found
        return None

    def __repr__(self) -> str:
        if not self.root:
            return "🌱 Árbol vacío"
        return self._build_tree_repr(self.root, "", True)

    def _build_tree_repr(self, node: GeneralNode, prefix: str, is_last: bool) -> str:
        tree_str = prefix + ("└── " if is_last else "├── ") + str(node.value) + "\n"
        prefix += "    " if is_last else "│   "

        child_count = len(node.children)
        for i, child in enumerate(node.children):
            is_last_child = (i == child_count - 1)
            tree_str += self._build_tree_repr(child, prefix, is_last_child)
        return tree_str


if __name__ == "__main__":
    tree = BinaryTree()
    tree.insert_by_level([1, 2, 3, None, 5, 6, None, 7])
    tree.insert(7, 10)
    tree.print()

    gtree = GeneralTree()
    gtree.insert(None, "A")
    gtree.insert("A", "B")
    gtree.insert("A", "C")
    gtree.insert("B", "D")
    print(gtree)
