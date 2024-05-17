import pytest

class Math:
    def sum(self, num1: int, num2: int) -> int:
        return num1 + num2

@pytest.fixture
def math() -> Math:
    # Este método devolverá un objeto Math cada vez que 
    # sea pedido por una función de pytest.
    return Math()

@pytest.mark.parametrize("num1, num2, result", [(1, 2, 3), (2, 2, 4)])
def test_sum(math, num1, num2, result):
    # El decorador parametrize nos ayuda a probar diferentes 
    # escenarios de forma automática.
    assert math.sum(num1, num2) == result  
 
 
 
 
 