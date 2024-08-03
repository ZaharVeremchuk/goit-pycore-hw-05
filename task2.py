# Import useful libraries
from typing import Callable
from decimal import Decimal
import re

# Created generator for convert text to decimal numbers
def generator_numbers(text: str):
    matches = re.findall(r"\d+.\d*", text) # pattern for search numbers
    for index in range(0, len(matches)):
        yield Decimal(matches[index])

# Function to get total_sum of all numbers in text
def sum_profit(text: str, func: Callable):
    total_sum = 0
    for number in func(text):
        total_sum += number # sum number returned by generator
    return total_sum
         
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
