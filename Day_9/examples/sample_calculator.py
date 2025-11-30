#!/usr/bin/env python3
"""
Sample Calculator Project for Git Practice
Day 9: Git Version Control

This file serves as an example project that students can use
to practice Git commands.
"""


def add(a: float, b: float) -> float:
    """
    Add two numbers together.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        Sum of a and b
        
    Example:
        >>> add(10, 5)
        15
    """
    return a + b


def subtract(a: float, b: float) -> float:
    """
    Subtract b from a.
    
    Args:
        a: Number to subtract from
        b: Number to subtract
        
    Returns:
        Difference of a and b
        
    Example:
        >>> subtract(10, 5)
        5
    """
    return a - b


def multiply(a: float, b: float) -> float:
    """
    Multiply two numbers.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        Product of a and b
        
    Example:
        >>> multiply(10, 5)
        50
    """
    return a * b


def divide(a: float, b: float) -> float:
    """
    Divide a by b.
    
    Args:
        a: Dividend
        b: Divisor
        
    Returns:
        Quotient of a and b
        
    Raises:
        ValueError: If b is zero
        
    Example:
        >>> divide(10, 5)
        2.0
    """
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b


def power(base: float, exponent: float) -> float:
    """
    Raise base to the power of exponent.
    
    Args:
        base: The base number
        exponent: The power to raise to
        
    Returns:
        base raised to the power of exponent
        
    Example:
        >>> power(2, 8)
        256
    """
    return base ** exponent


def modulo(a: float, b: float) -> float:
    """
    Calculate remainder of a divided by b.
    
    Args:
        a: Dividend
        b: Divisor
        
    Returns:
        Remainder of a / b
        
    Raises:
        ValueError: If b is zero
        
    Example:
        >>> modulo(10, 3)
        1
    """
    if b == 0:
        raise ValueError("Cannot calculate modulo with zero!")
    return a % b


def main():
    """Main function to demonstrate calculator operations."""
    print("=" * 40)
    print("       Simple Calculator Demo")
    print("=" * 40)
    print()
    
    # Basic operations
    print("Basic Operations:")
    print(f"  10 + 5 = {add(10, 5)}")
    print(f"  10 - 5 = {subtract(10, 5)}")
    print(f"  10 * 5 = {multiply(10, 5)}")
    print(f"  10 / 5 = {divide(10, 5)}")
    print()
    
    # Advanced operations
    print("Advanced Operations:")
    print(f"  2 ^ 8 = {power(2, 8)}")
    print(f"  10 % 3 = {modulo(10, 3)}")
    print()
    
    # Interactive mode
    print("Try it yourself!")
    print("-" * 40)
    
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        print(f"\nResults:")
        print(f"  {num1} + {num2} = {add(num1, num2)}")
        print(f"  {num1} - {num2} = {subtract(num1, num2)}")
        print(f"  {num1} * {num2} = {multiply(num1, num2)}")
        
        if num2 != 0:
            print(f"  {num1} / {num2} = {divide(num1, num2)}")
            print(f"  {num1} % {num2} = {modulo(num1, num2)}")
        else:
            print("  Division and modulo by zero not allowed!")
            
        print(f"  {num1} ^ {num2} = {power(num1, num2)}")
        
    except ValueError as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print("\nGoodbye!")


if __name__ == "__main__":
    main()
