import pytest
from dslib.stack import Stack


def test_empty_constructor():
    stack = Stack()
    assert stack.items == []


def test_int_constructor():
    list = [1, 2, 5, 7]
    stack = Stack(list=list, stack_type=int)
    assert stack.items == [1, 2, 5, 7]
    with pytest.raises(TypeError):
        list2 = [1, 1.4]
        stack2 = Stack(list=list2, stack_type=int)
        assert stack2.items == list2


def test_str_constructor():
    list = ['text1', 'text2']
    stack = Stack(list=list, stack_type=str)
    assert stack.items == ['text1', 'text2']
    with pytest.raises(TypeError):
        list2 = [1, 'op', 1.4]
        stack2 = Stack(list=list2, stack_type=int)
        assert stack2.items == list2


def test_float_constructor():
    list = [1.4, 2.3, 4.5]
    stack = Stack(list=list, stack_type=float)
    assert stack.items == [1.4, 2.3, 4.5]
    with pytest.raises(TypeError):
        list2 = [1, 1.4]
        stack2 = Stack(list=list2, stack_type=int)
        assert stack2.items == list2


def test_mixed_constructor():
    list = [1, 'text', 4.5]
    stack = Stack(list=list)
    assert stack.items == [1, 'text', 4.5]


def test_push():
    stack = Stack()
    test_list = []
    for i in range(3):
        stack.push(i)
        test_list.append(i)
        assert stack.items == test_list

    assert stack.items == [0, 1, 2]


def test_pop():
    stack = Stack(list=[0, 1, 2])
    assert stack.pop() == 2
    assert stack.items == [0, 1]


def test_peek():
    stack = Stack(list=[0, 1, 2])
    assert stack.peek() == 2
    assert stack.items == [0, 1, 2]


def test_size():
    stack = Stack()
    for i in range(3):
        stack.push(i)
        # assert stack.size() == i+1
    print(stack.items)


def test_is_empty():
    pass
