from __future__ import annotations
from typing import Any

class Node:

    def __init__(self, data: Any, next: Node =None):
        self.__data = data
        self.__next = next

    def __get_data(self) -> Any:
        return self.__data

    def __set_data(self, new_data: Any) -> None:
        self.__data = new_data

    def __get_next(self) -> Node:
        return self.__next

    def __set_next(self, new_next) -> None:
        self.__next = new_next

    data = property(__get_data, __set_data)
    next = property(__get_next, __set_next)

class LinkedList:


    def __init__(self):
        self.__count = 0
        self.__head = None

    def show(self) -> list[Any]:
        output = []

        iterator = self.__head

        while iterator is not None:
            output.append(iterator.data)

            iterator = iterator.next

        return output

    def add_last(self, data: Any) -> None:
        node = Node(data=data, next=None)

        if self.__count == 0:
            self.__head = node

            self.__count += 1

            return None

        iterator = self.__head

        while iterator.next is not None:
            iterator = iterator.next

        iterator.next = node

        self.__count += 1

        return None

    # Лучшее O(n)
    # Среднее O(n)
    # Худшее O(n)


    def add_head(self, data: Any) -> None:
        node = Node(data)

        node.next = self.__head

        self.__head = node

        self.__count += 1

    # Лучшее O(1)
    # Среднее O(1)
    # Худшее O(1)


    def insert(self, position: int, data: Any) -> None:
        if position > self.__count or position < 0: raise ValueError("list index out of range")

        if position == 0:
            self.add_head(data)

            return None

        node = Node(data, next=None)

        iterator = self.__head
        iiterator = 1

        while iiterator <= position-1 and iterator.next is not None:
            iiterator += 1
            iterator = iterator.next

        node.next = iterator.next
        iterator.next = node

        self.__count += 1

        return None

    # Лучшее O(1)
    # Среднее O(n)
    # Худшее O(n)


    def get(self, position: int) -> Node | None:
        if position > self.__count or position < 0: raise ValueError("list index out of range")

        iterator = self.__head
        iiterator = 1

        while iiterator <= position and iterator.next is not None:

            iterator = iterator.next
            iiterator += 1

        return iterator

    # Лучшее O(n)
    # Среднее O(n)
    # Худшее O(n)


    def remove(self, data: Any) -> Node | None:

        iterator = self.__search_before_target(data)

        if iterator is None: return None

        remove_node = iterator.next

        iterator.next = iterator.next.next

        self.__count -= 1

        return remove_node

    # Лучшее O(1)
    # Среднее O(n)
    # Худшее O(n)


    def find(self, data: Any) -> Node | None:

        iterator = self.__search_before_target(data)

        if iterator is None: return None

        node = iterator.next

        return node

    # Лучшее O(1)
    # Среднее O(n)
    # Худшее O(n)


    def count(self) -> int:
        return self.__count

    # Лучшее O(1)
    # Среднее O(1)
    # Худшее O(1)


    def is_empty(self) -> bool:
        return self.__count == 0

    # Лучшее O(1)
    # Среднее O(1)
    # Худшее O(1)


    def __search_before_target(self, target: Any) -> Node | None:

        iterator = self.__head

        if iterator is None: return None

        while iterator.next.data != target:

            if iterator.next is None: return None

            iterator = iterator.next

        return iterator