"""Linked list-based stack implementation."""

from dsa.stacks_queues.base import Stack
from typing import TypeVar, Optional
from dsa.lists.linked_list import LinkedList

T = TypeVar('T')


class LinkedStack(Stack[T]):
    """Stack implementation using a singly linked list.

    The top of the stack is maintained at the head of the linked list,
    providing O(1) push and pop operations.

    """

    class _Node:
        """A node in the singly linked list."""
        __slots__ = '_element', '_next'

        def __init__(self, element: T, next: Optional['LinkedStack._Node'] = None):
            self._element = element
            self._next = next
            

    def __init__(self):
        self._head = None
        self._n = 0
        #raise NotImplementedError

    def push(self, item: T) -> None:
        if self._n == 0:
            self._head = self._Node(item, next = None)
        else:
            current_node = self._head
            while current_node._next is not None:
                current_node = current_node._next
            current_node._next = self._Node(item, None)
        self._n += 1
        #raise NotImplementedError

    def pop(self) -> T:
        if self._n == 0: 
            raise IndexError
        prev_node = None
        current_node = self._head
        while current_node._next is not None:
            prev_node = current_node
            current_node = current_node._next
        top_value = current_node._element
        if prev_node is not None:
            prev_node._next = None
        current_node._element = None
        self._n -= 1
        return top_value
        #raise NotImplementedError

    def top(self) -> T:
        if self._n == 0:
            raise IndexError
        if self._n == 0:
            return self._head._element
        else:
            current_node = self._head
            while current_node._next is not None:
                current_node = current_node._next
            return current_node._element
        #raise NotImplementedError

    def __len__(self) -> int:
        return self._n
        #raise NotImplementedError
