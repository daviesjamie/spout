from flow.structures import Operation, Predicate


class PrintOperation(Operation):
    """
    Simple operation to print whatever input is supplied. Used for testing purposes only.
    """
    def perform(self, obj):
        print obj


class TruePredicate(Predicate):
    """
    Simple predicate that always returns True. Used for testing purposes only.
    """
    def test(self, obj):
        return True


class NullOperation(Operation):
    """
    An empty operation that does nothing, it is simply used to pull objects through the stream.
    Used for testing purposes only.
    """
    def perform(self, obj):
        pass
