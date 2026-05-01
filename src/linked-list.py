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


        iterator = self.__head

        while iterator.next is not None:
            iterator = iterator.next

        iterator.next = node

        self.__count += 1

    def add_head(self, data: Any) -> None:
        pass

    def insert(self, position: int, data: Any) -> None:

        if self.__count == 0:
            # дома
            pass

        node = Node(data, next=None)

        iterator = self.__head
        iiterator = 1

        while iiterator <= position-1 and iterator.next is not None:
            iiterator += 1
            iterator = iterator.next

        node.next = iterator.next
        iterator.next = node






