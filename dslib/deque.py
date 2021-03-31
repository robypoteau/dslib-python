"""Create of list object where values can be appended and removed on both side.

Functions:
    * add_front(item)
    * remove_front()
    * add_rear(item)
    * remove_rear()
    * peek_front()
    * peek_rear()
    * size()
    * is_empty()
"""


class Deque():

    def __init__(self):
        self.__list = []

    def __repr__(self):
        return f"{self.__class__.__name__} at  {hex(id(self))}"

    def __len__(self):
        return len(self.__list)

    def __iter__(self):
        """Outputs the elements starting from the front.
        """
        self.__index = 0
        return self

    def __next__(self):
        try:
            item = self.__list[self.__index]
        except Exception:
            raise StopIteration

        self.__index += 1
        return item

    def add_front(self, data):
        """Add an element to the front of the deque.

        Parameters
        ----------
        data : Object
            Data is an object of any type
        """
        self.__list.insert(0, data)

    def remove_front(self):
        """Remove an element in the front of the deque.

        Returns
        -------
        Object
            Data is an object of any type
        """
        if len(self.__list) > 0:
            item = self.__list[0]
            self.__list.pop(0)
            return item
        return None

    def peek_front(self):
        """Show the element at the front of the queue.

        Returns
        -------
        Object
            Data is an object of any type
        """
        if len(self.__list) > 0:
            return self.__list[0]
        return None

    def add_rear(self, data):
        """Add an element to the end of the deque.

        Parameters
        ----------
        data : Object
            Data is an object of any type
        """
        self.__list.append(data)

    def remove_rear(self):
        """Remove an element in the end of the deque.

        Returns
        -------
        Object
            Data is an object of any type
        """
        if len(self.__list) > 0:
            item = self.__list[-1]
            self.__list.pop()
            return item
        return None

    def peek_rear(self):
        """Show the element at the end of the queue.

        Returns
        -------
        Object
            Data is an object of any type
        """
        if len(self.__list) > 0:
            return self.__list[-1]
        return None

    def size(self):
        """Return the size of the linked list.

        This operations runs in constant time, O(1).

        Returns
        -------
        Integer
            List size
        """
        return len(self.__list)

    def is_empty(self):
        """Reveals whether the linked list is empty.

        This operations runs in constant time, O(1).

        Returns
        -------
        Boolean
            Returns True is the linked list is empty
        """
        return self.__list == []
