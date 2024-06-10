#!/usr/bin/python3
# 4-only_diff_elements.py
# Christian Alexander Vazquez Gonzalez <dev.chrisvaz@gmail.com>


def only_diff_elements(set_1, set_2):
    """Return a set of all elements present in only one set."""
    return (set_1 ^ set_2)
