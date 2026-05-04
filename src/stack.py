from typing import Any

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

        def __init__(self, data, prev=None):
            self.data = data
            self.prev = prev

    def __init__(self):
        self.__top = None
        self.__count = 0

    def push(self, data: Any) -> None:
        node = Stack.Node(data)

        if not self.is_empty():
            node.prev = self.__top

        self.__top = node
        self.__count += 1

    def pop(self) -> Any:
        if self.is_empty():
            return None

        buff = self.__top.data
        self.__top = self.__top.prev
        self.__count -= 1

        return buff

    def peek(self) -> Any:
        if self.is_empty():
            return None

        return self.__top.data

    def is_empty(self) -> bool:
        return self.__count == 0
#
# s1 = Stack()
# s1.push("Kara")
# s1.push("3xKara")
# s1.push("30xKara")
# s1.push("300xKara")
# s1.push("3000xKara")
#
# print(s1.peek())
# print(s1.pop())
# print(s1.peek())
# print(s1.pop())
# print(s1.pop())
# print(s1.pop())
# print(s1.pop())
# print(s1.pop())
# print(s1.pop())
# print(s1.pop())
