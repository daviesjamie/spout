from nose.tools import assert_equal, assert_true, assert_false, assert_is_instance
from spout.streams import Stream, FilterStream, MapStream
from spout.utils import TruePredicate, FalsePredicate, PassThroughFunction, NullOperation


class SimpleTestingStream(Stream):
    def __init__(self):
        self.data = ['test1', 'test2', 'test3']
        self.head = 0

    def has_next(self):
        return self.head < len(self.data)

    def next(self):
        to_return = self.data[self.head]
        self.head += 1
        return to_return


class TestStream:

    def test_testing_stream(self):
        s = SimpleTestingStream()
        assert_equal(s.next(), 'test1')
        assert_equal(s.next(), 'test2')
        assert_equal(s.next(), 'test3')

    def test_filter_returns_filter_stream(self):
        s = SimpleTestingStream()
        f = s.filter(TruePredicate())

        assert_is_instance(f, FilterStream)

    def test_map_returns_map_stream(self):
        s = SimpleTestingStream()
        m = s.map(PassThroughFunction())

        assert_is_instance(m, MapStream)

    def test_for_each_returns_nothing(self):
        s = SimpleTestingStream()
        n = s.for_each(NullOperation())

        assert_equal(n, None)

    def test_filter_is_applied(self):
        s = SimpleTestingStream()

        f = s.filter(TruePredicate())
        assert_true(f.has_next())
        assert_equal(f.next(), 'test1')

        f = s.filter(FalsePredicate())
        assert_false(f.has_next())

