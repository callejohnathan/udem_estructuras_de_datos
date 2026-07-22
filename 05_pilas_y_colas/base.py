"""Implementaciones base de pilas y colas (ADTs sobre lista de Python).

Uso:
    from base import Stack, Queue, PriorityQueue, EmptyStack, EmptyQueue
"""
from typing import Any, List


class EmptyStack(Exception):
    ...


class EmptyQueue(Exception):
    ...


class Stack:
    """Pila (LIFO): push agrega al tope, pop retorna y elimina el tope."""

    def __init__(self) -> None:
        self.__stack: List[Any] = []

    def push(self, element: Any) -> None:
        self.__stack.append(element)

    def pop(self) -> Any:
        if len(self.__stack) == 0:
            raise EmptyStack("No puedes hacer pop... La pila está vacía")
        return self.__stack.pop()

    def peek(self) -> Any:
        if len(self.__stack) == 0:
            raise EmptyStack("No puedes hacer peek... La pila está vacía")
        return self.__stack[-1]

    def add_from_list(self, data: List[Any]) -> None:
        for item in data:
            self.push(item)

    def __repr__(self) -> str:
        return f"{self.__stack}"

    def __len__(self) -> int:
        return len(self.__stack)


class Queue:
    """Cola (FIFO): enqueue agrega al final, dequeue retorna y elimina el primero."""

    def __init__(self) -> None:
        self.__queue: List[Any] = []

    def enqueue(self, element: Any) -> None:
        self.__queue.append(element)

    def dequeue(self) -> Any:
        if len(self.__queue) == 0:
            raise EmptyQueue("Cola vacía... No podés hacer dequeue")
        return self.__queue.pop(0)

    def peek(self) -> Any:
        if len(self.__queue) == 0:
            raise EmptyQueue("Cola vacía... No podés hacer peek")
        return self.__queue[0]

    def __repr__(self) -> str:
        return str(self.__queue)

    def __len__(self) -> int:
        return len(self.__queue)


class PriorityQueue:
    """Cola de prioridad: mantiene el orden según 'priority' ('min' o 'max')."""

    def __init__(self, priority: str) -> None:
        self.__queue: List[Any] = []
        self.__priority: str = priority

    def enqueue(self, element: Any) -> None:
        if self.__priority == "min":
            self.__queue.append(element)
            self.__queue.sort()
        elif self.__priority == "max":
            self.__queue.append(element)
            self.__queue.sort(reverse=True)
        else:
            raise ValueError("Grave... Este tipo de cola no existe...")

    def dequeue(self) -> Any:
        if len(self.__queue) == 0:
            raise EmptyQueue("Cola vacía... No podés hacer dequeue")
        return self.__queue.pop(0)

    def peek(self) -> Any:
        if len(self.__queue) == 0:
            raise EmptyQueue("Cola vacía... No podés hacer peek")
        return self.__queue[0]

    def __repr__(self) -> str:
        return str(self.__queue)

    def __len__(self) -> int:
        return len(self.__queue)
