from typing import Any, Self


# ----------- Stack (Стэк) -----------

# ------ Fields (Поля) ------
# 1. top - ссылка на вершину стека
# 2. count - кол-во элементов стека

# ------ Interface (Операции) ------
# 1. push(data):None -> добавить элемент на вершину стека
# 2. pop():Any -> удалить элемент с вершины стека
# 3. peek():Any -> посмотреть элемент на вершине стека
# 4. is_empty():bool -> проверка стека на пустоту

class Stack:

    class Node:

        def __init__(self, data, prev: Self = None):
            self.__data = data
            self.__prev = prev

        def __get_data(self) -> Any:
            return self.__data

        def __set_data(self, new_data: Any) -> None:
            self.__data = new_data

        def __get_prev(self) -> Self:
            return self.__prev

        def __set_prev(self, new_prev: Self) -> None:
            self.__prev = new_prev

        data = property(__get_data)
        prev = property(__get_prev, __set_prev)

    def __init__(self):
        self.__top = None
        self.__count = 0

    def push(self, data: Any) -> None:
        node = Stack.Node(data)

        if not self.is_empty():
            node.prev = self.__top

        self.__top = node
        self.__count += 1

    # Лучшее O(1)
    # Среднее O(1)
    # Худшее O(1)

    def pop(self) -> Any:
        if self.is_empty():
            return None

        buff = self.__top.data
        self.__top = self.__top.prev
        self.__count -= 1

        return buff

    # Лучшее O(1)
    # Среднее O(1)
    # Худшее O(1)


    def peek(self) -> Any:
        if self.is_empty():
            return None

        return self.__top.data

    # Лучшее O(1)
    # Среднее O(1)
    # Худшее O(1)


    def is_empty(self) -> bool:
        return self.__count == 0

    # Лучшее O(1)
    # Среднее O(1)
    # Худшее O(1)