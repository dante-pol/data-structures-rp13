import pytest

from src.hash_map import HashMap2


@pytest.fixture()
def create_hash_map1():
    hash_map = HashMap2(5)

    hash_map.add("a", 1)
    hash_map.add("b", 2)

    return hash_map

def test_add_positive(create_hash_map1):
    hash_map = create_hash_map1

    hash_map.add("c", 3)

    assert hash_map.get_memory() == [None, None, [('a', 1), ('b', 2), ('c', 3)], None, None]


def test_add_positive_empty():
    hash_map = HashMap2(3)

    hash_map.add("a", 1)

    assert hash_map.get_memory() == [None, None, [('a', 1)]]


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
    assert hash_map.get_memory() == [None, None, [('b', 2)], None, None]


def test_remove_boundary_from_coliseum(create_hash_map1):
    hash_map = create_hash_map1

    assert hash_map.remove("b") == 2
    assert hash_map.get_memory() == [None, None, [('a', 1)], None, None]


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



