from dslib.sllnode import SLLNode

"""Create an object that enables you to construct a list of elements which are
placed in nodes, in particularly the SLLNode class. Linked lists can grow
dynamically without concern for elements being contiguous in memory. Each
element points to the next element in the list.

Functions:
    * insert_node
    * remove_node
    * search
    * size
    * is_empty
"""


class LinkedList():
    def __init__(self):
        """Constructor for the LinkedList class.
        """
        self.__head = None
        self.__length = 0

    def __repr__(self):
        """
        """
        pass

    def __len__(self):
        """Return the size of the linked list.

        This operations runs in constant time, O(1).

        Returns
        -------
        Integer
            List size
        """
        return self.__length

    def __iter__(self):
        """
        """
        self.__current = self.__head
        return self

    def __next__(self):
        """
        """
        if self.__head:
            raise StopIteration
        else:
            current = self.__current.get_data()
            self.__current = self.__current.get_next()
        return current

    def insert_node(self, data):
        """Add a new node to the front of the linked list.

        This operations runs in constant time, O(1).

        Parameters
        ----------
        data : Object
            Data is an object of any type
        """
        node = SLLNode(data)
        node.set_next(self.__head)
        self.__head = node
        self.__length += 1

    def remove_node(self):
        """Remove the node from the front of the linked list.

        This operations runs in constant time, O(1).

        Returns
        -------
        Object
            Data in the node
        """
        if self.__head is None:
            raise IndexError("no nodes in this linked list.")

        data = self.__head.get_data()
        self.__head = self.__head.get_next()

        self.__length -= 1
        return data

    def search(self, data):
        """
        """
        pass

    def size(self):
        """Return the size of the linked list.

        This operations runs in constant time, O(1).

        Returns
        -------
        Integer
            List size
        """
        return self.__length

    def is_empty(self):
        """Reveals whether the linked list is empty.

        This operations runs in constant time, O(1).

        Returns
        -------
        Boolean
            Returns True is the linked list is empty
        """
        return self.__length == 0
