from hypothesis import given, strategies as st

class Math:
    def sum(self, num1: int, num2: int) -> int:
        return num1 + num2

@given(num1=st.integers(), num2=st.integers())
def test_decode_inverts_encode(num1: int, num2: int):
    # Las strategies en hypothesis son los que se encargan 
    # de la generación aleatoria de los inputs
    # en nuestro testing.
    math = Math()
    assert math.sum(num1, num2) == num1 + num2

