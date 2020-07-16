"""
Stack implementation.
LIFO structure where elements are pushed to the top of the stack and popped off the top of the stack.
Python's list can be used as a stack - using a linked list is for learning purposes.

Time complexity:
Push - O(1)
Pop - O(1)
Peek - O(1)

Space complexity: O(n)
"""


from my_python_algorithms.data_structures.linked_list import LinkedList, Node


class EmptyStackException(Exception):
    pass


class Stack(LinkedList):
    def peek(self):
        """Return topmost value."""
        if self.head:
            return self.head.value
        raise EmptyStackException

    def push(self, value):
        """Push a value to the top of the stack."""
        temp = self.head
        self.head = Node(value)
        self.head.next = temp

    def pop(self):
        """Pop off and return the topmost value."""
        if not self.head:
            raise EmptyStackException
        temp = self.head
        self.head = self.head.next
        temp.next = None
        return temp.value
