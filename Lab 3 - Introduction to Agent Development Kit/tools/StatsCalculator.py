# tools/hdb_calculator.py
from ibm_watsonx_orchestrate.agent_builder.tools import tool

@tool
def add(a: float, b: float) -> float:
    """
    Add two numbers together.

    :param a: First number
    :param b: Second number
    :returns: Sum of a and b
    """
    return a + b


@tool
def subtract(a: float, b: float) -> float:
    """
    Subtract b from a.

    :param a: Number to subtract from
    :param b: Number to subtract
    :returns: a - b
    """
    return a - b


@tool
def multiply(a: float, b: float) -> float:
    """
    Multiply two numbers.

    :param a: First number
    :param b: Second number
    :returns: a * b
    """
    return a * b


@tool
def divide(a: float, b: float) -> float:
    """
    Divide a by b.

    :param a: Dividend
    :param b: Divisor (must not be zero)
    :returns: a / b
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


@tool
def percentage_change(old: float, new: float) -> float:
    """
    Calculate percentage change from old to new value.

    Returns positive for increase, negative for decrease.

    :param old: Original value
    :param new: New value
    :returns: Percentage change as float (e.g. 12.5 means 12.5%)
    """
    if old == 0:
        raise ValueError("Old value cannot be zero for percentage change")
    return (new - old) / old * 100.0
