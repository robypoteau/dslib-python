"""Create of object where the last object to enter the data structure is
the first object to be removed. Last IN First OUT (FIFO).

Functions:

    * get_data
    * set_data
    * get_next
    * set_next
"""


class SLLNode:
    def __init__(self, data):
        """Constructor for the Stack class.
        """
        self.data = data
        self.next = None

    def get_data(self):
        """Get the data in the node.

        This operations runs in constant time, O(1).

        Returns
        -------
        Object
            Data in the node
        """
        return self.data

    def set_data(self, data):
        """Edit the data in the node.

        This operations runs in constant time, O(1).

        Parameters
        ----------
        data : Object
            Data is an object of any type
        """
        self.data = data

    def get_next(self):
        """Get the next-pointer to the next node.

        This operations runs in constant time, O(1).

        Returns
        -------
        SLLNode
            Pointer to a node
        """
        return self.next

    def set_next(self, next):
        """Edit the next-pointer to the next node.

        This operations runs in constant time, O(1).

        Parameters
        ----------
        next : SLLNode
            An singly linked list node
        """
        self.next = next

    def __repr__(self):
        return (
            f'<Data: {self.data},'
            f' Next: {self.next.get_data() if self.next else self.next}>'
        )
