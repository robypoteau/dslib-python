from dslib.dllnode import DLLNode

"""A pointer to the current element in a list of DLL nodes. This structure can
grow dynamically at both end of the list.

Functions:
    * insert_front
    * insert_end
    * remove_node
    * search
    * size
    * is_empty
"""


class DoublyLinkedList(object):
    """docstring for DoublyLinkedList."""

    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__length = 0

    def __len__(self):
        return self.__length

    def __repr__(self):
        pass

    def __iter__(self):
        """Traverse the linked list from the head to the tail.
        """
        pass

    def __next__(self):
        pass

    def insert_front(self, data):
        """Add a node to the front (head) of the linked list.

        This operation runs in constant time, O(1).

        Parameters
        ----------
        data : Object
            Data is an object of any type
        """
        dllnode = DLLNode(data)
        self.__head = dllnode
        self.__length += 1

    def insert_end(self, data):
        """Add a node to the end (tail) of the linked list.

        This operation runs in constant time, O(1).

        Parameters
        ----------
        data : Object
            Data is an object of any type
        """
        dllnode = DLLNode(data)
        self.__tail = dllnode
        self.__length += 1

    def remove_node(self, data):
        """Remove the first node, going from head to tail, containing the data
        parameter.

        Parameters
        ----------
        data : Object
            Data is an object of any type
        """
        pass

    def search(self, data):
        """Search for the first node, going from head to tail, containing the
        data parameter.

        Parameters
        ----------
        data : Object
            Data is an object of any type
        """
        pass

    def size(self):
        return self.__length

    def is_empty(self):
        return self.__length == 0
