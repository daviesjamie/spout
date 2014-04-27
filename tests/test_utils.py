from nose.tools import assert_equal, assert_true, assert_false
from spout.utils import TruePredicate, FalsePredicate, NullOperation, PassThroughFunction

class TestUtils:

    def test_true_predicate(self):
        p = TruePredicate()
        assert_true(p.test('anything'))

    def test_false_predicate(self):
        p = FalsePredicate()
        assert_false(p.test('anything'))

    def test_pass_through_function(self):
        f = PassThroughFunction()
        assert_equal(f.apply('anything'), 'anything')
