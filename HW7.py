from __future__ import annotations

from datetime import datetime


# task 1

class PersonList:
    class PersonCard:

        def __init__(self, name: str, age: int, occupation: str, next: PersonList.PersonCard = None):
            self.name = name
            self.age = age
            self.occupation = occupation

            self.next = next

        def __eq__(self, another: PersonList.PersonCard):
            return self.name == another.name and self.age == another.age and self.occupation == self.occupation

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
        if self.is_empty():
            return None

        self.__head = self.__head.next

        self.__count -= 1

        return None

    def remove_last_person(self) -> PersonCard | None:
        if self.is_empty():
            return None

        iterator = self.__head

        while not iterator.next.next is None:
            iterator = iterator.next

        iterator.next = None

        self.__count -= 1

        return None

    def remove_person(self, card: PersonCard) -> PersonCard | None:

        iterator = self.__head

        while not iterator.next == card:

            if iterator.next is None:
                return None

            iterator = iterator.next

        iterator.next = iterator.next.next

        self.__count -= 1

        return None


    def clear_all(self) -> None:
        self.__head = None

    def total_people(self) -> int:
        return self.__count

    def is_empty(self) -> bool:
        return self.__count == 0


# task2


class TaskStack:

    class ProjectTask:

        description: str
        due_date: datetime

        def __init__(self, description: str, due_date: datetime):
            self.description = description
            self.due_date = due_date

            self.prev = None

    def __init__(self):

        self.__top = None
        self.__count = 0

    def push(self, task: ProjectTask) -> None:
        if not self.is_empty():
            task.prev = self.__top

        self.__top = task

        self.__count += 1

    def pop(self) -> ProjectTask | None:

        if self.is_empty():
            return None

        buff = self.__top
        self.__top = self.__top.prev

        return buff

    def peek(self) -> ProjectTask | None:
        return self.__top

    def is_empty(self) -> bool:
        return self.__count == 0

    def count(self) -> int:
        return self.__count


# task 3


class PrintQueue:

    class PrintDocument:

        tittle: str
        number_pages: int

        def __init__(self, tittle: str, number_pages: int):
            self.tittle = tittle
            self.number_pages = number_pages

            self.prev = None

    def __init__(self):
        self.__head = None
        self.__tail = None

        self.__count = 0

    def enqueue(self, document: PrintDocument) -> None:
        if self.is_empty():
            self.__head = document
            self.__tail = document

            self.__count += 1

            return None

        self.__tail.prev = document
        self.__tail = document

        self.__count += 1

        return None

    def dequeue(self) -> PrintDocument | None:
        if self.is_empty(): return None

        self.__head = self.__head.prev

        self.__count -= 1

        return None

    def peek(self) -> PrintDocument | None:
        return self.__head

    def is_empty(self) -> bool:
        return self.__count == 0

    def count(self) -> int:
        pass

