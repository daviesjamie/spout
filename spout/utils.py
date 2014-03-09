from structs import Operation, Predicate


class PrintOperation(Operation):
    """
    Simple operation to print whatever input is supplied.
    """
    def perform(self, obj):
        print obj


class TruePredicate(Predicate):
    """
    Simple predicate that always returns True.
    """
    def test(self, obj):
        return True


class NullOperation(Operation):
    """
    An empty operation that does nothing, it is simply used to 'pull' objects through the
    previous operations in the stream pipeline.
    """
    def perform(self, obj):
        pass
