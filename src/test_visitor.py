import unittest, visitor

class TestVisitor(unittest.TestCase):
    def time_difference(self):
        import time
        visitor1 = Visitor()
        time.sleep(2)
        visitor2 = Visitor()
        time_dif = visitor2.get_timestamp().second - visitor1.get_timestamp().second 
        self.assertEqual(time_dif, 2)



if __name__ == "__main__":
    unittest.main()
