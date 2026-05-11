from typing import Any


class PriorityQueue:

    def __init__(self):
        pass

    def enqueue(self, data: Any, priority: int) -> None:
        pass

    def dequeue(self) -> Any:
        pass

    def peek(self) -> Any:
        pass

    def is_empty(self) -> bool:
        pass


class BinaryHeap:

    def __init__(self):
        self.__heap = []

    def push(self, priority: int) -> None:
        self.__heap.append(priority)
        self.up()

    def up(self) -> None:
        pass
