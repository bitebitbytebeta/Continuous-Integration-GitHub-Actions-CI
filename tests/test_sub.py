import unittest

import sys
from src.sub import sub

class TestSubFuncs(unittest.TestCase):
    def test_sub(self):
        self.assertEqual(sub(2, 3), 5)
        self.assertEqual(sub(-1, 1), 0)
        self.assertEqual(sub(0, 0), 0)

# def test_sub():
    # assert sub(2, 3) == -1
    # assert sub(-1, 1) == -2
    # assert sub(0, 0) == 0

if __name__ == "__main__":
    unittest.main()
