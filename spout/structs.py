import abc


class Operation(object):
    """
    Defines an operation that can be applied to items in a stream.
    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def perform(self, obj):
        pass


class Predicate(object):
    """
    Used to apply a boolean test to items in a stream, to determine if it meets some set
    criteria.
    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def test(self, obj):
        pass


class Function(object):
    """
    Applies a function to items in a stream, producing an appropriate result.
    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def apply(self, input):
        pass

