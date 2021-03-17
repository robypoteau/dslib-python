"""Create of object where the last object to enter the data structure is
the first object to be removed. Last IN First OUT (FIFO).

Functions:

    * push(item)
    * pop()
    * peek()
    * size()
    * is_empty()
"""


class Stack:
    def __init__(self, list=[], stack_type=object):
        """Constructor for the Stack class.
        """
        if stack_type == object:
            pass
        else:
            for item in list:
                if type(item) is not stack_type:
                    raise TypeError("An element of the list is not a \
                        {self.stack_type}")

        self.items = list
        self.stack_type = stack_type

    def push(self, item):
        """Adds the item parameter to the top of the stack.

        This operations runs in constant time, O(1).

        Parameters
        ----------
        item : Object
            Item is an object of any type
        """

        if self.stack_type == object:
            pass
        elif type(item) is not self.stack_type:
            raise TypeError("Item is not an {self.stack_type}")

        return self.items.append(item)

    def pop(self):
        """Removes an item from the top of the stack.

        This operations runs in constant time, O(1).

        Returns
        -------
        Object
            Item on the top of the stack
        """
        return self.items.pop()

    def peek(self):
        """Outputs the value of the element on the top of the stack.

        This operations runs in constant time, O(1).

        Returns
        -------
        Object
            Item on the top of the stack
        """

        try:
            return self.items[-1]
        except IndexError:
            return None

    def size(self):
        """Outputs the value of the element on the top of the stack.

        This operations runs in constant time, O(1), because len() runs in
        constant time since python tracks number of records in list.

        Returns
        -------
        Integer
            Size of the stack
        """
        return len(self.items)

    def is_empty(self):
        """Reveals whether the stack is empty.

        This operations runs in constant time, O(1).

        Returns
        -------
        Boolean
            Returns True is the stack is empty
        """
        return self.items == []

    def __repr__(self):
        return f'Stack(,type:{self.stack_type})'
