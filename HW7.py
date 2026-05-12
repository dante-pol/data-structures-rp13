from __future__ import annotations


class PersonList:
    class PersonCard:

        def __init__(self, name: str, age: int, occupation: str, next: PersonList.PersonCard = None):
            self.name = name
            self.age = age
            self.occupation = occupation

            self.next = next

    def __init__(self):
        self.__count = 0
        self.__head = None

    def add_person(self, card: PersonCard) -> None:
        if self.is_empty():

            self.__head = card
            self.__count += 1

            return None

        card.next = self.__head
        self.__head = card

        self.__count += 1

        return None

    def append_person(self, card: PersonCard) -> None:
        if self.is_empty():

            self.__head = card
            self.__count += 1

            return None

        iterator = self.__head

        while not iterator.next is None:
            iterator = iterator.next

        iterator.next = card

        self.__count += 1

        return None

    def insert_person_at(self, position: int, card: PersonCard) -> None:
        if position > self.__count or position < 0:  raise ValueError()

        iterator = self.__head
        iiterator = 0

        while iiterator < position - 1:

            iterator = iterator.next
            iiterator += 1

        card.next = iterator.next
        iterator.next = card

        self.__count += 1

        return None

    def remove_first_person(self) -> PersonCard | None:
        pass

    def remove_last_person(self) -> PersonCard | None:
        pass

    def remove_person(self, card: PersonCard) -> PersonCard | None:
        pass

    def clear_all(self) -> None:
        pass

    def total_people(self) -> int:
        pass

    def is_empty(self) -> bool:
        return self.__count == 0
