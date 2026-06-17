

import pytest

from deque.deque import Deque


@pytest.fixture()
def full_deq():
    deque = Deque()

    deque.enqueue(1)
    deque.enqueue(2)
    deque.enqueue(3)
    deque.enqueue(4)

    return deque


@pytest.fixture()
def one_item():
    deque = Deque()

    deque.enqueue(1)

    return deque

def test_enqueue_positive(full_deq):
    deque = full_deq
    assert deque.peek_tail() == 4

    deque.enqueue(10)

    assert deque.peek_tail() == 10


def test_enqueue_boundary_empty():
    deque = Deque()

    deque.enqueue(2)

    assert deque.peek() == 2


def test_enqueue_boundary_one_item(one_item):
    deque = one_item

    deque.enqueue(2)

    assert deque.peek_tail() == 2


def test_enqueue_head_positive(full_deq):
    deque = full_deq

    assert deque.peek() == 1

    deque.enqueue_head(10)

    assert deque.peek() == 10


def test_enqueue_head_boundary_empty():
    deque = Deque()

    deque.enqueue_head(10)

    assert deque.peek() == 10


def test_enqueue_head_boundary_one_item(one_item):
    deque = one_item

    deque.enqueue_head(10)

    assert deque.peek() == 10


def test_dequeue_positive(full_deq):
    deque = full_deq

    assert deque.dequeue() == 1
    assert deque.dequeue() == 2
    assert deque.peek() == 3


def test_dequeue_boundary_empty():
    deque = Deque()

    assert deque.dequeue() is None

def test_dequeue_boundary_one_item(one_item):
    deque = one_item

    deque.dequeue()

    assert deque.peek() is None


def test_dequeue_tail_positive(full_deq):
    deque = full_deq

    assert deque.dequeue_tail() == 4
    assert deque.dequeue_tail() == 3
    assert deque.peek_tail() == 2

def test_dequeue_tail_boundary_empty():
    deque = Deque()

    assert deque.dequeue_tail() is None


def test_dequeue_tail_boundary_one_item(one_item):
    deque = one_item

    deque.dequeue_tail()

    assert deque.peek() is None


def test_peek_positive(full_deq):
    deque = full_deq

    assert deque.peek() == 1


def test_peek_boundary_empty():
    deque = Deque()

    assert deque.peek() is None


def test_peek_boundary_one_item(one_item):
    deque = one_item

    assert deque.peek() == 1


def test_peek_tail_positive(full_deq):
    deque = full_deq

    assert deque.peek_tail() == 4


def test_peek_tail_boundary_empty():
    deque = Deque()

    assert deque.peek_tail() is None


def test_peek_tail_boundary_one_item(one_item):
    deque = one_item

    assert deque.peek_tail() == 1


def test_is_empty_positive_true():
    queue = Deque()

    assert queue.is_empty() == True


def test_is_empty_positive_false(one_item):
    queue = one_item

    assert queue.is_empty() == False

