import pytest
from calculator import add, subtract, multiply, divide, power, factorial, is_prime

class TestAdd:
    def test_positive_numbers(self):
        assert add(2, 3) == 5
        assert add(10, 15) == 25
    
    def test_negative_numbers(self):
        # This test will fail - ISSUE 1
        assert add(-2, 3) == 1
        assert add(5, -3) == 2
        assert add(-4, -5) == -9
    
    def test_zero(self):
        assert add(0, 0) == 0
        assert add(5, 0) == 5

class TestMultiply:
    def test_positive_numbers(self):
        assert multiply(3, 4) == 12
        assert multiply(7, 1) == 7
    
    def test_negative_numbers(self):
        assert multiply(-3, 4) == -12
        assert multiply(3, -4) == -12
        assert multiply(-3, -4) == 12
    
    def test_zero(self):
        assert multiply(0, 5) == 0
        assert multiply(5, 0) == 0
    
    def test_large_numbers(self):
        # This might be slow due to ISSUE 2
        assert multiply(1000, 1000) == 1000000

class TestDivide:
    def test_normal_division(self):
        assert divide(6, 3) == 2
        assert divide(5, 2) == 2.5
    
    def test_division_by_zero(self):
        # This test will fail - ISSUE 3
        with pytest.raises(ValueError):
            divide(5, 0)
    
    def test_negative_division(self):
        assert divide(-6, 3) == -2
        assert divide(6, -3) == -2

class TestPower:
    def test_positive_exponent(self):
        assert power(2, 3) == 8
        assert power(5, 1) == 5
    
    def test_zero_exponent(self):
        assert power(5, 0) == 1
        assert power(0, 0) == 1  # Mathematically debatable, but common in programming
    
    def test_negative_exponent(self):
        # This test will fail - ISSUE 4
        assert power(2, -2) == 0.25
        assert power(5, -1) == 0.2
    
    def test_base_zero(self):
        assert power(0, 5) == 0
        with pytest.raises(ValueError):
            power(0, -1)  # 0 raised to negative power is undefined

class TestFactorial:
    def test_positive_numbers(self):
        assert factorial(0) == 1
        assert factorial(1) == 1
        assert factorial(5) == 120
    
    def test_negative_numbers(self):
        # This test will fail - ISSUE 5
        with pytest.raises(ValueError):
            factorial(-1)
        with pytest.raises(ValueError):
            factorial(-5)

class TestIsPrime:
    def test_prime_numbers(self):
        assert is_prime(2) == True
        assert is_prime(3) == True
        assert is_prime(17) == True
        assert is_prime(29) == True
    
    def test_non_prime_numbers(self):
        assert is_prime(1) == False
        assert is_prime(4) == False
        assert is_prime(15) == False
        assert is_prime(25) == False
    
    def test_edge_cases(self):
        assert is_prime(0) == False
        assert is_prime(-5) == False
    
    def test_negative_numbers(self):
        assert is_prime(-7) == False
        assert is_prime(-10) == False