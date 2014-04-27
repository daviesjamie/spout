from structs import Operation, Predicate, Function


class TruePredicate(Predicate):
    """
    Simple predicate that always returns True.
    """
    def test(self, obj):
        return True


class FalsePredicate(Predicate):
    """
    Simple predicate that always returns False.
    """
    def test(self, obj):
        return False


class PassThroughFunction(Function):
    """
    Simple function that returns everything given to it.
    """
    def apply(self, input):
        return input


class NullOperation(Operation):
    """
    An empty operation that does nothing, it is simply used to 'pull' objects through the
    previous operations in the stream pipeline.
    """
    def perform(self, obj):
        pass
