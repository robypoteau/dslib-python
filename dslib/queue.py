"""Create of object where the last object to enter the data structure is
the last object to be removed. First IN First OUT (FIFO).

Functions:

    * enqueue(item)
    * dequeue()
    * peek()
    * size()
    * is_empty()
"""


class Queue():
    def __init__(self):
        """Constructor for queue class.
        """
        self.__list = []

    def __repr__(self):
        """
        """
        return f"<{self.__class__.__name__} at {hex(id(self))}"

    def __len__(self):
        """Return the size of the queue.

        This operations runs in constant time, O(1).

        Returns
        -------
        Integer
            List size
        """
        return len(self.__list)

    def enqueue(self, data):
        """Add an element to the back of a queue.

        This operation runs in constant time, O(n).

        Parameters
        ----------
        data : Object
            Data is an object of any type
        """
        self.__list.insert(0, data)

    def dequeue(self):
        """Remove an element from the front of a queue.

        This operations runs in linear time, O(1).

        Returns
        -------
        data : Object
            Data is an object of any type
        """
        if self.__list:
            return self.__list.pop()
        return None

    def peek(self):
        """Show the element at the front of the queue.

        This operations runs in linear time, O(1).

        Returns
        -------
        data : Object
            Data is an object of any type
        """
        if self.__list:
            return self.__list[-1]
        return None

    def size(self):
        """Return the size of the queue.

        This operations runs in constant time, O(1).

        Returns
        -------
        Integer
            List size
        """
        return len(self.__list)

    def is_empty(self):
        """Reveals whether the queue is empty.

        This operations runs in constant time, O(1).

        Returns
        -------
        Boolean
            Returns True is the queue is empty
        """
        return len(self.__list) == 0
