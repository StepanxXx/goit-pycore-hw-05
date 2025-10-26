"""Module for calculating the total sum of real numbers in a text."""

from typing import Callable
import re
from decimal import Decimal, getcontext

def generator_numbers(text: str):
    """ 
    Function parses the text, identifies all real numbers
    that are considered parts of the income, and returns them as a generator.
    """
    getcontext().prec = 8
    pattern = r"\d+\.\d+"
    for match in re.finditer(pattern, text):
        yield Decimal(match.group(0))

def sum_profit(text: str, func: Callable) -> float:
    """Function for summing numbers and calculating total profit."""
    return float(sum(profit for profit in func(text)))

if __name__ == "__main__" :
    TEXT = "Загальний дохід працівника складається з декількох" \
        " частин: 1000.01 як основний дохід, доповнений додатковими" \
        " надходженнями 27.45 і 324.00 доларів."
    total_income = sum_profit(TEXT, generator_numbers)
    print(f"Загальний дохід: {total_income}")
    # Загальний дохід: 1351.46
