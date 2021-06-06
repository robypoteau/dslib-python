from dslib.dllnode import DLLNode


def test_data_access():
    init_data = 'Initial Data'
    dnode = DLLNode(init_data)
    assert dnode.get_data() == init_data

    num_data = 1234.567
    dnode.set_data(num_data)
    assert dnode.get_data() == num_data


def test_get_set_adjacent_nodes():
    dn1 = DLLNode("First Node")
    dn2 = DLLNode("Second Node")
    dn3 = DLLNode("Third Node")

    dn2.set_prev(dn1)
    dn2.set_next(dn3)

    assert dn2.get_prev().get_data() == dn1.get_data()
    assert dn2.get_next().get_data() == dn3.get_data()
