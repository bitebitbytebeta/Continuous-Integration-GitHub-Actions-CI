import unittest

import sys
from src.sub import sub

def test_sub():
    assert sub(2, 3) == -1
    assert sub(-1, 1) == -2
    assert sub(0, 0) == 0

if __name__ == "__main__":
    unittest.main()
