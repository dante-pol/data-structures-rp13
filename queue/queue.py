from __future__ import annotations
from typing import Any, Self

class Queue:

    class Node:
        def __init__(self, data: Any, prev: Self = None):
            self.__data = data
            self.__prev = prev

        def __get_data(self) -> Any:
            return self.__data

        def __get_prev(self) -> Self:
            return self.__prev

        def __set_prev(self, new_prev: Self) -> None:
            self.__prev = new_prev

        data = property(__get_data)
        prev = property(__get_prev, __set_prev)

    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__count = 0

    def enqueue(self, data: Any) -> None:
        node = Queue.Node(data)

        if self.is_empty():
            self.__head = node
            self.__tail = node

            self.__count += 1

            return None

        self.__tail.prev = node
        self.__tail = node

        self.__count += 1

        return None

    # Лучшее O(1)
    # Среднее O(1)
    # Худшее O(1)


    def dequeue(self) -> None:
        if self.is_empty():
            return None

        self.__head = self.__head.prev

        self.__count -= 1

        return None

    # Лучшее O(1)
    # Среднее O(1)
    # Худшее O(1)


    def peek(self) -> Any:
        if self.is_empty():
            return None

        return self.__head.data

    # Лучшее O(1)
    # Среднее O(1)
    # Худшее O(1)


    def is_empty(self) -> bool:
        return self.__count == 0

    # Лучшее O(1)
    # Среднее O(1)
    # Худшее O(1)