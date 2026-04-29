from typing import Any

# List - динамический массив
# Поля
# 1. Size
# 2. Count
# 3. Memory

# Интерфейс
# -add(item) - добавить элемент в конец списка
# -add_head(item) - добавить элемент в начало списка
# -insert(index, item) - вставить элемент по индексу
# -remove(item) - удалить первое вхождение элемента
# -pop(index) - удалить элемент по индексу
# -count(item) - кол-во вхождений элемента
# -find(item) - найти первое вхождение элемента. если такого элемента нет, вернуть -1
# -is_empty() - вернуть кол-во элементов

# reverse() - развернуть массив
# -sort(key, order_by) - отсортировать текущий массив

class List:

    @staticmethod
    def __malloc(type, number):
        return [None]*number

    @staticmethod
    def __realloc(memory, type, old_size, new_size):
        new_memory = List.__malloc(int, new_size)

        for i in range(0, old_size, 1):
            new_memory[i] = memory[i]

        return new_memory

    def __init__(self):
        self.__count = 0
        self.__size = 4
        self.__memory = List.__malloc(int, self.__size)

    def __str__(self):
        return str(self.__memory)


    def add(self, data: Any) -> None:
        if self.__count == self.__size:
            new_size = self.__size + (self.__size // 2)

            self.__memory = List.__realloc(self.__memory, int, self.__size, new_size)
            self.__size = new_size

        self.__memory[self.__count] = data
        self.__count += 1

    def remove(self, data: Any) -> None:

        if self.__count == 0: return
        if self.__count == 1 and self.__memory[0] == data:  self.__memory[0] = None

        target_index = -1
        for i in range(0, self.__count, 1):
            if self.__memory[i] == data:
                target_index = i
                break

        if target_index == -1:  return

        for i in range(target_index, self.__count - 1, 1):
            self.__memory[i] = self.__memory[i + 1]

        self.__count -= 1
        self.__memory[self.__count] = None

    def sort(self,  order_by= lambda x, y: x < y, key= lambda obj: obj):

        for i in range(0, self.__count - 1, 1):
            for j in range(0, self.__count - i - 1, 1):
                if not order_by(key(self.__memory[j]), key(self.__memory[j + 1])):
                    self.__memory[j], self.__memory[j + 1] = self.__memory[j + 1], self.__memory[j]

    def is_empty(self) -> bool:
        return self.__count == 0

    def add_head(self, data: Any) -> None:
        if self.__count == self.__size:
            new_size = self.__size + (self.__size // 2)

            self.__memory = List.__realloc(self.__memory, int, self.__size, new_size)
            self.__size = new_size

        for i in range(self.__count, -1, -1):
            self.__memory[i], self.__memory[i + 1] = self.__memory[i + 1], self.__memory[i]

        self.__memory[0] = data

    def insert(self, data: Any, insert_index: int) -> None:
        if self.__count == self.__size:
            new_size = self.__size + (self.__size // 2)

            self.__memory = List.__realloc(self.__memory, int, self.__size, new_size)
            self.__size = new_size

        for i in range(self.__count, insert_index - 1, -1):
            self.__memory[i], self.__memory[i + 1] = self.__memory[i + 1], self.__memory[i]

        self.__memory[insert_index] = data

    def pop(self, pop_index: int) -> None:
        self.__memory[pop_index] = None

        for i in range(pop_index, self.__count - 1, 1):
            self.__memory[i], self.__memory[i + 1] = self.__memory[i + 1], self.__memory[i]

    def count(self, item: Any) -> int:
        count = 0

        for i in range(self.__count):

            if self.__memory[i] == item:
                count += 1

        return count

    def find(self, item: Any) -> int:
        for i in range(self.__count):

            if self.__memory[i] == item:
                return i

        return -1

    def reverse(self) -> None:
        for i in range(self.__count // 2):
            self.__memory[i], self.__memory[self.__count - 1 - i] = self.__memory[self.__count - 1 - i], self.__memory[i]