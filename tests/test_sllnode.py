from dslib.sllnode import SLLNode


def test_constructor():
    data = 'First Item'
    ll = SLLNode(data)
    assert ll.data == data


def test_get_data():
    data = [1, 2, 3]
    ll = SLLNode(data)
    assert ll.get_data() == data


def test_set_data():
    data = [1, 2, 3]
    ll = SLLNode(data)
    assert ll.get_data() == data

    data = {"Key": "Value"}
    ll.set_data(data)
    assert ll.get_data() == data


def test_get_next():
    ll1 = SLLNode('Datum 1')
    ll2 = SLLNode('Datum 2')
    assert ll1.get_next() is None

    ll1.next = ll2
    assert ll1.get_next() == ll2


def test_set_next():
    ll1 = SLLNode('Datum 1')
    ll2 = SLLNode('Datum 2')
    assert ll1.get_next() is None

    ll1.set_next(ll2)
    assert ll1.get_next() == ll2


def test_repr():
    repr = "<Data: Datum, Next: None>"
    ll = SLLNode('Datum')
    assert str(ll) == repr

    ll2 = SLLNode('Datum2')
    ll.set_next(ll2)
    repr = "<Data: Datum, Next: Datum2>"
    assert str(ll) == repr
    assert str(ll.get_next()) == "<Data: Datum2, Next: None>"
    assert str(ll2.get_next()) == "None"
