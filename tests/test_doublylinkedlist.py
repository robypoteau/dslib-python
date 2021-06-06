import pytest
from dslib.doublylinkedlist import DoublyLinkedList


def test_constructor():
    dll = DoublyLinkedList()
    assert dll is not None


@pytest.fixture()
def setup():
    pass


def test_front_insertion():
    dll = DoublyLinkedList()

    str_obj = "String"
    num_obj = 132.432
    list_obj = [1, 2, 3]
    dict_obj = {"Key1": 1, "Key2": 2}

    dll.insert_front(str_obj)
    assert dll._DoublyLinkedList__head.get_data() == str_obj

    dll.insert_front(num_obj)
    assert dll._DoublyLinkedList__head.get_data() == num_obj

    dll.insert_front(list_obj)
    assert dll._DoublyLinkedList__head.get_data() == list_obj

    dll.insert_front(dict_obj)
    assert dll._DoublyLinkedList__head.get_data() == dict_obj


def test_back_insertion():
    dll = DoublyLinkedList()

    str_obj = "String"
    num_obj = 132.432
    list_obj = [1, 2, 3]
    dict_obj = {"Key1": 1, "Key2": 2}

    dll.insert_end(str_obj)
    assert dll._DoublyLinkedList__tail.get_data() == str_obj

    dll.insert_end(num_obj)
    assert dll._DoublyLinkedList__tail.get_data() == num_obj

    dll.insert_end(list_obj)
    assert dll._DoublyLinkedList__tail.get_data() == list_obj

    dll.insert_end(dict_obj)
    assert dll._DoublyLinkedList__tail.get_data() == dict_obj


def test_search():
    pass


def test_node_removal():
    pass


def test_size():
    pass


def test_is_empty():
    pass


def test_iterable():
    pass
