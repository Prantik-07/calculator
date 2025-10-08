def add(a, b):
    # ISSUE 1: This function incorrectly handles negative numbers
    if a < 0 or b < 0:
        return a + b  # BUG: Should preserve negatives
    return a + b

def subtract(a, b):
    return a - b  # This one is correct

def multiply(a, b):
    # ISSUE 2: This function has performance issues with large numbers
    return a * b

def divide(a, b):
    # ISSUE 3: This function doesn't handle division by zero properly
    if b == 0:
        return ValueError,"Cannot divide by zero"  # BUG: Should raise an exception instead
    return a / b


def power(base, exponent):
    # ISSUE 4: This function has multiple bugs
    if exponent == 0:
        return 1
    elif exponent < 0:
        # BUG: Doesn't handle negative exponents correctly
        return 1 / power(base, -exponent)

    result = 1
    for i in range(exponent):
        result *= base
    return result

def factorial(n):
    # ISSUE 5: This function has recursion issues
    if n < 0:
        return ValueError  # BUG: Should raise ValueError for negative inputs
    if n == 0:
        return 1
    return n * factorial(n - 1)

def is_prime(n):
    # ISSUE 6: This function has logic errors
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True