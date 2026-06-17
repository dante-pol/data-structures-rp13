from __future__ import annotations
from typing import Any


class PriorityQueue:

    def __init__(self, ):
        self.__heap = BinaryHeap()

    def enqueue(self, priority: int, data: Any) -> None:
        self.__heap.push(priority, data)

    # Лучшее O(1)
    # Среднее O(log n)
    # Худшее O(log n)


    def dequeue(self) -> Any:
        return self.__heap.pop()

    # Лучшее O(1)
    # Среднее O(log n)
    # Худшее O(log n)


    def peek(self) -> Any:
        return self.__heap.peek()

    # Лучшее O(1)
    # Среднее O(1)
    # Худшее O(1)

    def is_empty(self) -> bool:
        return self.__heap.is_empty()

    # Лучшее O(1)
    # Среднее O(1)
    # Худшее O(1)


class BinaryHeap:

    def __init__(self):
        self.__heap = []

    def push(self, priority: int, data: Any) -> None:
        self.__heap.append([priority, data])
        self.__up()

    def pop(self) -> Any | None:
        if self.is_empty(): return None

        data = self.__heap[0][1]

        self.__heap[0], self.__heap[-1] = self.__heap[-1], self.__heap[0]
        self.__heap.pop(-1)

        self.__down()

        return data

    def peek(self) -> Any:
        if self.is_empty(): return None

        return self.__heap[0][1]

    def is_empty(self) -> bool:
        return len(self.__heap) == 0

    def __up(self) -> None:
        new_item = len(self.__heap) - 1
        parent = (new_item - 1) // 2

        while new_item != 0 and self.__heap[new_item][0] < self.__heap[parent][0]:

            self.__heap[new_item], self.__heap[parent] = self.__heap[parent], self.__heap[new_item]

            new_item = parent
            parent = (new_item - 1) // 2

    def __down(self) -> None:

        down_item = 0

        while down_item < len(self.__heap):
            min_child = 2 * down_item + 1

            if min_child >= len(self.__heap): return None

            if min_child + 1 < len(self.__heap) and self.__heap[min_child][0] > self.__heap[min_child + 1][0]:
                min_child += 1

            if self.__heap[down_item][0] < self.__heap[min_child][0]:
                return None

            self.__heap[down_item], self.__heap[min_child] = self.__heap[min_child], self.__heap[down_item]

            down_item = min_child

        return None
