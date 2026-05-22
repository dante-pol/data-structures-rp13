import pytest

from hash_map.hash_map import HashMap1


@pytest.fixture()
def create_hash_map1():
    hash_map = HashMap1(5)

    hash_map.add("a", 1)
    hash_map.add("b", 2)

    return hash_map

def test_add_positive(create_hash_map1):
    hash_map = create_hash_map1

    hash_map.add("c", 3)

    assert hash_map.get_memory() == [2, 3, 1, None, None]

def test_add_boundary_fuel_memory(create_hash_map1):
    hash_map = create_hash_map1

    hash_map.add("c", 3)
    hash_map.add("d", 4)
    hash_map.add("e", 5)
    hash_map.add("f", 6)


    assert hash_map.get_memory() == [2, 3, 1, 4, 5, 6, None, None, None, None]


def test_add_positive_empty():
    hash_map = HashMap1(3)

    hash_map.add("a", 1)

    assert hash_map.get_memory() == [None, None, 1]


def test_add_positive_overwriting(create_hash_map1):
    hash_map = create_hash_map1

    hash_map.add("a", 5)

    assert hash_map.get("a") == 5


def test_get_positive(create_hash_map1):
    hash_map = create_hash_map1

    assert hash_map.get("b") == 2


def test_get_negative(create_hash_map1):
    hash_map = create_hash_map1

    with pytest.raises(ValueError):
        hash_map.get("c")


def test_remove_positive_from_index(create_hash_map1):
    hash_map = create_hash_map1

    assert hash_map.remove("a") == 1
    assert hash_map.get_memory() == [2, None, None, None, None]


def test_remove_boundary_from_coliseum(create_hash_map1):
    hash_map = create_hash_map1

    assert hash_map.remove("b") == 2
    assert hash_map.get_memory() == [None, None, 1, None, None]


def test_remove_negative(create_hash_map1):
    hash_map = create_hash_map1

    with pytest.raises(ValueError):
        hash_map.remove("v")


def test_count(create_hash_map1):
    hash_map = create_hash_map1

    assert hash_map.count() == 2

    hash_map.add("c", 3)

    assert hash_map.count() == 3

    hash_map.remove("b")

    assert hash_map.count() == 2



