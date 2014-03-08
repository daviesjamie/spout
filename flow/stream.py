import abc


class AbstractStream(object):
    """
    Abstract implementation of a read-only data stream.
    """

    __metaclass__ = abc.ABCMeta

    def for_each(self, operation, limit=0):
        """
        Applies the given Operation to each item in the stream. The Operation executes on the
        items in the stream in the order that they appear in the stream.

        If the limit is supplied, then processing of the stream will stop after that many items
        have been processed.
        """
        if limit != 0:
            count = 0
            while self.has_next():
                operation.perform(self.next())
                count += 1
                if count >= limit:
                    break
        else:
            while self.has_next():
                operation.perform(self.next())

    def filter(self, predicate):
        """
        Transforms the stream by only keeping items that match the supplied predicate.
        """
        return FilterStream(self, predicate)

    def map(self, function):
        """
        Transforms the stream by applying the supplied function to each item in the stream,
        thus creating a new stream.
        """
        return MapStream(self, function)

    @abc.abstractmethod
    def has_next(self):
        """
        Tests to see if there are any items left in the stream to consume.
        """
        pass

    @abc.abstractmethod
    def next(self):
        """
        Fetches the next item in the stream.
        """
        pass


class FilterStream(AbstractStream):
    """
    A stream created by applying a filter (in the form of a Predicate) to another stream.
    """

    def __init__(self, source, predicate):
        self.source = source
        self.predicate = predicate
        self.obj = None

    def has_next(self):
        if self.obj is not None:
            return True

        while self.source.has_next() and self.obj is None:
            self.obj = self.source.next()
            if not self.predicate.test(self.obj):
                self.obj = None

        return self.obj is not None

    def next(self):
        if not self.has_next():
            raise Exception("Iteration has no more elements")

        to_return = self.obj
        self.obj = None

        return to_return


class MapStream(AbstractStream):
    """
    A stream created by applying a Function to the elements in another stream.
    """

    def __init__(self, source, function):
        self.source = source
        self.function = function

    def has_next(self):
        return self.source.has_next()

    def next(self):
        return self.function.apply(self.source.next())


class BufferedStream(AbstractStream):
    """
    Base implementation of an AbstractStream that uses a BufferedQueue as its internal buffer.

    This class is designed for use with live data sources that may produce data faster than it
    can be consumed, as the internal BufferedQueue will drop items that aren't consumed (i.e,
    removed from the queue) fast enough.
    """

    def __init__(self, buf):
        self.buf = buf
        self.connected = False

    def register(self, item):
        """
        Attempts to 'register' an item with the BufferedStream by offering it to the
        BufferedQueue. Returns True if the item was successfully published to the stream, or False
        if it wasn't.
        """
        return self.buf.offer(item)

    def connect(self):
        """
        Opens the streaming connection to the data source (makes has_next() return True)
        """
        self.connected = True

    def disconnect(self):
        """
        Closes the stream (by making has_next() return False)
        """
        self.connected = False

    def has_next(self):
        return self.connected

    def next(self):
        return self.buf.take()