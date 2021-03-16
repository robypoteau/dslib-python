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
        self.head = None
        self.length = 0

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
        return self.length

    def __iter__(self):
        """
        """
        pass

    def __next__(self):
        """
        """
        pass

    def insert_node(self, data):
        """Add a new node to the front of the linked list.

        This operations runs in constant time, O(1).

        Parameters
        ----------
        data : Object
            Data is an object of any type
        """
        node = SLLNode(data)
        node.set_next(self.head)
        self.head = node
        self.length += 1

    def remove_node(self):
        """Remove the node from the front of the linked list.

        This operations runs in constant time, O(1).

        Returns
        -------
        Object
            Data in the node
        """
        if self.length == 0:
            raise IndexError("no nodes in this linked list.")
        data = self.head.get_data() if self.head else self.head
        self.head = self.head.get_next() if self.head else self.head
        self.length -= 1
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
        return self.length

    def is_empty(self):
        """
        """
        pass
