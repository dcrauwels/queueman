import unittest
from visitor import Visitor

class TestVisitor(unittest.TestCase):
    def test_time_difference(self):
        import time
        time_gap = 0.2
        visitor1 = Visitor()
        time.sleep(time_gap)
        visitor2 = Visitor()
        time_dif = visitor2.get_timestamp() - visitor1.get_timestamp()
        self.assertEqual(round(time_dif, 1), time_gap)

    def test_set_and_get_status(self):
        visitor3 = Visitor()
        visitor3.set_status(1)
        self.assertEqual(visitor3.get_status(), "called")

if __name__ == "__main__":
    unittest.main()
