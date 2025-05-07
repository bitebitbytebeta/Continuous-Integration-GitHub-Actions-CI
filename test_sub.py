import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from src.sub import sub

def test_sub():
    assert sub(2, 3) == -1
    assert sub(-1, 1) == -2
    assert sub(0, 0) == 0