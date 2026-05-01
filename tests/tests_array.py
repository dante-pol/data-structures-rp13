import pytest

from src.array import List


@pytest.fixture
def create_list_has_not_free_memory() -> List:
    array = List()

    array.add(1)
    array.add(2)
    array.add(3)
    array.add(4)

    return array


@pytest.fixture
def create_list_has_free_memory() -> List:
    array = List()

    array.add(1)
    array.add(2)
    array.add(3)
    array.add(4)
    array.add(5)

    return array


def test_add_positive():
    array = List()

    array.add(1)
    array.add(2)

    assert str(array) == '[1, 2, None, None]'


def test_add_boundary():
    array = List()

    array.add(1)
    array.add(2)
    array.add(3)
    array.add(4)

    assert str(array) == '[1, 2, 3, 4]'


def test_remove_positive(create_list_has_free_memory):
    array = create_list_has_free_memory
    array.remove(3)

    assert str(array) == '[1, 2, 4, 5, None, None]'


def test_remove_boundary(create_list_has_not_free_memory):
    array = create_list_has_not_free_memory
    array.remove(1)

    assert str(array) == '[2, 3, 4, None]'


def test_sort_boundary(create_list_has_free_memory):
    array = create_list_has_free_memory
    array.sort(order_by= lambda x, y: x > y)

    assert str(array) == '[5, 4, 3, 2, 1, None]'


def test_sort_positive(create_list_has_not_free_memory):
    array = create_list_has_not_free_memory
    array.sort()

    assert str(array) == '[1, 2, 3, 4]'


def test_is_empty_positive_true():
    array = List()

    assert array.is_empty() == True


def test_is_empty_positive_false():
    array = List()
    array.add(1)

    assert array.is_empty() == False


def test_add_head_positive(create_list_has_free_memory):
    array = create_list_has_free_memory

    array.add_head(0)

    assert str(array) == '[0, 1, 2, 3, 4, 5]'


def test_add_head_boundary(create_list_has_not_free_memory):
    array = create_list_has_not_free_memory

    array.add_head(0)

    assert str(array) == '[0, 1, 2, 3, 4, None]'


def test_insert_positive(create_list_has_free_memory):
    array = create_list_has_free_memory

    array.insert(0, 3)

    assert str(array) == '[1, 2, 3, 0, 4, 5]'


def test_insert_boundary(create_list_has_not_free_memory):
    array = create_list_has_not_free_memory

    array.insert(0, 3)

    assert str(array) == '[1, 2, 3, 0, 4, None]'


def test_insert_negative():
    array = List()

    with pytest.raises(ValueError):
        array.insert(0, 1)

    with pytest.raises(ValueError):
        array.insert(0, -1)


def test_pop_positive(create_list_has_not_free_memory):
    array = create_list_has_not_free_memory

    array.pop(1)

    assert str(array) == '[1, 3, 4, None]'


def test_pop_boundary(create_list_has_not_free_memory):
    array = create_list_has_not_free_memory

    array.pop(3)

    assert str(array) == '[1, 2, 3, None]'


def test_pop_negative():
    array = List()

    with pytest.raises(ValueError):
        array.pop(1)

    with pytest.raises(ValueError):
        array.pop(-1)


def test_count_positive(create_list_has_free_memory):
    array = create_list_has_free_memory

    assert array.count(2) == 1

def test_count_boundary(create_list_has_free_memory):
    array = create_list_has_free_memory

    assert array.count(7) == 0


def test_find_positive(create_list_has_free_memory):
    array = create_list_has_free_memory

    assert array.find(2) == 1


def test_find_boundary(create_list_has_free_memory):
    array = create_list_has_free_memory

    assert array.find(7) == -1


def test_reverse_positive(create_list_has_not_free_memory):
    array = create_list_has_not_free_memory

    array.reverse()

    assert str(array) == '[4, 3, 2, 1]'


def test_reverse_boundary(create_list_has_free_memory):
    array = create_list_has_free_memory

    array.reverse()

    assert str(array) == '[5, 4, 3, 2, 1, None]'