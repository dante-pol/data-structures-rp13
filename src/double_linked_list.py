from __future__ import annotations
from typing import Any, Self


class DoubleLinkedList:

    class Node:

        def __init__(self, data: Any, next: Self = None, prev: Self = None):
            self.__data = data

            self.__next = next
            self.__prev = prev

        def __get_data(self) -> Any:
            return self.__data

        def __set_data(self, new_data: Any) -> None:
            self.__data = new_data

        def __get_next(self) -> Self:
            return self.__next

        def __set_next(self, new_next) -> None:
            self.__next = new_next

        def __get_prev(self) -> Self:
            return self.__prev

        def __set_prev(self, new_prev) -> None:
            self.__prev = new_prev

        data = property(__get_data, __set_data)
        next = property(__get_next, __set_next)
        prev = property(__get_prev, __set_prev)


    def __init__(self):
        self.__count = 0

        self.__head = None
        self.__tail = None


    def add_last(self, data: Any) -> None:
        node = DoubleLinkedList.Node(data=data, next=None)

        if self.is_empty():
            self.__head = node
            self.__tail = node

            self.__count += 1

            return None

        self.__tail.next = node
        node.prev = self.__tail

        self.__tail = node

        self.__count += 1

        return None


    def add_head(self, data: Any) -> None:
        node = DoubleLinkedList.Node(data=data, next=None)

        if self.is_empty():
            self.__head = node
            self.__tail = node

            self.__count += 1

            return None

        self.__head.prev = node
        node.next = self.__head

        self.__head = node

        self.__count += 1

        return None


    def is_empty(self) -> bool:
        return self.__count == 0

