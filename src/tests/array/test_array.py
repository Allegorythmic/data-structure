import pytest
from datastruct.array import Array


def test_array_initialization():
    arr = Array(int)
    assert arr.data_type == int
    assert len(arr) == 0


def test_append_valid_type():
    arr = Array(int)
    arr.append(1)
    assert arr[0] == 1


def test_append_invalid_type():
    arr = Array(int)
    with pytest.raises(TypeError):
        arr.append("string")


def test_insert_valid_type():
    arr = Array(int)
    arr.append(1)
    arr.insert(0, 2)
    assert arr[0] == 2
    assert arr[1] == 1


def test_insert_invalid_type():
    arr = Array(int)
    arr.append(1)
    with pytest.raises(TypeError):
        arr.insert(0, "string")


def test_remove():
    arr = Array(int)
    arr.append(1)
    arr.append(2)
    arr.remove(1)
    assert len(arr) == 1
    assert arr[0] == 2


def test_remove_nonexistent_value():
    arr = Array(int)
    arr.append(1)
    with pytest.raises(ValueError):
        arr.remove(2)


def test_pop():
    arr = Array(int)
    arr.append(1)
    arr.append(2)
    value = arr.pop()
    assert value == 2
    assert len(arr) == 1
    assert arr[0] == 1


def test_pop_with_index():
    arr = Array(int)
    arr.append(1)
    arr.append(2)
    value = arr.pop(0)
    assert value == 1
    assert len(arr) == 1
    assert arr[0] == 2


def test_getitem():
    arr = Array(int)
    arr.append(1)
    assert arr[0] == 1


def test_setitem_valid_type():
    arr = Array(int)
    arr.append(1)
    arr[0] = 2
    assert arr[0] == 2


def test_setitem_invalid_type():
    arr = Array(int)
    arr.append(1)
    with pytest.raises(TypeError):
        arr[0] = "string"


def test_len():
    arr = Array(int)
    assert len(arr) == 0
    arr.append(1)
    assert len(arr) == 1


def test_repr():
    arr = Array(int)
    arr.append(1)
    arr.append(2)
    assert repr(arr) == "Array(int, [1, 2])"
