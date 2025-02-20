import pytest
import sys
import os

# Add src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from calculator import add, sub, mul, div  # Stellen Sie sicher, dass diese Datei existiert und die Funktionen definiert sind

def test_add():
    assert add(2, 3) == 5

def test_sub():
    assert sub(2, 3) == -1

def test_mul():
    assert mul(2, 3) == 6

def test_div():
    assert div(6, 3) == 2
    with pytest.raises(ValueError):
        div(10, 0)
