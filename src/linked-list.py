from __future__ import annotations
from typing import Any


# ---------------- LinkedList (Односвязный список) -----------------

# ------- Field (Поля) -------
# 1. count - кол-во элементов списка
# 2. head -

# ------- Interface (Интерфейс) -------
# 1. add_last(data): None  - добавляет элемент data в конец списка
# 2. add_head(data): None  - добавляет элемент data в начало списка
# 3. insert(position, data): None  - вставляет элемент data на позицию position
# 4. get(position): Node | None  - возвращает узел (Node) по позиции. если такой позиции нет, вернуть None
# 5. remove(data): Node  - удаляет первое вхождение элемента data и возвращает его узел
# 6. find(data): Node | None
# 7. count(data): int
# 8. is_empty(): bool

class Node:

    def __init__(self, data: Any, next: Node =None):
        self.data = data
        self.next = next


class LinkedList:


    def __init__(self):
        self.__count = 0
        self.__head = None

    def add_last(self, data: Any) -> None:
        node = Node(data=data, next=None)

        if self.__count == 0:
            self.__head = node

            return None

        iterator = self.__head

        while iterator.next is not None:
            iterator = iterator.next

        iterator.next = node

        self.__count += 1

        return None

    def add_head(self, data: Any) -> None:
        node = Node(data)

        node.next = self.__head

        self.__head = node

    def insert(self, position: int, data: Any) -> None:
        if position > self.__count or position < 0: raise ValueError("list index out of range")

        if position == 1:
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

        return None

    def get(self, position: int) -> Node | None:
        if position > self.__count or position < 0: raise ValueError("list index out of range")

        iterator = self.__head
        iiterator = 1

        while iiterator <= position and iterator.next is not None:

            iterator = iterator.next
            iiterator += 1

        return iterator

    def remove(self, data: Any) -> Node | None:

        iterator = self.__head

        while iterator.next.data != data:

            if iterator.next is None: return None

            iterator = iterator.next

        node = iterator.next

        iterator.next = iterator.next.next

        return node


    def find(self, data: Any) -> Node | None:

        iterator = self.__head

        while iterator.next.data != data:

            if iterator.next is None: return None

            iterator = iterator.next

        node = iterator.next

        return node









