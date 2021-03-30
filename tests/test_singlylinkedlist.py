import pytest
from dslib.singlylinkedlist import LinkedList


def test_init():
    ll = LinkedList()
    assert ll is not None


def test_repr():
    pass


def test_iterator():
    ll = LinkedList()
    data = []
    for i in range(4):
        data.append(f'Datum{i}')
        ll.insert_node(data[i])

    i = -1
    for value in ll:
        assert value == data[i]
        i -= 1


def test_insert_node():
    ll = LinkedList()

    data1 = "Datum"
    ll.insert_node(data1)
    assert ll._LinkedList__head.get_data() == data1

    data2 = "Datum 2"
    ll.insert_node(data2)
    assert ll._LinkedList__head.get_data() == data2
    assert ll._LinkedList__head.get_next().get_data() == data1

    data3 = "Datum 3"
    ll.insert_node(data3)
    assert ll._LinkedList__head.get_data() == data3
    assert ll._LinkedList__head.get_next().get_data() == data2
    assert ll._LinkedList__head.get_next().get_next().get_data() == data1


def test_remove_node():
    ll = LinkedList()

    data1 = "Datum 1"
    ll.insert_node(data1)
    data2 = "Datum 2"
    ll.insert_node(data2)
    data3 = "Datum 3"
    ll.insert_node(data3)

    assert ll.remove_node() == data3
    assert ll.remove_node() == data2
    assert ll.remove_node() == data1

    with pytest.raises(IndexError):
        ll.remove_node()


def test_search():
    pass


def test_size():
    data1 = "Datum"
    ll = LinkedList()
    ll.insert_node(data1)
    assert ll.size() == 1
    data2 = "Datum 2"
    ll.insert_node(data2)
    assert ll.size() == 2
    data3 = "Datum 3"
    ll.insert_node(data3)
    assert ll.size() == 3
    ll.remove_node()
    assert ll.size() == 2
    ll.remove_node()
    assert ll.size() == 1
    ll.remove_node()
    assert ll.size() == 0

    with pytest.raises(IndexError):
        ll.remove_node()


def test_is_empty():
    data = "Datum"
    ll = LinkedList()
    assert ll.is_empty() is True

    ll.insert_node(data)
    assert ll.is_empty() is False
