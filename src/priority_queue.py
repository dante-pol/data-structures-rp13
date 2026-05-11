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
        self.__up()

    def pop(self) -> None:
        self.__heap[0], self.__heap[-1] = self.__heap[-1], self.__heap[0]

        self.__heap.pop(-1)

        self.__down()

    def __up(self) -> None:
        new_item = len(self.__heap) - 1
        parent = (new_item - 1) // 2

        while new_item != 0 and self.__heap[new_item] < self.__heap[parent]:

            self.__heap[new_item], self.__heap[parent] = self.__heap[parent], self.__heap[new_item]

            new_item = parent
            parent = (new_item - 1) // 2

    def __down(self) -> None:

        down_item = 0

        while down_item > len(self.__heap):
            min_child = 2 * down_item + 1

            if min_child + 1 < len(self.__heap) and self.__heap[min_child] > self.__heap[min_child + 1]:
                min_child += 1

            if self.__heap[down_item] < self.__heap[min_child]:
                return None

            self.__heap[down_item], self.__heap[min_child] = self.__heap[min_child], self.__heap[down_item]

            down_item = min_child

        return None
