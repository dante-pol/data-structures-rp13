from __future__ import annotations
from typing import Any, Self


class DoubleLinkedList:

    class Node:

        def __init__(self, data: Any, next: Self = None, prev: Self = None):
            self.data = data

            self.next = next
            self.prev = prev


    def __init__(self):
        self.__count = 0

        self.__head = None
        self.__tail = None


    def show(self) -> list[Any]:
        output = []

        iterator = self.__head

        while iterator is not None:
            output.append(iterator.data)

            iterator = iterator.next

        return output


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

    # Лучшее O(1)
    # Среднее O(1)
    # Худшее O(1)


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

    # Лучшее O(1)
    # Среднее O(1)
    # Худшее O(1)


    def delete_first(self) -> Node | None:

        if self.is_empty(): return None

        buff = self.__head

        self.__head = self.__head.next

        if self.__count == 1:

            self.__tail = None
            self.__count -= 1

            return buff

        self.__head.prev = None
        self.__count -= 1

        return buff

    # Лучшее O(1)
    # Среднее O(n)
    # Худшее O(n)


    def delete_last(self) -> Node | None:

        if self.is_empty(): return None

        buff = self.__tail

        self.__tail = self.__tail.prev

        if self.__count == 1:

            self.__head = None
            self.__count -= 1

            return buff

        self.__tail.next = None
        self.__count -= 1

        return buff

    # Лучшее O(1)
    # Среднее O(1)
    # Худшее O(1)


    def insert(self, position: int, data: Any) -> None:

        if position > self.__count or position < 0: raise ValueError("list index out of range")

        if position == 0:
            self.add_head(data)

            return None

        if position == self.__count:
            self.add_last(data)

            return None

        node = DoubleLinkedList.Node(data, next=None)

        iterator = self.get(position)

        node.prev = iterator.prev
        node.next = iterator

        iterator.prev.next = node
        iterator.prev = node

        self.__count += 1

        return None

    # Лучшее O(1)
    # Среднее O(n)
    # Худшее O(n)


    def get(self, position: int) -> Node:

        if position > self.__count or position < 0: raise ValueError("list index out of range")

        if position > self.__count // 2:

            iterator = self.__tail
            iiterator = self.__count

            while iiterator != position:
                iterator = iterator.prev
                iiterator -= 1

        else:

            iterator = self.__head
            iiterator = 0

            while iiterator != position:
                iterator = iterator.next
                iiterator += 1

        return iterator

    # Лучшее O(1)
    # Среднее O(n)
    # Худшее O(n)


    def remove(self, data: Any) -> Node | None:

        iterator = self.find(data)

        if iterator is None: return None

        if iterator.prev is None:
            node = self.delete_first()
            return node

        if iterator.next is None:
            node = self.delete_last()
            return node

        iterator.prev.next = iterator.next
        iterator.next.prev = iterator.prev

        self.__count -= 1

        return iterator

    # Лучшее O(1)
    # Среднее O(n)
    # Худшее O(n)


    def find(self, target: Any) -> Node | None:

        iterator = self.__head

        if iterator is None: return None

        while iterator.data != target:

            if iterator.next is None: return None

            iterator = iterator.next

        return iterator

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