"""
Unit Tests for Calculator
Students start with 2 passing tests, then add more
"""
import pytest
from src.calculator import add, divide, subtract, multiply, divide, power,sqrt

class TestBasicOperations:
    """Test basic arithmetic operations"""
    
    def test_add_positive_numbers(self):
        """Test adding positive numbers"""
        assert add(2, 3) == 5
        assert add(10, 15) == 25
    
    def test_subtract_positive_numbers(self):
        """Test subtracting positive numbers"""
        assert subtract(5, 3) == 2
        assert subtract(10, 4) == 6

    def test_add_negative_numbers(self):
        """Test adding negative numbers"""
        assert add(-2, -3) == -5
        assert add(-10, 5) == -5
    
    def test_subtract_negative_numbers(self):
        """Test subtracting negative numbers"""
        assert subtract(-5, -3) == -2
        assert subtract(10, -4) == 14  

class TestMultiplyDivideWithValidation:
    """Test multiplication and division with input validation."""
    
    def test_multiply_input_validation(self):
        """Test multiply rejects non-numeric inputs."""
        with pytest.raises(TypeError, match="Both arguments must be numbers"):
            multiply("5", 3)
        with pytest.raises(TypeError, match="Both arguments must be numbers"):
            multiply(5, "3")
    
    def test_divide_input_validation(self):
        """Test divide rejects non-numeric inputs."""
        with pytest.raises(TypeError, match="Division requires numeric inputs"):
            divide("10", 2)

# Test multiplication and division operations
class TestMultiplyDivide:
    """Test multiply and divide functions."""
    def test_multiply_positive_numbers(self):
        assert multiply(2, 3) == 6
        assert multiply(10, 5) == 50

    def test_multiply_negative_numbers(self):
        assert multiply(-2, 3) == -6
        assert multiply(-4, -5) == 20

    def test_multiply_by_zero(self):
        assert multiply(0, 5) == 0
        assert multiply(7, 0) == 0

    def test_divide_positive_numbers(self):
        assert divide(10, 2) == 5
        assert divide(9, 3) == 3

    def test_divide_negative_numbers(self):
        assert divide(-10, 2) == -5
        assert divide(-9, -3) == 3

    def test_divide_by_zero(self):
        with pytest.raises(ValueError, match="division by zero is undefined"):
            divide(5, 0)
        assert divide(0, 5) == 0

# Test power and sqrt operations
class TestPowerSqrt:
    """Test power and sqrt functions."""
    def test_power_positive_numbers(self):
        assert power(2, 3) == 8
        assert power(5, 2) == 25

    def test_power_negative_numbers(self):
        assert power(-2, 3) == -8
        assert power(2, -2) == 0.25

    def test_power_zero(self):
        assert power(0, 5) == 0
        assert power(5, 0) == 1

    def test_power_input_validation(self):
        with pytest.raises(TypeError):
            power("2", 3)
        with pytest.raises(TypeError):
            power(2, "3")

    def test_sqrt_positive_numbers(self):
        assert sqrt(4) == 2
        assert sqrt(9) == 3

    def test_sqrt_zero(self):
        assert sqrt(0) == 0

    def test_sqrt_negative_number(self):
        with pytest.raises(ValueError):
            sqrt(-4)

    def test_sqrt_input_validation(self):
        with pytest.raises(TypeError):
            sqrt("4")