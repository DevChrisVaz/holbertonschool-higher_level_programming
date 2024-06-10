#!/usr/bin/python3
# 1-square.py
# Christian Alexander Vazquez Gonzalez <dev.chrisvaz@gmail.com>
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        self.__size = size
