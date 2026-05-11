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
        new_item = len(self.__heap) - 1
        parent = (new_item - 1) // 2

        while new_item != 0 and self.__heap[new_item] > self.__heap[parent]:

            self.__heap[new_item], self.__heap[parent] = self.__heap[parent], self.__heap[new_item]

            new_item = parent
            parent = (new_item - 1) // 2
