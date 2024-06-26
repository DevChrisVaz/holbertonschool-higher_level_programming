#!/usr/bin/python3
# 9-print_last_digit.py
# Christian Alexander Vazquez Gonzalez <dev.chrisvaz@gmail.com>


def print_last_digit(number):
    """Print the last digit of a number and return it."""
    print(abs(number) % 10, end="")
    return (abs(number) % 10)
