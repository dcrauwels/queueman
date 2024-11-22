import unittest, visitor, queue
from collections import deque

class TestQueue(unittest.TestCase):
    def test_add_visitor_simple(self):
        queue1 = queue.Queue()
        v1 = visitor.Visitor()
        v2 = visitor.Visitor()
        queue1.add_visitor(v1)
        queue1.add_visitor(v2)
        self.assertEqual(queue1.get_queue(), deque([v1,v2]))

    def test_get_purposes(self):
        q2 = queue.Queue()
        # p1 visitors
        v3 = visitor.Visitor("p1")
        v4 = visitor.Visitor("p1")
        # p2 visitors
        v5 = visitor.Visitor("p2")
        # no purpose visitors
        v6 = visitor.Visitor()
        # append to queue
        for v in [v3, v4, v5, v6]:
            q2.add_visitor(v)

        # check purposes in purpose dict keys
        self.assertEqual(list(q2.get_purposes()), ["p1", "p2"])
        # check waiting count in p1 queue
        self.assertEqual(q2.get_waiting_count("p1"), 2)
        # check v5 in p2 queue
        self.assertEqual(q2["p2"].get_queue(), deque([v5]))
        

if __name__ == "__main__":
    unittest.main()
