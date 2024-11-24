import unittest, visitor, queue
from collections import deque

class TestJSON(unittest.TestCase):
    def test_save_read(self):
        q1 = queue.Queue()
        v1 = visitor.Visitor()
        v2 = visitor.Visitor()
        p1 = "purpose 1"
        v3 = visitor.Visitor(p1)
        for v in [v1, v2, v3]:
            q1.add_visitor(v)

        q1.save_to_json()
        q2 = queue.Queue()
        q2.load_from_json()

        self.assertEqual(q1.get_visitor().get_number(), q2.get_visitor().get_number())

    def est_save(self): # NYI
        q3 = queue.Queue()
        v4 = visitor.Visitor()
        v5 = visitor.Visitor()
        for v in [v4, v5]:
            q3.add_visitor(v)
        
        fp = "database/queue.json"
        q3.save_to_json(fp)

if __name__ == "__main__":
    unittest.main()
