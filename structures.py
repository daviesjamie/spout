import abc
import multiprocessing
import Queue


class Operation(object):
    """
    Defines an operation that can be applied to items in a stream.
    """

    @abc.abstractmethod
    def perform(self, obj):
        pass


class Predicate(object):
    """
    Used to apply a boolean test to items in a stream, to determine if it meets some set
    criteria.
    """

    @abc.abstractmethod
    def test(self, obj):
        pass


class Function(object):
    """
    Applies a function to items in a stream, producing an appropriate result.
    """

    @abc.abstractmethod
    def apply(self, input):
        pass


class BufferedQueue(object):
    """
    Abstract implementation of a queue with a finite capacity. If the queue becomes full and
    further items are added, then those elements are dropped. In addition, if an item is
    requested from the queue and no items are present, then the system waits for an item to be
    added before returning.
    """

    @abc.abstractmethod
    def offer(self, item):
        """
        Inserts the specified element into the queue, but only if it is possible to do so
        immediately without violating capacity restrictions. Returns True if the item was added,
        and False if there is no space currently available.
        """
        pass

    @abc.abstractmethod
    def take(self):
        """
        Retrieves and removes the head of this queue, waiting if necessary until an element
        becomes available.
        """
        pass

    @abc.abstractmethod
    def remaining_capacity(self):
        """
        Returns the number of additional elements that this queue can hold (assuming no other
        constraints).
        """
        pass


class QueueBufferedQueue(BufferedQueue):
    """
    Implementation of a BufferedQueue using Python's Queue library as the backing data structure.
    """
    def __init__(self, capacity):
        self.max_size = capacity
        self.queue = multiprocessing.Queue(capacity)

    def offer(self, item):
        try:
            self.queue.put(item, False)
        except Queue.Full:
            return False

        return True

    def take(self):
        return self.queue.get(True)

    def remaining_capacity(self):
        return self.remaining_capacity() - self.queue.qsize()