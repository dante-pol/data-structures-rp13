from typing import Any

from Cryptodome.SelfTest.Cipher.test_DES3 import index


# Линейный способ разрешения коллизий

class HashMap1:

    def __init__(self, size: int = 16):
        self.__keys = [None] * size
        self.__memory = [None] * size

        self.__count = 0

    @staticmethod
    def __malloc(type, number):
        return [None] * number

    @staticmethod
    def __realloc(memory, new_size):
        new_memory = HashMap1.__malloc(int, new_size)

        for i in range(0, len(memory), 1):
            new_memory[i] = memory[i]

        return new_memory

    def add(self, key: Any, value: Any) -> None:
        index = self.__hash(key)

        if self.__memory is None:

            self.__memory[index] = value
            self.__keys[index] = key

            self.__count += 1

        elif self.__keys[index] == key:

            self.__memory[index] = value

        else:
            for i in range(len(self.__memory)):
                if self.__memory[i] is None:
                    self.__memory[i] = value
                    self.__keys[i] = key

                    return None

            raise RuntimeError("Нет свободного места")

        fill_factor = self.__count / len(self.__memory)

        if fill_factor >= 0.7:

            new_size = len(self.__memory) * 2
            HashMap1.__realloc(self.__memory, new_size)

        return None

    def get(self, key: Any) -> Any:
        index = self.__hash(key)

        if self.__keys[index] == key:
            return self.__memory[index]

        for i in range(len(self.__memory)):

            if self.__keys[i] == key:
                return self.__memory[i]

        raise ValueError("Не существует элемента с таким ключём")

    def remove(self, key: Any) -> Any:
        index = self.__hash(key)

        if self.__keys[index] == key:

            buff = self.__memory[index]

            self.__memory[index] = None
            self.__keys[index] = None

            return buff

        for i in range(len(self.__memory)):
            if self.__keys[i] == key:
                buff = self.__memory[i]

                self.__memory[i] = None
                self.__keys[i] = None

                return buff

        raise ValueError("Нет элемента с искомым ключем")

    def count(self) -> int:
        return self.__count

    def __hash(self, key: Any) -> int:
        return hash(key) % len(self.__memory)
