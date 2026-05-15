from typing import Any


def malloc(size):
    return [None] * size


def realloc(memory, new_size):
    new_memory = malloc(new_size)

    for i in range(0, len(memory), 1):
        new_memory[i] = memory[i]

    return new_memory


# Линейный способ разрешения коллизий

class HashMap1:

    def __init__(self, size: int = 16):
        self.__keys = malloc(size)
        self.__memory = malloc(size)

        self.__count = 0

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
            realloc(self.__memory, new_size)

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


# Цепочный способ разрешения коллизий


class HashMap2:

    def __init__(self, size: int = 16):
        self.__memory = malloc(size)
        self.__keys = malloc(size)

        self.__count = 0

    def add(self, key : Any, value: Any) -> None:
        index = self.__hash(key)

        if self.__memory[index] is None:
            self.__memory[index] = [ (key, value) ]
            self.__count += 1

            return None

        bucket = self.__memory[index]

        for i in range(len(bucket)):
            if key == bucket[i][0]:
                bucket[i] = (key, value)

                return None

            bucket.append((key, value))
            self.__count += 1

        return None


    def get(self, key: Any) -> Any:
        index = self.__hash(key)

        bucket = self.__memory[index]

        if bucket is None:
            raise ValueError("bucket пустой")

        for i in range(len(bucket)):

            if key == bucket[i][0]:
                return bucket[i][1]

        raise ValueError("Нет искомого ключа")

    def remove(self, key: Any) -> Any:
        pass

    def count(self) -> int:
        return self.__count

    def __hash(self, key: Any) -> int:
        return hash(key) % len(self.__memory)
