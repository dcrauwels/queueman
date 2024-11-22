import unittest, visitor

class TestVisitor(unittest.TestCase):
    def test_time_difference(self):
        import time
        visitor1 = visitor.Visitor()
        time.sleep(0.5)
        visitor2 = visitor.Visitor()
        time_dif = visitor2.get_timestamp() - visitor1.get_timestamp()
        self.assertEqual(round(time_dif, 1), 0.5)

    def test_set_and_get_status(self):
        visitor3 = visitor.Visitor()
        visitor3.set_status(1)
        self.assertEqual(visitor3.get_status(), "called")

if __name__ == "__main__":
    unittest.main()
