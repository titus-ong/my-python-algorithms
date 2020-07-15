"""
Singly linked list implementation.

Time complexity:
Access - O(n)
Search - O(n)
Insert - O(1) (given pointer at the inserted index)
Delete - O(1) (likewise ^)

Space complexity: O(n)
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self, head=None):
        self.head = Node(head) if head is not None else head

    def append(self, value):
        """Append value to the end of the linked list."""
        if not self.head:
            self.head = Node(value)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(value)

    def index(self, value):
        """Return index of the first node with the given value."""
        if not self.head:
            raise ValueError
        current = self.head
        index = 0
        while current:
            if current.value == value:
                return index
            index += 1
            current = current.next
        raise ValueError

    def _get_indexed_node(self, index) -> Node:
        """Return node at given index."""
        if not self.head:
            raise IndexError
        current = self.head
        for _ in range(index):  # go to indexed node
            if not current.next:
                raise IndexError
            current = current.next
        return current

    def insert(self, index, value):
        """Insert value into the linked list at given index."""
        new_node = Node(value)
        if index == 0:  # inserting head
            new_node.next = self.head
            self.head = new_node
            return
        prev_node = self._get_indexed_node(index-1)
        new_node.next, prev_node.next = prev_node.next, new_node

    def delete(self, index):
        """Delete node at given index."""
        if not self.head:
            raise IndexError
        if index == 0:
            self.head = self.head.next
            return
        prev_node = self._get_indexed_node(index-1)
        if not prev_node.next:
            raise IndexError
        prev_node.next = prev_node.next.next

    def __getitem__(self, index):
        """Return value at given index e.g. linked[1]"""
        if not self.head:
            raise IndexError
        current = self._get_indexed_node(index)
        return current.value

