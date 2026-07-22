"""Implementaciones base de listas enlazadas: simple, doble y circular.

Uso:
    from base import NodeSingly, SinglyLinkedList
    from base import NodeDoubly, DoublyLinkedList
    from base import NodeCircular, CircularLinkedList
"""
from typing import Any, Optional


class NodeSingly:
    def __init__(self, data: Any, next: Optional["NodeSingly"] = None) -> None:
        self.data = data
        self.next = next

    def __repr__(self) -> str:
        return f"{self.data}"


class SinglyLinkedList:
    def __init__(self) -> None:
        self.head: Optional[NodeSingly] = None
        self.tail: Optional[NodeSingly] = None
        self.size: int = 0

    def append(self, data: Any) -> None:
        new_node = NodeSingly(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            assert self.tail is not None
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def delete_and_return_first(self) -> Any:
        if self.head is None:
            return None
        old_head = self.head
        self.head = self.head.next
        old_head.next = None
        if self.head is None:
            self.tail = None
        self.size -= 1
        return old_head.data

    def delete_and_return_last(self) -> Any:
        if self.size == 0:
            return None
        if self.size == 1:
            old_tail = self.head
            self.head = None
            self.tail = None
            self.size -= 1
            return old_tail.data

        current = self.head
        while current.next != self.tail:
            current = current.next

        old_tail = self.tail
        self.tail = current
        self.tail.next = None
        self.size -= 1
        return old_tail.data

    def __repr__(self) -> str:
        values = []
        current = self.head
        while current:
            values.append(str(current.data))
            current = current.next
        return " → ".join(values) if values else "[]"

    def __len__(self) -> int:
        return self.size


class NodeDoubly:
    def __init__(
        self,
        data: Any,
        prev: Optional["NodeDoubly"] = None,
        next: Optional["NodeDoubly"] = None,
    ) -> None:
        self.data = data
        self.prev = prev
        self.next = next

    def __repr__(self) -> str:
        return f"{self.data}"


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head: Optional[NodeDoubly] = None
        self.tail: Optional[NodeDoubly] = None

    def append(self, data: Any) -> None:
        new_node = NodeDoubly(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            assert self.tail is not None
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def __repr__(self) -> str:
        values = []
        current = self.head
        while current:
            values.append(str(current.data))
            current = current.next
        return " ⇄ ".join(values) if values else "[]"


class NodeCircular:
    def __init__(self, data: Any, next: Optional["NodeCircular"] = None) -> None:
        self.data = data
        self.next = next

    def __repr__(self) -> str:
        return f"{self.data}"


class CircularLinkedList:
    def __init__(self) -> None:
        self.head: Optional[NodeCircular] = None
        self.tail: Optional[NodeCircular] = None

    def append(self, data: Any) -> None:
        new_node = NodeCircular(data)
        if not self.head:
            self.head = self.tail = new_node
            new_node.next = new_node
        else:
            assert self.tail is not None
            new_node.next = self.head
            self.tail.next = new_node
            self.tail = new_node

    def __repr__(self) -> str:
        values = []
        if not self.head:
            return "[]"
        current = self.head
        while True:
            values.append(str(current.data))
            current = current.next
            if current == self.head:
                break
        return " → ".join(values) + " → (head)"
