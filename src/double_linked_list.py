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


    def delete_first(self) -> None:

        if self.is_empty(): return None

        self.__head = self.__head.next

        if self.__count == 1:

            self.__tail = None
            self.__count -= 1

            return None

        self.__head.prev = None
        self.__count -= 1

        return None


    def delete_last(self) -> None:

        if self.is_empty(): return None

        self.__tail = self.__tail.prev

        if self.__count == 1:

            self.__head = None
            self.__count -= 1

            return None

        self.__tail.next = None
        self.__count -= 1

        return None


    def insert(self, position: int, data: Any) -> None:

        if position > self.__count or position < 0: raise ValueError("list index out of range")

        if position == 0:
            self.add_head(data)

            return None

        node = DoubleLinkedList.Node(data, next=None)

        iterator = self.get(position)

        node.prev = iterator.prev
        node.next = iterator

        iterator.prev = node

        node.prev.next = node

        return None


    def get(self, position: int) -> Node:

        if position > self.__count or position < 0: raise ValueError("list index out of range")

        if position > self.__count // 2:
            iterator = self.__tail
            move = iterator.prev

        else:
            iterator = self.__head
            move = iterator.next

        iiterator = 0

        while iiterator == position:
            iterator = move
            iiterator += 1

        return iterator


    def remove(self, data: Any) -> Node | None:

        iterator = self.__search_before_target(data)

        if iterator is None: return None

        iterator.prev.next = iterator.next
        iterator.next.prev = iterator.prev

        return None


    def __search_before_target(self, target: Any) -> Node | None:

        iterator = self.__head

        if iterator is None: return None

        while iterator.data != target:

            if iterator.next is None: return None

            iterator = iterator.next

        return iterator




    def is_empty(self) -> bool:
        return self.__count == 0




