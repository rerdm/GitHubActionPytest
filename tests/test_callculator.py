import pytest
from src.calculator import add
from src.calculator import sub

def test_add():
    """Test test the add function from callculator program."""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    
def test_sub():
    """Test test the substract function from callculator program."""
    assert sub(2, 3) == 5
    assert sub(1, 1) == 0
    assert sub(5, 5) == 0
    


if __name__ == "__main__":
    pytest.main()
