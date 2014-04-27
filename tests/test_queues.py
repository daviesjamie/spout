from nose.tools import nottest
from nose.tools import assert_equal, assert_true, assert_false
from spout.queues import QueueBufferedQueue

class TestQueueBufferedQueue:

    def test_adding_to_queue(self):
        q = QueueBufferedQueue(1)
        q.offer('test')
        assert_equal(q.queue.get(), 'test')

    def test_removing_from_queue(self):
        q = QueueBufferedQueue(1)
        q.offer('test')
        assert_equal(q.take(), 'test')

    def test_dropping_when_full(self):
        q = QueueBufferedQueue(1)
        assert_true(q.offer('test'))
        assert_false(q.offer('another test'))

    # Fails, because multiprocessing.queue.qsize() is not implemented
    @nottest
    def test_remaining_capacity(self):
        q = QueueBufferedQueue(3)
        assert_equal(q.remaining_capacity(), 3)
        q.offer('test')
        assert_equal(q.remaining_capacity(), 2)
        q.offer('blah')
        q.offer('another thing')
        assert_equal(q.remaining_capacity(), 0)
        q.take()
        assert_equal(q.remaining_capacity(), 1)
