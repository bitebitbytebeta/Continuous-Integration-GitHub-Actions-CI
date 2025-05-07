import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from main import add_number as add

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0