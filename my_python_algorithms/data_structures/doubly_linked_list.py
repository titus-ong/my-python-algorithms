"""
Doubly linked list implementation.
Each node has pointers to the previous and next node.

Time complexity:
Append - O(n)
Search - O(n)
Insert - O(1) (given pointer at the inserted index)
Delete - O(1) (likewise ^)

Space complexity: O(n)
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self, head=None):
        self.head = Node(head) if head is not None else head

    def append(self, value):
        """Append value to the end of the DLL."""
        n = Node(value)
        if not self.head:
            self.head = n
            return
        current = self.head
        while current.next:
            current = current.next
        current.next, n.prev = n, current

    def _get_node(self, index):
        """Return node at the given index."""
        if not self.head:
            raise IndexError
        current = self.head
        for _ in range(index):
            if not current.next:
                raise IndexError
            current = current.next
        return current

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

    def insert(self, index, value):
        """Insert the value at the given index."""
        n = Node(value)
        if not self.head and index == 0:
            self.head = n
            return
        if index == 0:
            self.head.prev, n.next = n, self.head
            self.head = n
            return
        prev = self._get_node(index - 1)
        n.next, n.prev = prev.next, prev
        prev.next = n

    def delete(self, index):
        """Delete the value at the given index."""
        deleted = self._get_node(index)
        if index == 0:
            temp = self.head
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            temp.prev, temp.next = None, None
            return
        prev = deleted.prev
        next_ = deleted.next
        prev.next = next_
        if next_:
            next_.prev = prev
        deleted.prev, deleted.next = None, None

    def __getitem__(self, index):
        """Return value at given index e.g. dll[1]"""
        return self._get_node(index).value
