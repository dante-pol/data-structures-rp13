from src.queue import Queue


def test_peek():
    queue = Queue()
    queue.enqueue(1)

    assert queue.peek() == 1

def test_enqueue():
    queue = Queue()
    queue.enqueue(1)

    assert queue.peek() == 1

def test_dequeue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.dequeue()
    assert queue.peek() == 2

def test_is_empty_positive():
    queue = Queue()
    assert queue.is_empty() == True

    queue.enqueue(1)
    assert queue.is_empty() == False