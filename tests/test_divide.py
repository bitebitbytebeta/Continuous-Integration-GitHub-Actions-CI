import unittest

import sys
from src.divide import floor_divide

class TestDivideFLoorFuncs(unittest.TestCase):
    def test_sub(self):
        self.assertEqual(floor_divide(10, 3), 3)
        self.assertEqual(floor_divide(25, 4), 6)
        self.assertEqual(floor_divide(8, 3), 2)

if __name__ == "__main__":
    unittest.main()
