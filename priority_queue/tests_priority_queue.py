import pytest

from priority_queue.priority_queue import PriorityQueue


@pytest.fixture()
def one_priority():
    priority_queue = PriorityQueue()

    priority_queue.enqueue(2, "twice1")
    priority_queue.enqueue(2, "twice2")
    priority_queue.enqueue(2, "twice3")

    return priority_queue


@pytest.fixture()
def three_priority():
    priority_queue = PriorityQueue()

    priority_queue.enqueue(1, "first")
    priority_queue.enqueue(2, "twice")
    priority_queue.enqueue(3, "three")
    priority_queue.enqueue(1, "first1")
    priority_queue.enqueue(2, "twice1")
    priority_queue.enqueue(3, "three1")

    return priority_queue


def test_enqueue_positive(one_priority):
    queue = one_priority

    queue.enqueue(1, "first1")

    assert queue.peek() == "first1"


def test_enqueue_boundary():
    queue = PriorityQueue()

    queue.enqueue(3, "three")

    assert queue.peek() == "three"


def test_dequeue_positive(three_priority):

    queue = three_priority

    assert queue.dequeue() == "first"
    assert queue.dequeue() == "first1"
    assert queue.dequeue() == "twice"
    assert queue.dequeue() == "twice1"


def test_dequeue_boundary():

    queue = PriorityQueue()

    assert queue.dequeue() is None


def test_peek_positive(one_priority):

    queue = one_priority

    assert queue.peek() == "twice1"


def test_peek_boundary():
    queue = PriorityQueue()

    assert queue.peek() is None


def test_is_empty_positive_true():
    queue = PriorityQueue()

    assert queue.is_empty() == True


def test_is_empty_positive_false(one_priority):
    queue = one_priority

    assert queue.is_empty() == False

