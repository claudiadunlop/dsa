"""Stack, queue, and deque implementations."""

from dsa.stacks_queues.base import Stack, Queue, Deque
from dsa.stacks_queues.array_stack import ArrayStack
from dsa.stacks_queues.linked_stack import LinkedStack
from dsa.stacks_queues.array_queue import ArrayQueue
from dsa.stacks_queues.linked_queue import LinkedQueue
from dsa.stacks_queues.deque import ArrayDeque

__all__ = [
    'Stack', 'Queue', 'Deque',
    'ArrayStack', 'LinkedStack',
    'ArrayQueue', 'LinkedQueue',
    'ArrayDeque'
]
