# Calculator Multi-Issues Repository

A calculator library with multiple bugs for educational purposes. Students should clone this repository and fix all the issues.

## Issues to Fix

### Issue 1: Negative Number Addition
- **File**: `calculator.py` - `add()` function
- **Problem**: The `add()` function incorrectly handles negative numbers by using absolute values
- **Expected**: `add(-2, 3)` should return `1`, not `5`
- **Test**: `test_negative_numbers` in `TestAdd` class

### Issue 2: Inefficient Multiplication
- **File**: `calculator.py` - `multiply()` function
- **Problem**: Uses slow iterative approach for large numbers
- **Expected**: Should use direct multiplication operator `*`
- **Test**: `test_large_numbers` in `TestMultiply` class

### Issue 3: Division by Zero Handling
- **File**: `calculator.py` - `divide()` function
- **Problem**: Returns `inf` instead of raising an exception for division by zero
- **Expected**: Should raise `ValueError` with message "Cannot divide by zero"
- **Test**: `test_division_by_zero` in `TestDivide` class

### Issue 4: Negative Exponents in Power
- **File**: `calculator.py` - `power()` function
- **Problem**: Recursive call with negative exponent causes infinite recursion
- **Expected**: Should handle negative exponents correctly
- **Test**: `test_negative_exponent` in `TestPower` class

### Issue 5: Factorial with Negative Input
- **File**: `calculator.py` - `factorial()` function
- **Problem**: Returns `-1` for negative inputs instead of raising exception
- **Expected**: Should raise `ValueError` for negative inputs
- **Test**: `test_negative_numbers` in `TestFactorial` class

### Issue 6: Prime Number Detection
- **File**: `calculator.py` - `is_prime()` function
- **Problem**: Inefficient and may have logical errors
- **Expected**: Should correctly identify prime numbers
- **Tests**: All tests in `TestIsPrime` class

## Setup Instructions

1. Clone the repository:
```bash
git clone <repository-url>
cd calculator-multi-issues