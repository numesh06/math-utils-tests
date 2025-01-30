import pytest
from src.math_utils import MathUtils

class TestMathUtils:
    def test_add(self):
        assert MathUtils.add(3, 2) == 5
        assert MathUtils.add(-3, -2) == -5
        assert MathUtils.add(-1, 1) == 0
        assert MathUtils.add(1 , -1) == 0
        assert MathUtils.add(0, 0) == 0
        assert MathUtils.add(-1, 0) == -1
        assert MathUtils.add(0, -1) == -1
        assert MathUtils.add(1, 0) == 1
        assert MathUtils.add(0, 1) == 1

    def test_subtract(self):
        assert MathUtils.subtract(5, 3) == 2
        assert MathUtils.subtract(-5, -3) == -2
        assert MathUtils.subtract(-1, 1) == -2
        assert MathUtils.subtract(1, -1) == 2
        assert MathUtils.subtract(0, 0) == 0
        assert MathUtils.subtract(0, -1) == 1
        assert MathUtils.subtract(-1, 0) == -1
        assert MathUtils.subtract(1, 0) == 1
        assert MathUtils.subtract(0, 1) == -1

    def test_multiply(self):
        assert MathUtils.multiply(3, 2) == 6
        assert MathUtils.multiply(-1, 5) == -5
        assert MathUtils.multiply(0, 100) == 0

    def test_divide(self):
        assert MathUtils.divide(6, 2) == 3.0
        assert MathUtils.divide(5, 2) == 2.5
        assert MathUtils.divide(10, 0) == -1.0
        assert MathUtils.divide(-10, -5) == 2.0
        assert MathUtils.divide(0, -5) == 0
        assert MathUtils.divide(-5, 0) == -1.0
