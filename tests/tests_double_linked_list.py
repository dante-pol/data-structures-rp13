import pytest

from src.double_linked_list import DoubleLinkedList


@pytest.fixture()
def create_fuel_double_linked_list():
    list = DoubleLinkedList()

    list.add_last(1)
    list.add_last(2)
    list.add_last(3)
    list.add_last(4)

    return list

@pytest.fixture()
def create_empty_double_linked_list():
    list = DoubleLinkedList()

    return list

@pytest.fixture()
def create_double_linked_list_one_item():
    list = DoubleLinkedList()

    list.add_last(1)

    return list


def test_add_last_positive(create_fuel_double_linked_list):
    list = create_fuel_double_linked_list

    list.add_last(5)

    assert list.show() == [1,2,3,4,5]


def test_add_last_boundary(create_empty_double_linked_list):
    list = create_empty_double_linked_list

    list.add_last(1)

    assert list.show() == [1]


def test_add_head_positive(create_fuel_double_linked_list):
    list = create_fuel_double_linked_list

    list.add_head(0)

    assert list.show() == [0,1,2,3,4]


def test_add_head_boundary(create_empty_double_linked_list):
    list = create_empty_double_linked_list

    list.add_head(1)

    assert list.show() == [1]


def test_delete_first_positive(create_fuel_double_linked_list):
    list = create_fuel_double_linked_list

    assert list.delete_first().data == 1

    assert list.show() == [2,3,4]


def test_delete_first_boundary_empty(create_empty_double_linked_list):
    list = create_empty_double_linked_list

    assert list.delete_first() is None

    assert list.show() == []


def test_delete_first_boundary_one_item(create_double_linked_list_one_item):
    list = create_double_linked_list_one_item

    assert list.delete_first().data == 1

    assert list.show() == []


def test_delete_last_positive(create_fuel_double_linked_list):
    list = create_fuel_double_linked_list

    assert list.delete_last().data == 4

    assert list.show() == [1,2,3]


def test_delete_last_boundary_empty(create_empty_double_linked_list):
    list = create_empty_double_linked_list

    assert list.delete_last() is None

    assert list.show() == []


def test_delete_last_boundary_one_item(create_double_linked_list_one_item):
    list = create_double_linked_list_one_item

    assert list.delete_last().data == 1

    assert list.show() == []


def test_insert_positive(create_fuel_double_linked_list):
    list = create_fuel_double_linked_list

    list.insert(2, 10)
    assert list.show() == [1,2,10,3,4]


def test_insert_boundary_in_head(create_fuel_double_linked_list):
    list = create_fuel_double_linked_list

    list.insert(0, 10)

    assert list.show() == [10, 1,2,3,4]


def test_insert_boundary_in_tail(create_fuel_double_linked_list):
    list = create_fuel_double_linked_list

    list.insert(4, 10)

    assert list.show() == [1,2,3,4,10]


def test_insert_boundary(create_double_linked_list_one_item):
    list = create_double_linked_list_one_item

    list.insert(0, 10)

    assert list.show() == [10, 1]


def test_insert_negative(create_empty_double_linked_list):
    list = create_empty_double_linked_list

    with pytest.raises(ValueError):
        list.insert(1, 10)


def test_get_positive(create_fuel_double_linked_list):
    list = create_fuel_double_linked_list

    assert list.get(2).data == 3


def test_get_negative(create_empty_double_linked_list):
    list = create_empty_double_linked_list

    with pytest.raises(ValueError):
        list.get(4)


def test_remove_positive(create_fuel_double_linked_list):
    list = create_fuel_double_linked_list

    assert list.remove(2).data == 2

    assert list.show() == [1,3,4]


def test_remove_first_item(create_fuel_double_linked_list):
    list = create_fuel_double_linked_list

    assert list.remove(1).data == 1

    assert list.show() == [2, 3, 4]


def test_remove_last_item(create_fuel_double_linked_list):
    list = create_fuel_double_linked_list

    assert list.remove(4).data == 4

    assert list.show() == [1,2,3]


def test_remove_boundary(create_empty_double_linked_list):
    list = create_empty_double_linked_list

    assert list.remove(2) is None


def test_find_positive(create_fuel_double_linked_list):
    list = create_fuel_double_linked_list

    assert list.find(2).data == 2


def test_find_negative(create_empty_double_linked_list):
    list = create_empty_double_linked_list

    assert list.find(3) is None


def test_count_positive(create_fuel_double_linked_list):
    list = create_fuel_double_linked_list

    assert list.count() == 4


def test_count_boundary(create_empty_double_linked_list):
    list = create_empty_double_linked_list

    assert list.count() == 0


def test_is_empty_positive_fuel(create_fuel_double_linked_list):
    list = create_fuel_double_linked_list

    assert list.is_empty() == False


def test_is_empty_positive_empty(create_empty_double_linked_list):
    list = create_empty_double_linked_list

    assert list.is_empty() == True