"""Create of object that reference another data object and two other nodes
object, one occurring before it and the other after it.

Functions:

    * get_data
    * set_data
    * get_next
    * set_next
    * get_prev
    * set_prev
"""


class DLLNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

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
        DLLNode
            Pointer to a node
        """
        return self.next

    def set_next(self, next):
        """Edit the next-pointer to the next node.

        This operations runs in constant time, O(1).

        Parameters
        ----------
        next : DLLNode
            A doubly linked list node
        """
        self.next = next

    def get_prev(self):
        """Get the prev-pointer to the previous node.

        This operations runs in constant time, O(1).

        Returns
        -------
        DLLNode
            Pointer to a node
        """
        return self.prev

    def set_prev(self, prev):
        """Edit the prev-pointer to the previous node.

        This operations runs in constant time, O(1).

        Parameters
        ----------
        next : DLLNode
            A doubly linked list node
        """
        self.prev = prev

    def __repr__(self):
        return (
            f'<Data: {self.data},'
            f' Next: {self.next.get_data() if self.next else self.next}',
            f' Prev: {self.prev.get_data() if self.prev else self.prev}>'
        )
