from src.stack import Stack


def test_peek():
    stack = Stack()
    stack.push(1)

    assert stack.peek() == 1

def test_push():
    stack = Stack()
    stack.push(1)
    stack.push(2)

    assert stack.peek() == 2

def test_pop():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.pop()
    assert stack.peek() == 1

def test_is_empty_positive():

    stack = Stack()
    assert stack.is_empty() == True

    stack.push(1)
    assert stack.is_empty() == False