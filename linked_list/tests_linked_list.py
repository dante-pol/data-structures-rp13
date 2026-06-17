
import pytest

from linked_list.linked_list import LinkedList


@pytest.fixture()
def create_linked_list():
    linked_list = LinkedList()

    linked_list.add_last(1)
    linked_list.add_last(2)
    linked_list.add_last(3)
    linked_list.add_last(4)

    return linked_list


def test_add_last_positive(create_linked_list):

    linked_list = create_linked_list

    linked_list.add_last(5)

    assert linked_list.show() == [1,2,3,4,5]


def test_add_last_boundary():
    linked_list = LinkedList()

    linked_list.add_last(1)

    assert linked_list.show() == [1]


def test_add_head_positive(create_linked_list):
    linked_list = create_linked_list

    linked_list.add_head(0)

    assert linked_list.show() == [0,1,2,3,4]


def test_add_head_boundary():
    linked_list = LinkedList()

    linked_list.add_head(1)

    assert linked_list.show() == [1]


def test_insert_positive(create_linked_list):
    linked_list = create_linked_list

    linked_list.insert(3, 10)

    assert linked_list.show() == [1, 2, 3, 10, 4]


def test_insert_boundary():
    linked_list = LinkedList()

    linked_list.insert(0, 10)

    assert linked_list.show() == [10]


def test_insert_negative(create_linked_list):
    linked_list = create_linked_list

    with pytest.raises(ValueError):
        linked_list.insert(10, 10)


@pytest.mark.parametrize(
    "input, expected", [
        (0, 1),
        (1, 2),
        (2, 3),
        (3, 4)
    ]
)
def test_get_positive_and_boundary(create_linked_list, input, expected):
    linked_list = create_linked_list

    assert linked_list.get(input).data == expected


def test_get_negative(create_linked_list):
    linked_list = create_linked_list

    with pytest.raises(ValueError):
        linked_list.get(10)


def test_remove_positive(create_linked_list):
    linked_list = create_linked_list

    assert linked_list.remove(2).data == 2
    assert linked_list.show() == [1,3,4]


def test_remove_boundary():
    linked_list = LinkedList()

    assert linked_list.remove(4) is None
    assert linked_list.show() == []


def test_find_positive(create_linked_list):
    linked_list = create_linked_list

    assert linked_list.find(3).data == 3


def test_find_boundary():
    linked_list = LinkedList()

    assert linked_list.find(4) is None


def test_count_positive(create_linked_list):
    linked_list = create_linked_list

    assert linked_list.count() == 4


def test_count_boundary():
    linked_list = LinkedList()

    assert linked_list.count() == 0


def test_is_empty_true():
    linked_list = LinkedList()

    assert linked_list.is_empty() == True


def test_is_empty_positive(create_linked_list):
    linked_list = create_linked_list

    assert linked_list.is_empty() == False