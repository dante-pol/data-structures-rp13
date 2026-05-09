from __future__ import annotations
from typing import Any


class Deq:

    __head: Node | None
    __tail: Node | None
    __count: int

    class Node:

        def __init__(self, data, next=None, prev=None):
            self.data = data
            self.next = next
            self.prev = prev


    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__count = 0


    def enqueue(self, data: Any) -> None:
        node = Deq.Node(data=data)

        if self.is_empty():
            self.__head = node
            self.__tail = node

            self.__count += 1

            return None

        self.__tail.prev = node
        node.next = self.__tail

        self.__tail = node

        self.__count += 1

        return None

    def enqueue_head(self, data: Any) -> None:
        node = Deq.Node(data=data)

        if self.is_empty():
            self.__head = node
            self.__tail = node

            self.__count += 1

            return None

        self.__head.next = node
        node.prev = self.__head

        self.__head = node

        self.__count += 1

        return None


    def dequeue(self) -> Any | None:
        if self.is_empty():
            return None

        data = self.__head.data

        if self.__count == 1:
            self.__head = None
            self.__tail = None

            self.__count -= 1

            return data

        self.__head = self.__head.prev
        self.__head.next = None

        self.__count -= 1

        return data

    def dequeue_tail(self) -> Any | None:
        if self.is_empty():
            return None

        data = self.__tail.data

        if self.__count == 1:
            self.__head = None
            self.__tail = None

            self.__count -= 1

            return data

        self.__tail = self.__tail.next
        self.__tail.prev = None

        self.__count -= 1

        return data

    def peek(self) -> Any:
        return self.__head.data

    def peek_tail(self) -> Any:
        return self.__tail.data

    def is_empty(self) -> bool:
        return self.__count == 0