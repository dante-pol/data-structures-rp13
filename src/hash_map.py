from typing import Any


# Линейный способ разрешения коллизий

class HashMap1:

    def __init__(self, size: int = 16):
        self.__keys = [None] * size
        self.__memory = [None] * size

        self.__count = 0

    def add(self, key: Any, value: Any) -> None:
        pass

    def get(self, key: Any) -> Any:
        pass

    def remove(self, key: Any) -> Any:
        pass

    def count(self) -> int:
        pass

    def __hash(self, key: Any) -> int:
        return hash(key) % len(self.__memory)
